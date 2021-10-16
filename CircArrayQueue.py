def Exit():
	print 'exit'
	exit()

class CircArrayQueue(object):
	"""A Queue implemented using a Circular Array"""
	def __init__(self, staticType, initialCapacity):
		super(CircArrayQueue, self).__init__()
		self.staticType = staticType # What type of element the Queue stores
		self.size = initialCapacity
		self.array = [ None for x in xrange(self.size) ] # Empty array of length initialCapacity
		self.frontIndex = 0
		self.backIndex = initialCapacity - 1
	def enqueue(self, element):
		if type(element) is not self.staticType:
			raise TypeError("This array can only accept {}s, not {}s.".format(self.staticType, type(element)))
		self.backIndex += 1
		self.backIndex %= self.size
		self.array[self.backIndex] = element
		if self.isFull():
			self.doubleSize()
	def dequeue(self):
		result = self.array[self.frontIndex % self.size]
		self.array[self.frontIndex] = None
		self.frontIndex += 1
		self.frontIndex %= self.size
		return result
	def getFront(self):
		return self.array[self.frontIndex % self.size]
	def isEmpty(self):
		return (self.backIndex + 1) % self.size == self.frontIndex
	def isFull(self):
		# print (self.backIndex + 2) % self.size, self.frontIndex
		result = (self.backIndex + 2) % self.size == self.frontIndex
		# print result
		return result
	def __iter__(self):
		i = self.frontIndex
		# print (self.backIndex + 1) % self.size
		# Exit()
		while i != (self.backIndex + 1) % self.size:
			# print i,
			yield self.array[i]
			i += 1
			i %= self.size
		# print
	def doubleSize(self):
		# print 'doubleSize'
		newArr = [ None for x in xrange(self.size * 2) ]
		i = 0
		for element in self.__iter__():
			newArr[i] = element
			i += 1
		self.array = newArr
		self.frontIndex = 0
		self.backIndex = i - 1
		self.size *= 2
	def __str__(self):
		return "<- "+", ".join([ str(x) for x in self ])+" <-"