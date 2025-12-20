# Target calories for the day
TARGET_CALORIES = 1600

# Allowed deviations (soft limits)
CALORIE_TOLERANCE_UNDER = 150  # allowed calorie deficit
CALORIE_TOLERANCE_OVER = 100  # allowed calorie surplus

MIN_CALORIES = TARGET_CALORIES - CALORIE_TOLERANCE_UNDER
MAX_CALORIES = TARGET_CALORIES + CALORIE_TOLERANCE_OVER

# Mandatory products (if any)
MANDATORY_PRODUCTS = ["soup"]

# Portion limits
MAX_PORTIONS_PER_PRODUCT = 4
