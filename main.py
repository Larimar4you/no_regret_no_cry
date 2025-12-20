import json
from src.model import build_model
from src.config import MAX_CALORIES
from pulp import LpStatus, value

with open("data/products.json") as f:
    products = json.load(f)

model, vars = build_model(products, MAX_CALORIES)
model.solve()

print("Статус:", LpStatus[model.status])
for v in vars.values():
    print(v.name, "=", v.varValue)

print("Всего ккал:", value(model.objective))
