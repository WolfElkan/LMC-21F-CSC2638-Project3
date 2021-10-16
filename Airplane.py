import Airline
from random import random as rand
nato_nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINER"]

class Airplane(object):
	"""docstring for Airplane"""
	def __init__(self, airline, flight):
		super(Airplane, self).__init__()
		self.airline = airline
		self.flight = flight
		self.NQ = None
		self.DQ = None
	def __str__(self):
		return "{}-{:04}".format(self.airline.iata, self.flight)
	def callsign(self):
		return ' '.join([self.airline.callsign]+[ nato_nums[int(n)] for n in str(self.flight) ])
	def waitTime(self):
		return self.DQ - self.NQ
	@staticmethod
	def new():
		airplane = Airplane(
			Airline.random(), 
			int((rand()*99 + 1) ** 2), # Weighted toward lower numbers
		)
		return airplane