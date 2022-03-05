import random
import sys
import math

if sys.version_info[0] < 3: raise EnvironmentError('Needs Python 3.10+')
if sys.version_info[0] >=3 and sys.version_info[1] < 10: raise EnvironmentError('Needs Python 3.10+ (Program uses match/case)')

import math

def linebr(beg='\n', end='\n'):
	return beg + '-'*50 + end

def lineclr():
	return '\033[H\033[J'

endl = '\n'

class SquareRootSimplifier:
	def __init__(self, sqrtInput: str):
		self.sqrtInput = sqrtInput
		self.getNumbers()
		self.getSquares(100)
		self.simplifyRoot()

	def getNumbers(self):
		self.factor = self.sqrtInput.split('*')[0]
		
		if self.factor.startswith('sqrt('):
			self.sqrt = self.sqrtInput.split('(')[1][:-1]
			self.factor = 1
		else:
			self.sqrt = self.sqrtInput.split('*')[1].split('(')[1][:-1]
		
		self.sqrt = float(self.sqrt)
		self.factor = float(self.factor)

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
	
	def output(self):
		return f'Answer: {int(self.factor)}*sqrt({int(self.squareOut)}) or {self.squareMath}'

class AverageCalculator:
	def __init__(self, to_avg: list):
		self.to_avg = to_avg
		self.calculateInputs()
		self.output()
	
	def calculateInputs(self):
		self.total = 0
		for i in self.to_avg:
			self.total += i
		
		self.total /= len(self.to_avg)
	
	def output(self):
		return f'Answer: {self.total}'

class FourFunctionCalculator:
	def __init__(self, math: str):
		self.math = math
	
		self.evalmath()
	
	def evalmath(self):
		try: self.answer = eval(self.math)
		except: raise ValueError('Invalid Math')

	
	def output(self):
		return f'Answer: {self.answer}'

class GCFCalculator:
	def __init__(self, num1: float, num2: float):
		self.num1 = num1
		self.num2 = num2
		
		self.calculateGCF()

	def calculateGCF(self):
		self.answer = math.gcd(self.num1, self.num2)

	def output(self):
		return f'Answer: {self.answer}'

class LCMCalculator:
	def __init__(self, num1: float, num2: float):
		self.num1 = num1
		self.num2 = num2
		self.calculateLCM()

	def calculateLCM(self):
		self.lcm = math.lcm(self.num1, self.num2)
	
	def output(self):
		return f'Answer: {self.lcm}'

class RandomNumberGenerator:
	def __init__(self, rangeStart: float, rangeEnd: float):
		self.rangeStart = rangeStart
		self.rangeEnd = rangeEnd
		self.getRandom()

	def getRandom(self):
		self.random = random.randint(self.rangeStart, self.rangeEnd)	

	def output(self):
		return f'Answer: {self.random}'

class PythagoreanTheoremCalculator:
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

		if self.toSolveFor == 'a': 
			self.infoOut = f'b² = {self.b**2} \n'
			self.infoOut += f'c² = {self.c**2} \n'
			self.infoOut += f'c² - b² = {self.c**2-self.b**2}'

		if self.toSolveFor == 'b': 
			self.infoOut = f'a² = {self.a**2} \n'
			self.infoOut += f'c² = {self.c**2} \n'
			self.infoOut += f'c² - a² = {self.c**2-self.a**2}'
		
		if self.toSolveFor == 'c': 
			self.infoOut = f'a² = {self.a**2} \n'
			self.infoOut += f'b² = {self.b**2} \n'
			self.infoOut += f'a² + b² = {self.a**2+self.b**2}'

	def output(self):
		return f'{self.infoOut}{endl}{linebr()}{endl}Answer: {self.ans}'

class ArithmeticSequenceUtils:
	def __init__(self):
		print(lineclr(), end='')
		print(linebr(beg=''))
		print(
			'	1) Calculate Common Difference (Given one index and its value) \n' +
			'	2) Calculate Common Difference (Given two indexes and their values) \n' +
			'	3) Calculate for an index (Given a₁ and Common Difference)'
		)
		print(linebr(end=''))

		try: self.input = float(input())
		except ValueError: raise ValueError('Not a Number')

		self.evaluateInput()

		if True in [isinstance(self.method, i) for i in [self.oneIndex, self.twoIndexes]]:
			indexyn = input('Would you like to calculate an index? [y/n] ')
			if indexyn.lower() in ['y', 'yes']: 
				index = input('Enter the index to solve for (Value "n" in "a(n) = x") ')
				index1 = input('Enter the first index in the sequence (Value "x" in "a(1) = x") ')

				self.method2 = self.calculateIndex(index, index1, float(self.method.output()[8:]))
		
		self.generateOutput()
	
	def evaluateInput(self):
		print(lineclr())
		print(linebr(beg=''))
		
		match self.input:
			case 1:
				index = float(input('Enter the index (Value "n" in "a(n) = x") '))
				index_value = float(input(f'Enter the value of the index (Value "x" in "a({index}) = x") '))

				self.method = self.oneIndex(index, index_value)
			case 2:
				index1 = float(input('Enter the first index (Value "n" in "a(n) = x") '))
				index1_value = float(input(f'Enter the value of the first index (Value "x" in "a({index1}) = x") '))

				index2 = float(input('Enter the second index (Value "n" in "a(n) = x") '))
				index2_value = float(input(f'Enter the value of the second index (Value "x" in "a({index2}) = x") '))

				self.method = self.twoIndexes(index1, index1_value, index2, index2_value)
			case 3:
				index = float(input('Enter the index to solve for (Value "n" in "a(n) = x") '))
				index1 = float(input('Enter the first index in the sequence (Value "x" in "a(1) = x") '))
				cd = input('Enter the common difference (Value "d" in "a(n) = a(1) + d(n-1)") ')

				self.method = self.calculateIndex(index, index1, cd)
			case _: raise ValueError('Invalid Input')

	def generateOutput(self):
		self.out = ''
		self.out += self.method.output()

		try: self.method2
		except NameError: self.method2 = '_dummy'
		if isinstance(self.method2, self.calculateIndex):
			self.out += f'{endl}a({self.method2.index}) = {self.method2.output()[8:]}'
	
	def output(self):
		return self.out
	class oneIndex:
		def __init__(self, index: float, index_value: float):
			self.index = index
			self.index_value = index_value

			self.calculateCommonDifference()
		
		def calculateCommonDifference(self):
			self.cd = self.index_value / self.index
		
		def output(self):
			return f'Answer: {self.cd}'
	
	class twoIndexes:
		def __init__(self, index1: float, index2: float, index1_value: float, index2_value: float):
			self.index1 = index1
			self.index2 = index2
			self.index1_value = index1_value
			self.index2_value = index2_value
			self.calculateCommonDifference()
		
		def calculateCommonDifference(self):
			self.cd = (self.index2_value - self.index1_value) / (self.index2 - self.index1)

		def output(self):
			return f'Answer: {self.cd}'
	
	class calculateIndex:
		def __init__(self, index: float, index1: float, cd: float):
			self.index = float(index)
			self.index1 = float(index1)
			self.cd = float(cd)

			self.calculateIndex()
		
		def calculateIndex(self):
			self.indexValue = self.index1 + (self.index - 1) * self.cd
		
		def output(self):
			return f'Answer: {self.indexValue}'

class ChoiceMenu:
	def __init__(self):
		while True:
			self.listOptions()
			self.getChoice()
			self.evaluateChoice()
			self.postCalculation()
	
	def listOptions(self):
		print(lineclr(), end='')
		print(linebr(beg=''))
		print(
			'	1) Square Root Simplifier \n' +
			'	2) Average Calculator \n' +
			'	3) Four Function Calculator \n' +
			'	4) GCF Calculator \n' +
			'	5) LCM Calculator \n' +
			'	6) Random Number Generator \n' +
			'	7) Pythagorean Theorem Calculator \n' +
			'	8) Arithmetic Sequence \n' +
			'	9) Exit'
		)
		print(linebr(end=''))

	def getChoice(self):
		self.choice = input()
		try: self.choice = float(self.choice)
		except: raise ValueError('Not a number')
	
	def evaluateChoice(self):
		print(lineclr(), end='')
		if self.choice != 9: print(linebr(beg=''))

		match self.choice:
			case 1:
				print('Input a square root, or one with a factor.')
				print('This program relies heavily on pattern matching')
				print('and string modification. \n')
				
				print('For these reasons, please input in this format:')
				print('factor*sqrt(number) or')
				print('sqrt(number)')
				print(linebr(end=''))
				
				sqrtInput = input() 
				self.method = SquareRootSimplifier(sqrtInput)
			case 2:
				print('Please enter numbers.')
				print('Use "stop" to stop')
				print(linebr(end=''))

				to_avg = []
				while True:
					number = input()
					if number.lower() == 'stop':
						break
					
					try: number = float(number)
					except ValueError: raise ValueError('Not a Number')

					to_avg.append(number)
				
				self.method = AverageCalculator(to_avg)
			case 3:
				self.method = FourFunctionCalculator(input('Input math using +, -, *, /, and ** for exponents. '))
			case 4:
				try: num1 = float(input('First Number: '))
				except: raise ValueError('Not a Number')
				try: num2 = float(input('Second Number: '))
				except: raise ValueError('Not a Number') 
				
				self.method = GCFCalculator(num1, num2)
			case 5:
				try: num1 = float(input('First Number: '))
				except: raise ValueError('Not a Number')
				try: num2 = float(input('Second Number: '))
				except: raise ValueError('Not a Number') 
				
				self.method = LCMCalculator(num1, num2)
			case 6:
				try: self.rangeStart = float(input('First range number: '))
				except: raise ValueError('Not a Number')
				try: self.rangeEnd = float(input('Second range number: '))
				except: raise ValueError('Not a Number')

				self.method = RandomNumberGenerator(self.rangeStart, self.rangeEnd)
			case 7:
				print('a² + b² = c²')
				toSolveFor = input('Solve for: ')
				if toSolveFor not in ['a', 'b', 'c']: raise ValueError('Not a, b, or c')

				if toSolveFor != 'a': a = float(input('a = '))
				if toSolveFor != 'b': b = float(input('b = '))
				if toSolveFor != 'c': c = float(input('c = '))
				if 	(
						toSolveFor not in ['b', 'c'] and 
						(b > c)
					) or (
						toSolveFor not in ['a', 'c'] and 
						(a > c)
					): raise ValueError('"c" is not the greatest value')
				
				if toSolveFor == 'a': self.method = PythagoreanTheoremCalculator(b, c, toSolveFor)
				if toSolveFor == 'b': self.method = PythagoreanTheoremCalculator(a, c, toSolveFor)
				if toSolveFor == 'c': self.method = PythagoreanTheoremCalculator(a, b, toSolveFor)

			case 8:
				self.method = ArithmeticSequenceUtils()
			case 9: sys.exit()
			case _: raise ValueError('Invalid Option')
	
	def postCalculation(self):
		print(lineclr(), end='')
		print(linebr(beg='', end=endl))

		print(self.method.output())

		print('Press enter to continue')
		print(linebr(end=''))

		input()
		print(lineclr())

ChoiceMenu()