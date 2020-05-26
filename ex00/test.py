from book import Book
from recipe import Recipe
import traceback

burger = Recipe('burger', 1, 11, ['bread', 'steak', 'cheese'], 'lunch')
print("\nTEST 1")
try:
    burger = Recipe('burger', 1, 11, ['bread', 'steak', 'cheese'], 'lunch')
    print(burger)
    salad = Recipe('salad', 1, 11, ['bread', 'steak', 'cheese'], 'lunch')
    burgerbis = Recipe('burger', 2, 12, ['bread', 'steak', 'cheese'], 'lunch')
    # line to modify to test errors on recipe creation :
    recipe = Recipe('', 1, 11, ['bread', 'steak', 'cheese'], 'lunch')
except Exception:
    traceback.print_exc()

print("\nTEST 2")
try:
    book = Book("Mon cookbook")
    book2 = Book()
    # line to modify to test errors on book creation :
    book3 = Book("")
except Exception:
    traceback.print_exc()

print("\nTEST 3")
try:
    book.add_recipe(burger)
    book.add_recipe(salad)
    print(book.get_recipes_by_types('lunch'))
    print(book.get_recipes_by_types('dessert'))
    print(book.get_recipe_by_name('burger'))
    print(book.get_recipe_by_name('salad'))
    print(book.get_recipe_by_name('roasted fries'))
    book.add_recipe(burger)
except Exception:
    traceback.print_exc()

print("\nTEST 5")
try:
    book.get_recipes_by_types('dinner')
except Exception:
    traceback.print_exc()

print("\nTEST 6")
try:
    book.add_recipe('notarecipe')
except Exception:
    traceback.print_exc()
