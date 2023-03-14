# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:33:07 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:34:45 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time, sleep


def print_progress_bar(prct):
	width = 25
	comp = round(width * prct) - 1
	ucomp = width - comp
	s_comp = '=' * comp
	s_ucomp = ' ' * ucomp
	if (prct < 1):
		pbar = '[' + s_comp + '>' + s_ucomp + ']'
	else:
		pbar = '[' + s_comp + ']'
	return pbar


def ft_progress(lst):
	start_t = time()
	total_op = len(lst)
	for i in lst:
		current_op = i + 1
		prct = current_op / total_op
		pbar = print_progress_bar(prct)
		elapsed_t = time() - start_t
		avg_t = elapsed_t / current_op
		eta = avg_t * (total_op - current_op)
		print(f"ETA: {eta:5.2f}s [{prct:5.0%}]{pbar} {current_op:5}/{total_op:5} | elapsed time {elapsed_t:5.2f}s", end = '\r')
		yield i


if (__name__ == "__main__"):
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)
