# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 22:13:59 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/01 23:34:06 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader
import sys

if __name__ == "__main__":
	# filename = sys.argv[1]
	filename = './module02/ex03/good.csv'
	print (f'openning {filename}...')
	with CsvReader(filename) as file:
		if file == None:
			print("File is corrupted")
		else:
			data = file.getdata()
			print(data)
			header = file.getheader()
			print(header)
