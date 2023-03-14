# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:53:56 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:31:21 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
	def zip_evaluate(coefs, words):
		if (type(coefs) != list or type(words) != list \
			or len(coefs) != len(words)):
			return -1
		lst = list(zip(coefs, words))
		# print (lst) # uncomment to see what zip is doing
		res = 0
		for i in range(0, len(lst)):
			res += lst[i][0] * len(lst[i][1])
		return res


	def enumerate_evaluate(coefs, words):
		if (type(coefs) != list or type(words) != list \
			or len(coefs) != len(words)):
			return -1
		lst = list(enumerate(words))
		# print (lst) # uncomment to see what enumerate is doing
		res = 0
		for i in range(0, len(lst)):
			res += coefs[lst[i][0]] * len(lst[i][1])
		return res


if (__name__ == "__main__"):
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))

	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))