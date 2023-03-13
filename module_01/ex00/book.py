# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 22:39:57 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 12:43:06 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time
from recipe import Recipe


class Book:
	'''Book Class. Book(name)'''


	def __init__(self, name):
		self.name = name
		self.last_update = time()
		self.creation_date = time()
		self.recipe_list = {"starter": [], "lunch": [], "dessert": []}


	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name name and returns the instance"""
		for key in self.recipe_list:
			for elem in self.recipe_list[key]:
				if (name == elem.name):
					return elem
		print ("\033[31mRecipe not Found!\033[0m")
		return None


	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type"""
		for key in self.recipe_list:
			if (key == recipe_type):
				return self.recipe_list[key]


	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		self.last_update = time()
		if (self.recipe_list[recipe.type] == None):
			self.recipe_list[recipe.type] = recipe
		else:
			self.recipe_list[recipe.type].append(recipe)


if(__name__ == "__main__"):
	print("\033[33mbuilt-in test...\033[0m")
	cookbook = Book("cookbook")
	test1 = Recipe("test1", 5, 60, ["asd", "zxc", "wer"], "lunch", "hi!")
	test2 = Recipe("test2", 1, 60, ["asd", "zxc", "wer"], "lunch")
	test3 = Recipe("test3", 2, 60, ["asd", "zxc", "wer"], "dessert")
	test4 = Recipe("test4", 3, 60, ["asd", "zxc", "wer"], "starter")
	print(type(test1))
	cookbook.add_recipe(test1)
	cookbook.add_recipe(test2)
	cookbook.add_recipe(test3)
	cookbook.add_recipe(test4)
	cookbook.get_recipe_by_name("test1").print_recipe()
	cookbook.get_recipe_by_name("test3").print_recipe()
	cookbook.get_recipe_by_name("test4").print_recipe()
	for i in cookbook.get_recipes_by_types("lunch"):
		i.print_recipe()