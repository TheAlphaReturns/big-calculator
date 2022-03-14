import math
from modules.Console import console

class LCM:
	def __init__(self, num1: int, num2: int):
		self.num1 = num1
		self.num2 = num2
		self.calculateLCM()

	def calculateLCM(self):
		self.lcm = math.lcm(self.num1, self.num2)
	
	def output(self):
		return f'Answer: {self.lcm}'