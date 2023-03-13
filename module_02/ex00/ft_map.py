# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/22 11:57:22 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/27 18:51:41 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
	Return:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	if not callable(function_to_apply):
		raise TypeError("Function is not callable.")
	if not hasattr(iterable, '__iter__'):
		raise TypeError("Argument is not iterable.")
	for i in iterable:
		yield function_to_apply(i)
