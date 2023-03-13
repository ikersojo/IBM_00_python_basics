# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:36 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 20:35:08 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv


def ft_operation(A, B):
	if (argv[1].isnumeric() and argv[2].isnumeric()):
		print(f"Sum:        {int(A) + int(B)}")
		print(f"Difference: {int(A) - int(B)}")
		print(f"Product:    {int(A) * int(B)}")
		if (int(B) != 0):
			print(f"Quotient:   {int(A) / int(B)}")
			print(f"Remainder:  {int(A) % int(B)}")
		else:
			print(f"Quotient:   ERROR (division by zero)")
			print(f"Remainder:  ERROR (modulo by zero)")
	else:
		print("AssertionError: only integers")


if (__name__ == "__main__"):
	if (len(argv) == 1):
		print("Usage: python operations.py <number1> <number2>.")
	elif (len(argv) == 2):
		print("AssertionError: not enough arguments")
	elif (len(argv) == 3):
		ft_operation(argv[1], argv[2])
	else:
		print("AssertionError: too many arguments")
