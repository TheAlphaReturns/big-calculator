import random
from modules.utils.Console import console

class RandomNumber:
	def __init__(self, rangeStart: int, rangeEnd: int):
		self.rangeStart = rangeStart
		self.rangeEnd = rangeEnd
		self.getRandom()

	def getRandom(self):
		self.random = random.randint(self.rangeStart, self.rangeEnd)	

	def output(self, returnType='string'):
		return self.method.output(returnType)