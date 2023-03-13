# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 19:11:03 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 11:06:22 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (__name__ == "__main__"):
	if (len(sys.argv) == 3):
		try:
			s = sys.argv[1]
			n = int(sys.argv[2])
		except:
			print("ERROR")
		else:
			s = s.replace(',', '')
			s = s.replace('.', '')
			s = s.replace(';', '')
			s = s.replace(':', '')
			s = s.replace('!', '')
			s = s.replace('?', '')
			words = s.split(' ')
			res = []
			for i in words:
				if (len(i) > n):
					res.append(i)
			print(res)
	else:
		print("ERROR")
