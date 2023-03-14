# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 22:52:30 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 23:00:50 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time, sleep
from random import randint
import os

def log(func):
	def log_decorator(*args, **kwargs):
		start_t = time()
		run = func(*args, **kwargs)
		ellapsed_t = time() - start_t
		if (ellapsed_t < 1.0):
			ellapsed = f"[ exec-time {(ellapsed_t * 1000):.3f} ms ]"
		else:
			ellapsed = f"[ exec-time {(ellapsed_t):.3f} s ]"
		user = os.environ['USER']
		task = func.__name__.replace('_', ' ').title()
		log = (f"({user})Running: {task: <19}{ellapsed}\n")
		file = open('machine.log', 'a')
		file.write(log)
		file.close
		return run
	return log_decorator

class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")


if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)