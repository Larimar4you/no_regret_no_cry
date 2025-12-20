# 🥗 NO_REGRET_NO_CRY/Food Optimizer (PuLP)

Optimizes daily meals based on available products to reach a target
calorie intake (~1600 kcal) with flexible under- and over-consumption.

## Features:

- Target calories with soft limits
- Mandatory products (e.g., soup)
- Integer portion sizes
- Optimizes from available fridge products

## Tech:

- Python
- PuLP (Mixed Integer Linear Programming)

## How to use:

pip install -r requirements.txt
python main.py

## SettingsConfiguration

- Calorie target & tolerance: src/config.py
- Food products & calories: data/products.json

## My Idea:

Demonstrates resource optimization in meal planning, selecting optimal portions of available products while minimizing deviation from a target calorie goal.
