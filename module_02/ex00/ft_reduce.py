# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 17:24:59 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:32:38 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce


def input_check(func):
	def decorator(function_to_apply, iterable):
		if not callable(function_to_apply):
			raise TypeError("TypeError:Function is not callable.")
		if not hasattr(iterable, '__iter__'):
			raise TypeError("TypeError:Argument is not iterable.")
		run = func(function_to_apply, iterable)
		return run
	return decorator


def ft_reduce(function_to_apply, iterable):
	'''
	Apply function of two arguments cumulatively.
	Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
	Return:
		A value, of same type of elements in the iterable parameter.
		None if the iterable can not be used by the function.
	'''
	res = iterable[0]
	for i in range (1, len(iterable), 2):
		res = res + function_to_apply(iterable[i], iterable[i + 1])
	return (res)
