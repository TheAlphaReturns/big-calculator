import math
from modules.utils.Console import console

from modules.error.err import InvalidOptionError

class SquareRootSimplifier:
	def __init__(self, sqrtInput: str):
		self.sqrtInput = sqrtInput
		self.getNumbers()
		self.getSquares(100)
		self.simplifyRoot()

	def getNumbers(self):
		try:
			self.factor = self.sqrtInput.split('*')[0]
			
			if self.factor.startswith('sqrt('):
				self.sqrt = self.sqrtInput.split('(')[1][:-1]
				self.factor = 1
			else:
				self.sqrt = self.sqrtInput.split('*')[1].split('(')[1][:-1]
			
			self.sqrt = float(self.sqrt)
			self.factor = float(self.factor)
		except (IndexError, ValueError): raise InvalidOptionError(self.sqrtInput) from None

	def getSquares(self, limit: float):
		self.squares = []
		for i in range(1, limit+1):
			self.squares.append(i**2)
		
		self.squares = [sqare for sqare in reversed(self.squares)]
	
	def simplifyRoot(self):
		for i in self.squares:
			if self.sqrt % i == 0:
				self.factor = (math.sqrt(i))*self.factor
				self.squareOut = self.sqrt/i
				self.squareMath = self.factor*math.sqrt(self.sqrt/i)
				return
	
	def output(self, returns = 'formatted'):
		if returns == 'formatted': return f'Answer: {int(self.factor)}*sqrt({int(self.squareOut)}) or {self.squareMath}'
		elif returns == 'bare': return f'{int(self.factor)}*sqrt({int(self.squareOut)})'

		return None