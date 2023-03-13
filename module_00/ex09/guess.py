# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:33:18 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 20:35:08 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint


def prompt():
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!\n")


if (__name__ == "__main__"):
	prompt()
	n = randint(1, 99)
	i = 0
	while (True):
		guess_str = input(">> ")
		if (guess_str == "exit"):
			print("Goodbye!")
			break
		i += 1
		try:
			guess = int(guess_str)
			if (guess == n):
				if (n == 42):
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				if (i == 1):
					print("Congratulations! You got it on your first try!")
				else:
					print("Congratulations, you've got it!")
					print(f"You won in {i} attempts!")
				break
			elif (guess > n):
				print("Too high!")
			else:
				print("Too low!")
		except:
			print("That's not a number.")
