
class Recipe:
	'''Recipe Class. Recipe(name, lvl, time, ingredients, type, description)'''
	name = str
	lvl = int
	time = int
	ingr = [str]
	type = str
	descr = str

	def __init__(self, name, lvl, time, ingr, type, descr='Not available.'):
		self.name = name
		self.lvl = lvl
		self.time = time
		self.ingr = ingr
		self.type = type
		self.descr = descr

	def __str__(self):
		txt = "This is the Recipe Class"
		return txt
	
	def print_recipe(self):
		print("\033[90m")
		print(f"\nRecipe name: {self.name}")
		print(f"    Level: {self.lvl}")
		print(f"    Time: {self.time}")
		print(f"    Ingredients: {self.ingr}")
		print(f"    Type: {self.type}")
		print(f"    Description: {self.descr}\n")
		print("\033[0m")

