import random
import sys
import math

if sys.version_info[0] < 3: raise EnvironmentError('Needs Python 3.10+')
if sys.version_info[0] >=3 and sys.version_info[1] < 10: raise EnvironmentError('Needs Python 3.10+ (Program uses match/case)')

import math

class SquareRootSimplifier:
	def __init__(self):
		self.getNumbers()
		self.getSquares(15)
		self.simplifyRoot()
		self.outputSimplified()

	def getNumbers(self):
		self.sqrtInput = input('Input a square root (e.g. sqrt(4) or 4*sqrt(3)): ')
		self.factor = self.sqrtInput.split('*')[0]
		
		if self.factor.startswith('sqrt('):
			self.sqrt = self.sqrtInput.split('(')[1][:-1]
			self.factor = 1
		else:
			self.sqrt = self.sqrtInput.split('*')[1].split('(')[1][:-1]
		
		self.sqrt = int(self.sqrt)
		self.factor = int(self.factor)

	def getSquares(self, limit: int):
		self.squares = []
		for i in range(1, limit+1):
			self.squares.append(i**2)
	
	def simplifyRoot(self):
		for i in self.squares:
			if self.sqrt % i == 0:
				self.factor = (math.sqrt(i))*self.factor
				self.squareOut = self.sqrt/i
				self.squareMath = self.factor*math.sqrt(self.sqrt/i)
	
	def outputSimplified(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(f'Answer: {int(self.factor)}*sqrt({int(self.squareOut)}) or {self.squareMath}')

class AverageCalculator:
	def __init__(self):
		self.getInputs()
		self.calculateInputs()
		self.output()
	
	def getInputs(self):
		print('Please enter numbers.')
		print('Use "stop" to stop')
		print('***' *7)

		self.to_avg = []
		while True:
			number = input()
			if number.lower() == 'stop':
				break
			
			try: number = float(number)
			except ValueError: raise ValueError('Not a Number')

			self.to_avg.append(number)
	
	def calculateInputs(self):
		self.total = 0
		for i in self.to_avg:
			self.total += i
		
		self.total /= len(self.to_avg)
	
	def output(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(f'Answer: {self.total}')

class FourFunctionCalculator:
	def __init__(self):
		self.math = input('Input math using +-/* ')
	
		self.evalmath()
		self.outputMath()
	
	def evalmath(self):
		try: self.output = eval(self.math)
		except: raise ValueError('Invalid Math')

	
	def outputMath(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(f'Answer: {self.output}')

class GCFCalculator:
	def __init__(self):
		self.getInputs()
		self.calculateInputs()
		self.outputGCF()
	
	def getInputs(self):
		try: self.num1 = int(input('First Number: '))
		except: raise ValueError('Not a Number')
		
		try: self.num2 = int(input('Second Number: '))
		except: raise ValueError('Not a Number')

	def calculateInputs(self):
		self.output = math.gcd(self.num1, self.num2)

	def outputGCF(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(f'Answer: {self.output}')

class LCMCalculator:
	def __init__(self):
		self.getNumbers()
		self.calculateLCM()
		self.outputLCM()
	
	def getNumbers(self):
		try: self.num1 = int(input('First Number: '))
		except ValueError: raise ValueError('Not a number')

		try: self.num2 = int(input('Second Number: ')) 
		except ValueError: raise ValueError('Not a number')

	def calculateLCM(self):
		self.lcm = math.lcm(self.num1, self.num2)

	def outputLCM(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(f'Answer: {self.lcm}')

class RandomNumberGenerator:
	def __init__(self):
		self.getRange()
		self.getRandom()
		self.outputRandom()

	def getRange(self):
		try: self.rangeStart = int(input('First range number: '))
		except: raise ValueError('Not a Number')
		
		try: self.rangeEnd = int(input('Second range number: '))
		except: raise ValueError('Not a Number')

	def getRandom(self):
		self.random = random.randint(self.rangeStart, self.rangeEnd)	

	def outputRandom(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(f'Answer: {self.random}')

class PythagoreanTheoremCalculator:
	def __init__(self):
		self.getABC()
		self.calculateABC()
		self.output()
	
	def getABC(self):
		print('a² + b² = c²')
		self.toSolveFor = input('Solve for: ')
		if self.toSolveFor not in ['a', 'b', 'c']: raise ValueError('Not a, b, or c')

		if self.toSolveFor != 'a': self.a = int(input('a = '))
		if self.toSolveFor != 'b': self.b = int(input('b = '))
		if self.toSolveFor != 'c': self.c = int(input('c = '))
		if (
				self.toSolveFor not in ['b', 'c'] and 
				(self.b > self.c)
			) or (
				self.toSolveFor not in ['a', 'c'] and 
				(self.a > self.c)
			): raise ValueError('"c" is not the greatest value')
	
	def calculateABC(self):
		if self.toSolveFor == 'a': self.ans = math.sqrt(self.c**2-self.b**2)
		if self.toSolveFor == 'b': self.ans = math.sqrt(self.c**2-self.a**2)
		if self.toSolveFor == 'c': self.ans = math.sqrt(self.a**2+self.b**2)

		if self.toSolveFor == 'a': self.infoOut = f'b² = {self.b**2} \nc² = {self.c**2} \nc² - b² = {self.c**2-self.b**2}'
		if self.toSolveFor == 'b': self.infoOut = f'a² = {self.a**2} \nc² = {self.c**2} \nc² - a² = {self.c**2-self.a**2}'
		if self.toSolveFor == 'c': self.infoOut = f'a² = {self.a**2} \nb² = {self.b**2} \na² + b² = {self.a**2+self.b**2}'

	def output(self):
		print('\033[H\033[J', end='')
		print('***' *7)
		print(self.infoOut)
		print('***' *7)
		print(f'Answer: {self.ans}')


class ChoiceMenu:
	def __init__(self):
		while True:
			self.listOptions()
			self.getChoice()
			self.evaluateChoice()
			self.postCalculation()
	
	def listOptions(self):
		print('\033[H\033[J', end='')
		print('***' *7 + '\n')
		print(
			'	1) Square Root Simplifier \n' +
			'	2) Average Calculator \n' +
			'	3) Four Function Calculator \n' +
			'	4) GCF Calculator \n' +
			'	5) LCM Calculator \n' +
			'	6) Random Number Generator \n' +
			'	7) Pythagorean Theorem Calculator \n' +
			'	8) Exit \n'
		)
		print('***' *7)

	def getChoice(self):
		self.choice = input()
		try: self.choice = int(self.choice)
		except: raise ValueError('Not a number')
	
	def evaluateChoice(self):
		print('\033[H\033[J', end='')
		if self.choice != 8: print('***' *7)

		match self.choice:
			case 1: SquareRootSimplifier()
			case 2: AverageCalculator()
			case 3: FourFunctionCalculator()
			case 4: GCFCalculator()
			case 5: LCMCalculator()
			case 6: RandomNumberGenerator()
			case 7: PythagoreanTheoremCalculator()
			case 8: sys.exit()
			case _: raise ValueError('Invalid Option')
	
	def postCalculation(self):
		print('Press enter to continue')
		print('***' *7)
		input()
		print('\033[H\033[J', end='')

ChoiceMenu()