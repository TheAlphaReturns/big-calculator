import random
from modules.Console import console

class RandomNumber:
	def __init__(self, rangeStart: int, rangeEnd: int):
		self.rangeStart = rangeStart
		self.rangeEnd = rangeEnd
		self.getRandom()

	def getRandom(self):
		self.random = random.randint(self.rangeStart, self.rangeEnd)	

	def output(self):
		return f'Answer: {self.random}'