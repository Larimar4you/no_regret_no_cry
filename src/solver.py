from pulp import LpStatus, PULP_CBC_CMD


def solve_model(model, portions, products):
    solver = PULP_CBC_CMD(msg=False)
    model.solve(solver)

    result = {
        "status": LpStatus[model.status],
        "portions": {name: round(portions[name].varValue, 1) for name in portions},
        "total_calories": round(
            sum(
                products[name]["calories"] * portions[name].varValue
                for name in portions
            ),
            1,
        ),
    }
    return result
