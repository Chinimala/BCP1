from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name="My cookbook"):
        if not isinstance(name, str):
            raise TypeError("name should be str")
        elif name == "":
            raise ValueError("name cannot be empty")

        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {'starter': {}, 'lunch': {}, 'dessert': {}}
        print("Book", name, "successfully created !")

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""

        if not isinstance(name, str):
            raise TypeError("name should be str")
        for recipe_type in self.recipes_list.keys():
            if name in self.recipes_list[recipe_type]:
                print("Getting the", recipe_type,
                      self.recipes_list[recipe_type][name])
                return self.recipes_list[recipe_type][name]
        return

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """

        if recipe_type not in self.recipes_list:
            raise ValueError("recipe_type must be "
                             + ' or '.join(self.recipes_list.keys()))
        return list(self.recipes_list[recipe_type].keys())

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""

        if not isinstance(recipe, Recipe):
            raise ValueError("recipe must be a Recipe")
        if self.get_recipe_by_name(recipe.name) is not None:
            raise ValueError("this recipe is already in the book")
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.now()
        print(recipe.name, "succesfully added to", self.name, "!")
