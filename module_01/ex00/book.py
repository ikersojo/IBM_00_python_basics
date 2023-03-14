# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:53:01 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 16:51:35 by isojo-go         ###   ########.fr        #
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
