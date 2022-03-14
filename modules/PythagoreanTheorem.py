import math
from modules.Console import console

class PythagoreanTheorem:
	def __init__(self, var1: float, var2: float, toSolveFor: str):
		self.getABC(var1, var2, toSolveFor)
		self.calculateABC()
		self.output()
	
	def getABC(self, var1: float, var2: float, toSolveFor: str):
		self.toSolveFor = toSolveFor
		if self.toSolveFor == 'a':
			self.b = var1
			self.c = var2
		elif self.toSolveFor == 'b':
			self.a = var1
			self.c = var2
		elif self.toSolveFor == 'c':
			self.a = var1
			self.b = var2

	def calculateABC(self):
		if self.toSolveFor == 'a': self.ans = math.sqrt(self.c**2-self.b**2)
		if self.toSolveFor == 'b': self.ans = math.sqrt(self.c**2-self.a**2)
		if self.toSolveFor == 'c': self.ans = math.sqrt(self.a**2+self.b**2)

		self.infoOut = ''
		match self.toSolveFor:
			case 'a': 
				self.infoOut = f'b² = {self.b**2} \n'
				self.infoOut += f'c² = {self.c**2} \n'
				self.infoOut += f'c² - b² = {self.c**2-self.b**2}'

			case 'b': 
				self.infoOut = f'a² = {self.a**2} \n'
				self.infoOut += f'c² = {self.c**2} \n'
				self.infoOut += f'c² - a² = {self.c**2-self.a**2}'
		
			case 'c': 
				self.infoOut = f'a² = {self.a**2} \n'
				self.infoOut += f'b² = {self.b**2} \n'
				self.infoOut += f'a² + b² = {self.a**2+self.b**2}'

	def output(self):
		return f'{self.infoOut}{console.endl}{console.endl}Answer: {self.ans}'
