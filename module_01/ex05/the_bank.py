# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:54:18 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:33:28 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")


	def transfer(self, amount):
		self.value += amount


	def	check_validity(self):
		if (not isinstance(self, Account)):
			return False
		if (not(hasattr(self, 'name') and type(self.__dict__['name']) == str)):
			return False
		if (not(hasattr(self, 'id') and type(self.__dict__['id']) == int)):
			return False
		if (not hasattr(self, 'value')):
			return False
		if (not(type(self.__dict__['value']) == int or type(self.__dict__['value']) == float)):
			return False
		req = 0
		count = 0
		for key in self.__dict__.keys():
			count += 1
			if key.startswith('b'):
				return False
			if key.startswith('zip'):
				req += 1
			if key.startswith('addr'):
				req += 1
		if (req != 2):
			return False
		if (count % 2) != 0:
			return False
		print(f"{self.name} is a valid account object.")
		return True


class Bank():
	'''The bank'''
	def __init__(self):
		self.accounts = []


	def __str__(self):
		str = "Bank accounts:\n"
		for ac in self.accounts:
			if hasattr(ac, 'name'):
				str += " -" + ac.name + "\n"
		return str


	def add(self, new_account=None):
		'''
		Add new_account in the Bank
		@ac: Account() new account to append
		@return True if success, False if an error occured
		'''
		if (new_account == None):
			print("Please include a valid Account object as argument.")
			return False
		if (not isinstance(new_account, Account)):
			print(f"{new_account.name} is not a valid Account object.")
			return False
		for ac in self.accounts:
			if (ac.name == new_account):
				print(f"{new_account.name} already exists.")
				return False
		self.accounts.append(new_account)
		print(f"{new_account.name} added to the bank.")
		return True


	def transfer(self, origin, dest, amount):
		'''
		Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		'''
		if (amount < 0):
			return False
		for ac in self.accounts:
			if (ac.name == origin):
				origin_ac = ac
			if (ac.name == dest):
				dest_ac = ac
		if (not(origin_ac.check_validity() and dest_ac.check_validity())):
			return False
		if (origin_ac.name != dest_ac.name and origin_ac.value >= amount):
			origin_ac.transfer(-1 * amount)
			dest_ac.transfer(amount)
			print(f"{amount} transferred from {origin_ac.name} to {dest_ac.name}.")
		return True


	def fix_account(self, name): 
		'''
		Fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		'''
		if (type(name) != str):
			return False
		for ac in self.accounts:
			if (ac.name == name):
				target_ac = ac
				break
		if (target_ac.name != name):
			return False
		if (not hasattr(target_ac, 'id') or type(ac.__dict__['id']) != int):
			target_ac.__setattr__('id', Account.ID_COUNT)
			Account.ID_COUNT += 1
		# if (not hasattr(target_ac, 'name') or type(ac.__dict__['name']) != str):
		# 	target_ac.__setattr__('name', 'user id: ' + str(target_ac.ID_COUNT))
		if (not hasattr(target_ac, 'value')):
			target_ac.__setattr__('value', 0)
		if (not(type(target_ac.__dict__['value']) == int or type(target_ac.__dict__['value']) == float)):
			target_ac.__setattr__('value', 0)
		zip = 0
		addr = 0
		for key in target_ac.__dict__.keys():
			if key.startswith('b'):
				target_ac.__delattr__(key)
			if key.startswith('zip'):
				zip = 1
			if key.startswith('addr'):
				addr = 1
		if (zip == 0):
			target_ac.__setattr__('zip', 0)
		if (addr == 0):
			target_ac.__setattr__('addr', 'no address defined')
		if (len(target_ac.__dict__.keys()) % 2 != 0):
			if (hasattr(target_ac, 'dummy')):
				target_ac.__delattr__('dummy')
			else:
				target_ac.__setattr__('dummy', 'dummy')
		print(f"{target_ac.name} fixed.")
		return True

