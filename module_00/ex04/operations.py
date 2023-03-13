# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 14:12:41 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 12:27:17 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def ft_operation(A, B):
	print(f"Sum:        {int(A) + int(B)}")
	print(f"Difference: {int(A) - int(B)}")
	print(f"Product:    {int(A) * int(B)}")
	if (int(B) != 0):
		print(f"Quotient:   {int(A) / int(B)}")
		print(f"Remainder:  {int(A) % int(B)}")
	else:
		print(f"Quotient:   ERROR (division by zero)")
		print(f"Remainder:  ERROR (modulo by zero)")


if (__name__ == "__main__"):
	if (len(sys.argv) == 1):
		print("Usage: python operations.py <number1> <number2>.")
	elif (len(sys.argv) == 2):
		print("AssertionError: not enough arguments")
	elif (len(sys.argv) == 3):
		if (sys.argv[1].isnumeric() and sys.argv[2].isnumeric()):
			ft_operation(sys.argv[1], sys.argv[2])
		else:
			print("AssertionError: only integers")
	else:
		print("AssertionError: too many arguments")
