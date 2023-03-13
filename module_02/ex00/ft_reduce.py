# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/22 11:57:30 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/27 19:07:30 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

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
	if not callable(function_to_apply):
		raise TypeError("Function is not callable.")
	if not hasattr(iterable, '__iter__'):
		raise TypeError("Argument is not iterable.")
	res = iterable[0]
	for i in range (1, len(iterable), 2):
		res = res + function_to_apply(iterable[i], iterable[i + 1])
	return (res)
