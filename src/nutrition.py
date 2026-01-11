import os
import json
from dotenv import load_dotenv
from usda_fdc import FdcClient

load_dotenv()
API_KEY = os.getenv("USDA_API_KEY")
client = FdcClient(API_KEY)

CACHE_FILE = os.path.join(os.path.dirname(__file__), "../products_cache.json")

# Загружаем кэш
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}


def save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def get_product_nutrition(product_name: str):
    name_lower = product_name.lower()
    if name_lower in cache:
        return cache[name_lower]

    results = client.search(product_name)
    if not results.foods:
        result = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        cache[name_lower] = result
        save_cache()
        return result

    food = results.foods[0]
    fdc_id = food.fdc_id

    nutrients = client.get_nutrients(fdc_id)
    nutrient_map = {n.name.lower(): n.amount for n in nutrients}

    result = {
        "calories": nutrient_map.get("energy", 0),
        "protein": nutrient_map.get("protein", 0),
        "fat": nutrient_map.get("total lipid (fat)", 0),
        "carbs": nutrient_map.get("carbohydrate, by difference", 0),
    }

    cache[name_lower] = result
    save_cache()
    return result
