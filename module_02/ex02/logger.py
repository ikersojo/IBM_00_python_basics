import time
from random import randint
import os

def log(func):
	def log_decorator(*args, **kwargs):
		start_t = time.time()
		run = func(*args, **kwargs)
		ellapsed_t = time.time() - start_t
		if (ellapsed_t < 1.0):
			ellapsed = f"[ exec-time {(ellapsed_t * 1000):.3f} ms ]"
		else:
			ellapsed = f"[ exec-time {(ellapsed_t):.3f} s ]"
		user = os.environ['USER']
		task = func.__name__.replace('_', ' ').title()
		length = 20 - 1 - len(task) - 1
		for i in range(0, length):
			task += ' '
		log = (f"({user})Running: {task} {ellapsed}\n")
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
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")


if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)