# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/22 11:59:32 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/27 19:00:37 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce
from functools import reduce

if (__name__ == '__main__'):
	# Example 1:
	print("\033[33m\n- Example 1:\033[0m")
	print("\033[33m    x = [1, 2, 3, 4, 5]\033[0m")
	print("\033[33m    ft_map(lambda dum: dum + 1, x)\n\033[0m")
	print("\033[33m    Expected Output:\033[0m")
	print("\033[33m    <generator object ft_map at 0x7f708faab7b0>", end ='')
	print(" # The adress will be different\n\033[0m")

	x = [1, 2, 3, 4, 5]
	print(ft_map(lambda dum: dum + 1, x))
	print("    -------------------")
	print(map(lambda dum: dum + 1, x))


	# Example 2:
	print("\033[33m- Example 2:\033[0m")
	print("\033[33m    list(ft_map(lambda t: t + 1, x))\033[0m")
	print("\033[33m    Expected Output:\033[0m")
	print("\033[33m    [2, 3, 4, 5, 6]\033[0m")

	print(list(ft_map(lambda t: t + 1, x)))
	print("\n-------------------\n")
	print(list(map(lambda t: t + 1, x)))
	print("\n\n\033[33m- Example 3:\033[0m")
	print("\033[33m    ft_filter(lambda dum: not (dum % 2), x)\033[0m")
	print("\033[33m    Expected Output:\033[0m")
	print("\033[33m    <generator object ft_filter at 0x7f709c777d00> # The adress will be different\033[0m")

	# Example 3:
	print(ft_filter(lambda dum: not (dum % 2), x))
	print("    -------------------")
	print(filter(lambda dum: not (dum % 2), x))

	print("\n\n\033[33m    list(ft_filter(lambda dum: not (dum % 2), x))\033[0m")
	print("\033[33m    Expected Output:\033[0m")
	print("\033[33m    [2, 4]\033[0m")

	print(list(ft_filter(lambda dum: not (dum % 2), x)))
	print("    -------------------")
	print(list(filter(lambda dum: not (dum % 2), x)))


	# Example 4:
	print("\n\n\033[33m- Example 4:\033[0m")
	print("\033[33m    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']\033[0m")
	print("\033[33m    ft_reduce(lambda u, v: u + v, lst)\033[0m")
	print("\033[33m    Expected Output:\033[0m")
	print("\033[33m    Hello world\033[0m")

	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	print(ft_reduce(lambda u, v: u + v, lst))
	print("    -------------------")
	print(reduce(lambda u, v: u + v, lst))
