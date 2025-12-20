from pulp import *


def build_model(products, max_calories):
    model = LpProblem("DailyFood", LpMinimize)

    variables = {name: LpVariable(name, lowBound=0, cat="Integer") for name in products}

    # суп обязателен
    variables["soup"].lowBound = 1
    variables["soup"].upBound = 1

    # цель
    model += lpSum(products[p] * variables[p] for p in products)

    # ограничение
    model += lpSum(products[p] * variables[p] for p in products) <= max_calories

    return model, variables
