import pulp
from .config import (
    TARGET_CALORIES,
    MIN_CALORIES,
    MAX_CALORIES,
    MAX_PORTIONS_PER_PRODUCT,
    MANDATORY_PRODUCTS,
)


def build_model(products: dict) -> tuple[pulp.LpProblem, dict]:
    """
    Builds a MILP model for daily food optimization.
    """

    model = pulp.LpProblem("FoodOptimizer", pulp.LpMinimize)

    # Decision variables: number of portions per product
    portions = {
        name: pulp.LpVariable(
            name,
            lowBound=0,
            upBound=MAX_PORTIONS_PER_PRODUCT,
            cat="Integer",
        )
        for name in products
    }

    # Total calories
    total_calories = pulp.lpSum(products[name] * portions[name] for name in products)

    # Hard calorie bounds
    model += total_calories >= MIN_CALORIES
    model += total_calories <= MAX_CALORIES

    # Mandatory products
    for product in MANDATORY_PRODUCTS:
        model += portions[product] >= 1

    # Soft deviation variables
    under = pulp.LpVariable("under_consumption", lowBound=0)
    over = pulp.LpVariable("over_consumption", lowBound=0)

    model += under >= TARGET_CALORIES - total_calories
    model += over >= total_calories - TARGET_CALORIES

    # Objective: minimize deviation from target calories
    model += under + over

    return model, portions
