	#! /usr/bin/env python3
# Matthew Jun
# Matt.j@csu.fullerton.edu
# @mwjun

import pickle
from locale import currency, setlocale, LC_ALL


class Player:
	"""player class that has both human and ai"""

	def __init__(self, name, bankroll = 10000):
		"""update te bank balance of the player"""
		self._pname = name
		self._pbalance = bankroll
		self._bet = 0
		self._wager = 0
		self._betlist = []
		self._bust = False
		self._stay = False
		setlocale(LC_ALL, '')

	#def _hit(self):
		
	@property
	def name(self):
		"""return player's name"""
		return self._pname
	
	def __str__(self):
		"""covert the player to a printale string"""
		return f"{self._pname} and remaining balance is {self._pbalance}"
	
	def __repr__(self):
		"""python reprsentation, represent!"""
		return f'Player(name = {self._pname}, pbalance = {self._pbalance}'
	
	@property
	def wager(self):
		"""how much player is waging"""
		return self._wager
	
	@wager.setter
	def wager(self,amount):
		"""how muh a player is betting"""
		if amount > self._pbalance:
			raise ValueError("You dont have enough money fool")
		self._wager = amount
		self._pbalance -= amount

	def get_bet(self):
		return self._betlist

	def deposit(self, amount):
		"""Deposit cash into the player's wallet"""
		self._pbalance += amount

	def withdraw(self, amount):
		"""take away frm the player's wallet"""
		if amount > self._pbalance:
			print("You dont have enough money fool, go home!")
			exit
		self._pbalance -= amount

	def track_bet(self,amount):
		return self._wager == amount
	
	def get_bet(self):
		return self._wager

	def player_stay(self):
		self._stay = True
		print("You chose to stay")
		return self._stay

	def busted(self):
		self._bust = True
		print(f'{self._pname} busted!')
		return self._bust

	def get_bal(self):
		return self._pbalance

	def dont_have_enough_msg(self):
		print("You don't have enough balance.")

	def deduction_message(self, amount):
		print(f"{self._pname}, you hve deducted {amount} from your balance.")

	def remaining_bal(self):
		print(f"{self._pname}, you now have {self._pbalance} left in your balance.\n")
	
	def is_dealer(self):
		"""Keep track if its player or bot"""
		return False
	
	def dealer_loss(self):
		return False
	
	def double_down(self):
		double_wager = self._wager *2
		return double_wager

	def deposit_winning(self,amount):
		winning = amount *2
		self._pbalance += winning

def to_file(pickle_file, players):
	"""Write players onto a file and store them, otherwise known as a pickled file"""
	#with automatically closes the file after everything is open
	#open opens a file called pickle_file and makes it in write mode, then assigns it to file_handle
	#file_handle is a variable
	with open(pickle_file, 'wb') as file_handle:
		pickle.dump(players,file_handle, pickle.HIGHEST_PROTOCOL)

def from_file(pickle_file):
	"""This unpacks the pickle file and loads the contents"""
	with open(pickle_file, 'rb') as file_handle:
		players = pickle.load(file_handle)
	return players

class Dealer(Player):
	"""The AI player"""
		
	def __init__(self, pname = "dealer", amount = 0):
		super().__init__(pname, amount)

	def is_dealer(self):
		return True
			

	
	
