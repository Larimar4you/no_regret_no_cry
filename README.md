# 🥗 NO_REGRET_NO_CRY/Food Optimizer (PuLP)

Daily meal optimizer that takes into account:

- a maximum calorie limit
- mandatory dishes (for example, soup)
- integer portion sizes

## Tech

- Python
- PuLP (Linear Programming)

## How to use:

pip install -r requirements.txt
python main.py

## Settings

- calorie limits: src/config.py
- food products and calorie values: data/products.json

## My Idea:

The project demonstrates an approach to resource optimization
by managing calorie limits, food products, and their calorie values.
Although the maximum calorie limit is set to 1600 kcal, the model minimizes total calorie intake. Since only soup is mandatory, the optimizer selects the minimum feasible solution that satisfies all constraints.
