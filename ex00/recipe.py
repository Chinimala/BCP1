class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description=""):
        if not isinstance(name, str):
            raise TypeError("name should be str")
        elif not isinstance(cooking_lvl, int):
            raise TypeError("cooking_lvl should be int")
        elif not isinstance(cooking_time, int):
            raise TypeError("cooking_time should be int")
        elif not isinstance(ingredients, list):
            raise TypeError("ingredients should be a list of strings")
        elif not isinstance(recipe_type, str):
            raise TypeError("recipe_type should be str")
        elif not isinstance(description, str):
            raise TypeError("description should be str")

        if name == "":
            raise ValueError("name cannot be empty")
        elif cooking_lvl not in range(1, 5):
            raise ValueError("cooking_lvl must in range 1 to 5")
        elif cooking_time < 0:
            raise ValueError("cooking_time must be positive")
        elif not all(isinstance(i, str) and i != "" for i in ingredients):
            raise ValueError("ingredients must be strings")
        elif recipe_type not in ["starter", "lunch", "dessert"]:
            raise TypeError("recipe_type must be starter, lunch or dessert")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description
        print("Recipe for", name, "successfully created !")

    def __str__(self):
        """String to print()"""

        return self.name
