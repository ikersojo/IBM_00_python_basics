# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/10 16:05:46 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 15:21:37 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, values):
		if (type(values) == list):
			self.values = values
			if (len(values) == 1):
				self.shape = (1, len(values[0])) # row: list of a list of several floats: [[1., 2., 3.]]
				self.size = len(values[0])
			else:
				self.shape = (len(values), 1) # col: list of lists of single float: [[1.], [2.], [3.]]
				self.size = len(values)
		elif (type(values) == int):
			self.size = values
			self.values = []
			for i in range (0, self.size):
				self.values.append([float(i)])
			self.shape = (self.size, 1)
		elif (type(values) == tuple):
			if (values[0] >= values[1]):
				print ("\033[31mError: Range not in ascending order.\033[0m")
			else:
				self.size = values[1] - values[0]
				self.shape = (self.size, 1)
				self.values = []
				for i in range (values[0], values[1]):
					self.values.append([float(i)])
		else:
			print ("\033[31mError: arguments not valid.\033[0m")


	def __str__(self):
		return f"{self.values}"


	def dot(self, other):
		res = 0
		if (self.shape == other.shape):
			if (len(self.values) == 1):
				for i in range(0, self.size):
					res += self.values[0][i] * other.values[0][i]
			else:
				for i in range(0, self.size):
					res += self.values[i][0] * other.values[i][0]
			return res
		else:
			print("\033[31mError: Vector not of the same shape.\033[0m")


	def T(self):
		res = []
		if (len(self.values) == 1):
			for val in self.values[0]:
				res.append([val])
		else:
			for val in self.values:
				res.append(val[0])
			res = [res]
		return Vector(res)


	def	__add__(self, other):
		try:
			if (self.shape == other.shape):
				res = []
				if (len(self.values) == 1):
					for i in range (0, self.size):
						res.append([self.values[0][i] + other.values[0][i]])
					res = Vector(res).T()
				else:
					for i in range (0, self.size):
						res.append([self.values[i][0] + other.values[i][0]])
					res = Vector(res)
				return res
			else:
				print("\033[31mError: Vector not of the same shape.\033[0m")
		except:
			print("\033[31mError: Addition of a Vector to a Vector is not defined here.\033[0m")


	def	__radd__(self, other):
		print("\033[31mError: Addition of a scalar to a Vector is not defined here.\033[0m")


	def	__sub__(self, other):
		try:
			if (self.shape == other.shape):
				res = []
				if (len(self.values) == 1):
					for i in range (0, self.size):
						res.append([self.values[0][i] - other.values[0][i]])
					res = Vector(res).T()
				else:
					for i in range (0, self.size):
						res.append([self.values[i][0] - other.values[i][0]])
					res = Vector(res)
				return res
			else:
				print("\033[31mError: Vector not of the same shape.\033[0m")
		except:
			print("\033[31mError: Substraction of a Vector by a Vector is not defined here.\033[0m")


	def	__rsub__(self, other):
		print("\033[31mError: Substraction of a scalar by a Vector is not defined here.\033[0m")


	def	__mul__(self, other):
		if (type(other) == int or type(other) == float):
			res = []
			if (len(self.values) == 1):
				for i in range (0, self.size):
					res.append([self.values[0][i] * other])
				res = Vector(res).T()
			else:
				for i in range (0, self.size):
					res.append([self.values[i][0] * other])
				res = Vector(res)
			return res
		else:
			print("\033[31mError: Multiplication of a Vector to a Vector is not defined here.\033[0m")


	def	__rmul__(self, other):
		print("\033[31mError: Multiplication of a scalar to a Vector is not defined here.\033[0m")


	def	__truediv__(self, other):
		if (type(other) == int or type(other) == float):
			res = []
			if (len(self.values) == 1):
				for i in range (0, self.size):
					res.append([self.values[0][i] / other])
				res = Vector(res).T()
			else:
				for i in range (0, self.size):
					res.append([self.values[i][0] / other])
				res = Vector(res)
			return res
		else:
			print("\033[31mError: Division of a Vector by a Vector is not defined here.\033[0m")


	def	__rtruediv__(self, other):
		print("\033[31mError: Division of a scalar by a Vector is not defined here.\033[0m")


	def __repr__(self) -> str:
		return f"{self.values}"
