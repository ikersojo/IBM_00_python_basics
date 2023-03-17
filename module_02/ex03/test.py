# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 22:13:59 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/17 09:14:36 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader

def test(fileame):
	print (f'openning {filename}...')
	with CsvReader(filename) as file:
		if file == None:
			print("File is corrupted")
		else:
			data = file.getdata()
			print('Data:')
			print(data)
			header = file.getheader()
			print ('Header:')
			print(header)

if __name__ == "__main__":
	filename = 'good.csv'
	test(filename)
	filename = 'bad1.csv'
	test(filename)
	filename = 'bad2.csv'
	test(filename)
