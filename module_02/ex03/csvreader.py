# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 22:12:39 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/16 10:44:22 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():
	'''
	Import a CSV file
	'''
	def __str__(self):
		return ('CSV reader')

	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None

	# print('Error: file could not be openned.')
	def __enter__(self):
		self.file = open(self.filename, 'r')
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()
	
	def importfile(self):
		lst = []
		items = -1
		lines = self.file.read().split('\n')
		for line in lines:
			values = line.split(self.sep)
			if (items == -1):
				items = len(values)
			if (items != len(values)):
				return None
			lst.append(values)
		return lst

	def getdata(self):
		'''
		Retrieves the data/records from skip_top to skip bottom.
		Return:
			nested list (list(list, list, ...)) representing the data.
		'''
		lst = self.importfile()
		if (lst == None):
			return None
		if self.header:
			lst = lst[1:]
		lst = lst[self.skip_top:len(lst) - self.skip_bottom]
		return lst

	def getheader(self):
		'''
		Retrieves the header from csv file.
		Returns:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		'''
		lst = self.importfile()
		if (lst == None):
			return None
		if self.header == True:
			return lst[0]
		else:
			return None
