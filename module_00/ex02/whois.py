# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:47 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 20:35:08 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if (__name__ == '__main__'):
	if (len(argv) > 2):
		print("AssertionError: more than one argument are provided")
		exit(2)
	if (len(argv) == 2):
		try:
			n = int(argv[1])
		except:
			print("AssertionError: argument is not an integer")
			exit(3)
		else:
			if (n == 0):
				print("I'm Zero.")
			elif (n % 2 == 0):
				print("I'm Even.")
			else:
				print("I'm Odd.")
