# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:53:51 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:34:10 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint


def shuffle(array):
	out = []
	it = len(array)
	i = 0
	while (i < (it - 1)):
		item = randint(0, it - 1 - i)
		out.append(array[item])
		array.pop(item)
		i += 1
	out.append(array[0])
	return out


def	generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yields the substrings.'''
	if (type(text) != str):
		print("\033[31mERROR\033[0m")
		return
	valid_options = ("shuffle", "unique", "ordered")
	if (option != None and option not in valid_options):
		print("\033[31mERROR\033[0m")
		return
	array = text.split(sep)
	if (option == "shuffle"):
		array = shuffle(array)
	elif (option == "unique"):
		array = set(array)
	elif (option == "ordered"):
		array = sorted(array)
	for elem in array:
		yield elem


if (__name__ == "__main__"):
	print (generator.__doc__)
	print("-----------")
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text, sep=" "):
		print (word);
	print("-----------")
	for word in generator(text, sep=" ", option="shuffle"):
		print (word);
	print("-----------")
	for word in generator(text, sep=" ", option="ordered"):
		print (word);
	print("-----------")
	text = "Lorem Ipsum Lorem Ipsum"
	for word in generator(text, sep=" ", option="unique"):
		print (word);
	print("-----------")
	text = 1.0
	for word in generator(text, sep="."):
		print (word);