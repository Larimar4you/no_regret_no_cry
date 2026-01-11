from src.nutrition import get_product_nutrition
from src.build_model import build_model
from src.solver import solve_model


def pretty_print(result):
    print("\n==============================")
    print("     РЕЗУЛЬТАТ ОПТИМИЗАЦИИ")
    print("==============================\n")

    print(f"Статус: {result['status']}\n")

    print("Выбранные продукты и порции (г):")
    for product, amount in result["portions"].items():
        print(f"  • {product:<15} {amount:>6.1f}")

    print(f"\nОбщие калории: {result['total_calories']:.1f} kcal")
    print("\n==============================\n")


def main():
    # Ввод продуктов пользователем
    product_names = input("Введите продукты через запятую: ").split(",")
    product_names = [p.strip() for p in product_names if p.strip()]

    if not product_names:
        print("❌ Вы не ввели ни одного продукта.")
        return

    # Получаем нутриенты через API + кэш
    products = {}
    for name in product_names:
        products[name] = get_product_nutrition(name)

    # Строим модель PuLP
    model, portions = build_model(products)
    result = solve_model(model, portions, products)

    # 👉 ВЫВОД РЕЗУЛЬТАТА
    pretty_print(result)


if __name__ == "__main__":
    main()
