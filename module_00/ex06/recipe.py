# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:33:50 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:35:16 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def add(cookbook):
	ingr_list = []
	meal_type = ''
	time = 0
	name = input(">>> Enter a name:\n")
	if (name in cookbook):
		print("The recipe already exists.")
	else:
		ingr = input(">>> Enter ingredients:\n")
		while (ingr != ''):
			ingr_list.append(ingr)
			ingr = input()
		meal_type = input(">>> Enter a meal type:\n")
		time = input(">>> Enter preparation time:\n")
		recipe = {
			"ingredients": ingr_list,
			"meal": meal_type,
			"prep_time": time
			}
		cookbook[name] = recipe


def delete(cookbook):
	name = input(">>> Enter a recipe to be deleted:\n")
	try:
		cookbook.pop(name)
	except:
		print("The recipe does not exist.")


def print_recipe(cookbook, name):
	if (name in cookbook):
		print(f"\nRecipe for {name}:")
		i = cookbook[name]["ingredients"]
		m = cookbook[name]["meal"]
		p = cookbook[name]["prep_time"]
		print(f"    Ingredients list: {i}")
		print(f"    To be eaten for {m}.")
		print(f"    Takes {p} minutes of cooking.")
	else:
		print("The recipe does not exist.")


def print_all(cookbook):
	for key, value in cookbook.items():
		print_recipe(cookbook, key)
		print("\n------------------")


def print_selection():
	print("List of available option:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit\n")
	print("Please select an option:")
	selection = input(">> ")
	try:
		return (int(selection))
	except:
		return (0)


if (__name__ == "__main__"):
	sandwich = {
		"ingredients": ["ham", "bread", "cheese", "tomatoes"],
		"meal": "lunch",
		"prep_time": 10
	}
	cake = {
		"ingredients": ["flour", "sugar", "eggs"],
		"meal": "dessert",
		"prep_time": 60
	}
	salad = {
		"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
		"meal": "lunch",
		"prep_time": 15
	}
	cookbook = {
		"sandwich": sandwich,
		"cake": cake,
		"salad": salad
	}
	opt = 0
	print("Welcome to the Python Cookbook !")
	while (opt != 5):
		opt = print_selection()
		print()
		if (opt == 1):
			add(cookbook)
		elif (opt == 2):
			delete(cookbook)
		elif (opt == 3):
			name = input("Please enter a recipe name to get its details:\n>>> ")
			print_recipe(cookbook, name)
		elif (opt == 4):
			print_all(cookbook)
		elif (opt != 5):
			print("Sorry, this option does not exist.")
		print()
	print("Cookbook closed. Goodbye !")
