import Airline
from random import random
nato_nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINER"]

class Airplane(object):
	"""docstring for Airplane"""
	def __init__(self, airline, flight):
		super(Airplane, self).__init__()
		self.airline = airline
		self.flight = flight
	def __str__(self):
		return "{}-{:04}".format(self.airline.iata, self.flight)
	def callsign(self):
		return ' '.join([self.airline.callsign]+[ nato_nums[int(n)] for n in str(self.flight) ])
	@staticmethod
	def new():
		return Airplane(
			Airline.random(), 
			int((random()*100) ** 2) # Weighted toward lower numbers
		)

print Airplane.new()