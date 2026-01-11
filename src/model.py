from pulp import LpProblem, LpVariable, LpMinimize, lpSum

TARGET_CALORIES = 1600
MAX_PORTIONS_PER_PRODUCT = 4
MANDATORY_PRODUCTS = []


def build_model(products):
    model = LpProblem("Meal_Optimization", LpMinimize)

    # Переменные: порции продуктов
    portions = {
        name: LpVariable(name, 0, MAX_PORTIONS_PER_PRODUCT) for name in products
    }

    # Обязательные продукты
    for name in MANDATORY_PRODUCTS:
        if name in portions:
            portions[name].lowBound = 1

    # Суммарные калории
    total_calories = lpSum(
        [products[name]["calories"] * portions[name] for name in portions]
    )

    # Вводим переменные отклонений
    over = LpVariable("over_calories", 0)
    under = LpVariable("under_calories", 0)

    # Ограничение: total_calories + over - under = TARGET
    model += total_calories + over - under == TARGET_CALORIES

    # Целевая функция: минимизируем сумму отклонений
    model += over + under

    return model, portions
