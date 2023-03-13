# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/10 16:05:32 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 12:43:13 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

if(__name__ == "__main__"):
	print("\033[33mCreating book and recipes... \033[0m", end = '')
	cookbook = Book("cookbook")
	test1 = Recipe("test1", 5, 60, ["asd", "zxc", "wer"], "lunch", "hi!")
	test2 = Recipe("test2", 1, 60, ["asd", "zxc", "wer"], "lunch")
	test3 = Recipe("test3", 2, 60, ["asd", "zxc", "wer"], "dessert")
	test4 = Recipe("test4", 3, 60, ["asd", "zxc", "wer"], "starter")
	print("\033[32mOK\n\033[0m")
	print("\033[33mAdding recipes to cookbook... \033[0m", end = '')
	cookbook.add_recipe(test1)
	cookbook.add_recipe(test2)
	cookbook.add_recipe(test3)
	cookbook.add_recipe(test4)
	print("\033[32mOK\n\033[0m")
	print("\033[33mPrinting by name... \033[0m")
	cookbook.get_recipe_by_name("test1").print_recipe()
	cookbook.get_recipe_by_name("test3").print_recipe()
	cookbook.get_recipe_by_name("test4").print_recipe()
	print("\033[32mOK\n\033[0m")
	print("\033[33mPrinting by type... \033[0m")
	for i in cookbook.get_recipes_by_types("lunch"):
		i.print_recipe()
	print("\033[32mOK\n\033[0m")
