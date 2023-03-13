# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 13:44:35 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 12:23:32 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (__name__ == '__main__'):
	if (len(sys.argv) > 2):
		print("AssertionError: more than one argument are provided")
		exit(2)
	if (len(sys.argv) == 2):
		try:
			n = int(sys.argv[1])
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
