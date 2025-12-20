import pulp


def solve_model(model: pulp.LpProblem, portions: dict, products: dict) -> dict:
    """
    Solves the model and returns the solution.
    """

    model.solve(pulp.PULP_CBC_CMD(msg=True))

    solution = {
        name: variable.value()
        for name, variable in portions.items()
        if variable.value() and variable.value() > 0
    }

    total_calories = sum(products[name] * solution[name] for name in solution)

    return {
        "status": pulp.LpStatus[model.status],
        "portions": solution,
        "total_calories": total_calories,
    }
