from pulp import LpProblem, LpVariable, LpMinimize, lpSum

TARGET_CALORIES = 1600
MAX_PORTIONS_PER_PRODUCT = 4
MIN_PORTIONS_PER_PRODUCT = 0.5


def build_model(products):
    model = LpProblem("Meal_Optimization", LpMinimize)

    # Переменные: порции продуктов
    portions = {
        name: LpVariable(name, MIN_PORTIONS_PER_PRODUCT, MAX_PORTIONS_PER_PRODUCT)
        for name in products
    }

    # Суммарные калории
    total_calories = lpSum(
        [products[name]["calories"] * portions[name] for name in portions]
    )

    # Переменные отклонений
    over = LpVariable("over_calories", 0)
    under = LpVariable("under_calories", 0)

    # Ограничение: total_calories + over - under = TARGET
    model += total_calories + over - under == TARGET_CALORIES

    # Цель: минимизируем отклонения + немного разнообразия
    model += over + under + 0.1 * lpSum(portions.values())

    return model, portions
