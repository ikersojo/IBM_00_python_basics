# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:43 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 20:35:08 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from string import punctuation


def text_analyzer(s='None'):
	'''
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	'''
	if (type(s) != str or s.isnumeric()):
		print("AssertionError: argument is not a string")
		return
	if (s == 'None'):
		s = input("What is the text to analyze?\n>> ")
	sp = 0
	l = 0
	u = 0
	m = 0
	count = 0
	for c in s:
		if (c == ' '):
			sp += 1
		elif (c.islower()):
			l += 1
		elif (c.isupper()):
			u += 1
		elif (c in punctuation):
			m += 1
		count += 1
	print(f"The text contains {count} character(s).")
	print(f"- {u} upper letters(s).")
	print(f"- {l} lower letter(s).")
	print(f"- {m} punctuation marks(s).")
	print(f"- {sp} space(s).")


if (__name__ == '__main__'):
	if (len(argv) == 2):
		text_analyzer(argv[1])
	elif (len(argv) == 1):
		text_analyzer()
	else:
		print("Error! Pass a single string argument.")
