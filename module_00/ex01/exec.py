# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:52 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:35:55 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if (__name__ == '__main__'):
	if (len(argv) >= 2):
		string = " ".join(argv[1::])
		rev = string[::-1].swapcase()
		print(rev)
