from Airplane import Airplane
from datetime import datetime, timedelta
from CircArrayQueue import CircArrayQueue

DAY = timedelta(1)
HOUR = timedelta(0,3600)
MINUTE = timedelta(0,60)
SECOND = timedelta(0,1)

increment = 1*MINUTE
duration = 8*HOUR
start = datetime(2021,10,16,9)

ground_likelihood = 0.2
air_likelihood = 0.05

def tf(time):
	time = time.strftime("%I:%M %p")
	if time[0] == '0':
		time = ' ' + time[1:]
	return time

end = start + duration

time = start
while time <= end:
	print tf(time)
	time += increment