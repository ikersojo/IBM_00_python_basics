# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/02 19:05:54 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/02 20:00:17 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import sqrt

class TinyStatistician:
	def check_lst(func):
		def decorator(*args, **kwargs):
			lst = args[1]
			if not lst:
				return None
			return func(*args, **kwargs)
		return decorator

	@check_lst
	def mean(self, lst):
		sum = 0
		for i in lst:
			sum += i
		return ((sum* 1.0) / len(lst))

	@check_lst
	def median(self, lst):
		lst = sorted(lst)
		n = len(lst)
		if n % 2 == 0:
			index1 = n // 2 - 1
			index2 = n // 2
			return float((lst[index1] + lst[index2]) // 2)
		else:
			index = n // 2
			return float(lst[index])

	@check_lst
	def quartile(self, lst):
		lst = sorted(lst)
		q1_index = int(len(lst) * 0.25)
		q3_index = int(len(lst) * 0.75)
		if len(lst) % 4 != 0:
			q1 = lst[q1_index]
			q3 = lst[q3_index]
		else:
			q1 = (lst[q1_index] + lst[q1_index + 1]) / 2
			q3 = (lst[q3_index] + lst[q3_index + 1]) / 2
		res =[float(q1), float(q3)]
		return res

	@check_lst
	def var(self, lst):
		lst = sorted(lst)
		med = self.mean(lst)
		sum = 0
		for i in lst:
			sum += (i - med)**2
		return sum/len(lst)

	@check_lst
	def std(self, lst):
		res = sqrt(self.var(lst))
		return res


if __name__ == '__main__':
	a = [1, 42, 300, 10, 59]
	b =[]
	tstat = TinyStatistician()

	print(tstat.mean(b))
	print("      --> Expected result: None")
	print(tstat.mean(a))
	print("      --> Expected result: 82.4")
	print(tstat.median(a))
	print("      --> Expected result: 42.0")
	print(tstat.quartile(a))
	print("      --> Expected result: [10.0, 59.0]")
	print(tstat.var(a))
	print("      --> Expected result: 12279.439999999999")
	print(tstat.std(a))
	print("      --> Expected result: 110.81263465868862")
