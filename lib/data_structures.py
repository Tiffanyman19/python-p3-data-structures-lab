spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicy_food.get('name') for spicy_food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    heat_levels = [spicy_food.get("heat_level") for spicy_food in spicy_foods]
    max_heat_level = max(heat_levels)
    spiciest_food = [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
    return spiciest_food
    pass

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {spicy_food['heat_level'] * '🌶'}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    pass

def print_spiciest_foods(spicy_foods):
    spicy_food_above_level = [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
    print_spicy_foods(spicy_food_above_level)
    pass

def get_average_heat_level(spicy_foods):
    heat_levels = [spicy_food["heat_level"] for spicy_food in spicy_foods]
    avg_heat_level = sum(heat_levels) / len(heat_levels)
    return avg_heat_level
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return  spicy_foods

    pass
