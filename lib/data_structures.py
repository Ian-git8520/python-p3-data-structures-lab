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
    """Returns a list of names of each spicy food"""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Returns a list of dictionaries where heat level is greater than 5"""
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """Prints each spicy food with its heat level in peppers"""
    for food in spicy_foods:
        heat_peppers = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_peppers}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns a single dictionary for the spicy food matching the cuisine"""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    """Prints only the spicy foods with heat level greater than 5"""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    """Returns the average heat level of all spicy foods"""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    """Adds a new spicy food to the list and returns the updated list"""
    spicy_foods.append(spicy_food)
    return spicy_foods



if __name__ == "__main__":
    print("=== Testing get_names() ===")
    print(get_names(spicy_foods))
   
    
    print("\n=== Testing get_spiciest_foods() ===")
    print(get_spiciest_foods(spicy_foods))
   
    
    print("\n=== Testing print_spicy_foods() ===")
    print_spicy_foods(spicy_foods)
    
    print("\n=== Testing get_spicy_food_by_cuisine() ===")
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))
   
    
    print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
    
    
    print("\n=== Testing print_spiciest_foods() ===")
    print_spiciest_foods(spicy_foods)
    
    print("\n=== Testing get_average_heat_level() ===")
    print(get_average_heat_level(spicy_foods))
   
    
    print("\n=== Testing create_spicy_food() ===")
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    updated_list = create_spicy_food(spicy_foods.copy(), new_food)
    print(f"List now has {len(updated_list)} items")
    print(f"Last item: {updated_list[-1]}")
    