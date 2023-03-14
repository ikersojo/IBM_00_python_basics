# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:47 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:22:42 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if (__name__ == '__main__'):
	assert len(argv) <= 2, 'more than one argument are provided'
	if (len(argv) == 2):
		assert argv[1].isnumeric(), 'argument is not an integer'
		n = int(argv[1])
		if (n == 0):
			print("I'm Zero.")
		elif (n % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
