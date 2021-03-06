from random import random as rand

class Airline(object):
	"""docstring for Airline"""
	def __init__(self, iata, full_name, callsign):
		super(Airline, self).__init__()
		self.iata = iata
		self.full_name = full_name
		self.callsign = callsign
	def __str__(self):
		return self.full_name

# Source: https://en.wikipedia.org/wiki/List_of_airlines_of_the_United_States
# Mined with: https://wikitable2csv.ggor.de/
us_mainline = [ 
	Airline('AS',"Alaska Airlines", "ALASKA"),
	Airline('G4',"Allegiant Air", "ALLEGIANT"),
	Airline('AA',"American Airlines", "AMERICAN"),
	Airline('XP',"Avelo Airlines", "AVELO"),
	Airline('MX',"Breeze Airways", "MOXY"),
	Airline('DL',"Delta Air Lines", "DELTA"),
	Airline('2D',"Eastern Airlines", "EASTERN"),
	Airline('F9',"Frontier Airlines", "FRONTIER FLIGHT"),
	Airline('HA',"Hawaiian Airlines", "HAWAIIAN"),
	Airline('B6',"JetBlue", "JETBLUE"),
	Airline('WN',"Southwest Airlines", "SOUTHWEST"),
	Airline('NK',"Spirit Airlines", "SPIRIT WINGS"),
	Airline('SY',"Sun Country Airlines", "SUN COUNTRY"),
	Airline('UA',"United Airlines", "UNITED"),
]

def random():
	airline = rand() * len(us_mainline)
	airline = int(airline)
	airline = us_mainline[airline]
	return airline
