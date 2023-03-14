# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 17:25:03 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:32:58 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_check(func):
	def decorator(function_to_apply, iterable):
		if not callable(function_to_apply):
			raise TypeError("Function is not callable.")
		if not hasattr(iterable, '__iter__'):
			raise TypeError("Argument is not iterable.")
		run = func(function_to_apply, iterable)
		return run
	return decorator


@input_check
def ft_map(function_to_apply, iterable):
	"""
	Map the function to all elements of the iterable.
	Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
	Return:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	for i in iterable:
		yield function_to_apply(i)
