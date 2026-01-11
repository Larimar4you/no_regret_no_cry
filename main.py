from src.nutrition import get_product_nutrition
from src.model import build_model
from src.solver import solve_model


def main():
    # Ввод продуктов пользователем
    product_names = input("Введите продукты через запятую: ").split(",")
    product_names = [p.strip() for p in product_names if p.strip()]

    # Получаем нутриенты через API + кэш
    products = {}
    for name in product_names:
        products[name] = get_product_nutrition(name)

    # Строим модель PuLP
    model, portions = build_model(products)
    result = solve_model(model, portions, products)

    print(f"\nСтатус оптимизации: {result['status']}")
    print("Выбранные продукты и порции (г):")
    for product, amount in result["portions"].items():
        print(f"  {product}: {amount:.1f}")

    print(f"\nОбщие калории: {result['total_calories']:.1f} kcal")


if __name__ == "__main__":
    main()
