import json
from src.model import build_model
from src.solver import solve_model


def main():
    with open("data/products.json", "r") as file:
        products = json.load(file)

    model, portions = build_model(products)
    result = solve_model(model, portions, products)

    print(f"Status: {result['status']}")
    print("Selected products:")
    for product, amount in result["portions"].items():
        print(f"  {product}: {amount}")

    print(f"Total calories: {result['total_calories']} kcal")


if __name__ == "__main__":
    main()
