import math
from modules.utils.Console import console

class GCF:
	def __init__(self, num1: int, num2: int):
		self.num1 = num1
		self.num2 = num2
		
		self.calculateGCF()

	def calculateGCF(self):
		self.answer = math.gcd(self.num1, self.num2)

	def output(self, returns='formatted'):
		if returns == 'formatted': return f'Answer: {self.answer}'
		elif returns == 'bare': return self.answer

		return None