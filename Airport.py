from Airplane import Airplane
from datetime import datetime, timedelta
from CircArrayQueue import CircArrayQueue
from random import random

DAY = timedelta(1)
HOUR = timedelta(0,3600)
MINUTE = timedelta(0,60)
SECOND = timedelta(0,1)

increment = 5*MINUTE
duration = 8*HOUR
start = datetime(2021,10,16,9)

# Each plane takes 1 time increment to take off or land.

ground_likelihood = 0.3
air_likelihood = 0.2

def tf(time):
	time = time.strftime("%I:%M %p")
	if time[0] == '0':
		time = ' ' + time[1:]
	return time

end = start + duration

GroundQueue = CircArrayQueue(Airplane, 8)
AirQueue = CircArrayQueue(Airplane, 8)

time = start
# No new planes join either queue after airport is closed,
# but planes already in queues are allowed to take off or land.
while time <= end or not GroundQueue.isEmpty() or not AirQueue.isEmpty():
	events = []
	if random() < (ground_likelihood if time < end else 0):
		plane = Airplane.new()
		plane.NQ = time
		GroundQueue.enqueue(plane)
		events.append("{} joins queue on the ground".format(plane))
	if random() < (air_likelihood if time < end else 0):
		plane = Airplane.new()
		plane.NQ = time
		AirQueue.enqueue(plane)
		events.append("{} joins queue in the air".format(plane))
	if not events:
		if not AirQueue.isEmpty():
			plane = AirQueue.dequeue()
			plane.DQ = time
			event = "{} lands".format(plane)
			if plane.waitTime() > increment:
				event += ", having waited {}".format(plane.waitTime())
			events.append(event)
		elif not GroundQueue.isEmpty():
			plane = GroundQueue.dequeue()
			plane.DQ = time
			event = "{} takes off".format(plane)
			if plane.waitTime() > increment:
				event += ", having waited {}".format(plane.waitTime())
			events.append(event)
	if events:
		print tf(time)+":",
		print '; '.join(events)
	time += increment