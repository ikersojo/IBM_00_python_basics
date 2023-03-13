# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 13:56:23 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 12:24:50 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def text_analyzer(s='None'):
	'''
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	'''
	if (s == 'None'):
		s = input("What is the text to analyze?\n>> ")
	if (type(s) != str):
		print("AssertionError: argument is not a string")
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
		elif (c in '!.,?:;'):
			m += 1
		count += 1
	print(f"The text contains {count} character(s).")
	print(f"- {u} upper letters(s).")
	print(f"- {l} lower letter(s).")
	print(f"- {m} punctuation marks(s).")
	print(f"- {sp} space(s).")


if (__name__ == '__main__'):
	if (len(sys.argv) == 2):
		text_analyzer(sys.argv[1])
	elif (len(sys.argv) == 1):
		text_analyzer()
	else:
		print("Error! Pass a single string argument.")
