import sys
from modules.utils.Console import console

if sys.version_info[0] < 3: raise EnvironmentError('Needs Python 3.10+')
if sys.version_info[0] >=3 and sys.version_info[1] < 10: raise EnvironmentError('Needs Python 3.10+ (Program uses match/case)')

# Imports
from modules.ArithmeticSQ import ArithmeticSQ
from modules.AverageCalculator import AverageCalculator
from modules.FourFunction import FourFunction
from modules.GCF import GCF
from modules.GeometricSQ import GeometricSQ
from modules.LCM import LCM
from modules.PythagoreanTheorem import PythagoreanTheorem
from modules.RandomNumber import RandomNumber
from modules.SquareRootSimplifier import SquareRootSimplifier

from modules.inputs.TwoNumbers import TwoNumberInput as tn

class ChoiceMenu:
	def __init__(self):
		while True:
			self.listOptions()
			self.getChoice()
			self.evaluateChoice()
			self.postCalculation()
	
	def listOptions(self):
		console.clear()
		console.linebreak(beg='')
		console.print(
			'	1) Square Root Simplifier \n' +
			'	2) Average Calculator \n' +
			'	3) Four Function Calculator \n' +
			'	4) GCF Calculator \n' +
			'	5) LCM Calculator \n' +
			'	6) Random Number Generator \n' +
			'	7) Pythagorean Theorem Calculator \n' +
			'	8) Arithmetic Sequence \n' +
			'	9) Geometric Sequence \n' +
			'	Q) Exit'
		)
		console.linebreak(end='')

	def getChoice(self):
		self.choice = input()
		try: self.choice = int(self.choice)
		except ValueError:
			if self.choice.lower() in ['q', 'quit']:
				console.clear()
				sys.exit()
			else:
				raise ValueError('Not a number')
	
	def evaluateChoice(self):
		console.clear()
		console.linebreak(beg='')

		match self.choice:
			case 1:
				console.print('Input a square root, or one with a factor.')
				console.print('This program relies heavily on pattern matching')
				console.print('and string modification. \n')
				
				console.print('For these reasons, please input in this format:')
				console.print('factor*sqrt(number) or')
				console.print('sqrt(number)')
				console.linebreak(end='')
				
				sqrtInput = input() 
				self.method = SquareRootSimplifier(sqrtInput)
		
			case 2:
				console.print('Please enter numbers.')
				console.print('Use "stop" to stop')
				console.linebreak(end='')

				to_avg = []
				while True:
					number = input()
					if number.lower() == 'stop':
						break
					
					try: number = float(number)
					except ValueError: raise ValueError('Not a Number')

					to_avg.append(number)
				
				self.method = AverageCalculator(to_avg)

			case 3: self.method = FourFunction(input('Input math using +, -, *, /, and ** for exponents. '))
			case 4:
				num1, num2 = tn()
				self.method = GCF(num1, num2)
			
			case 5:
				num1, num2 = tn()				
				self.method = LCM(num1, num2)

			case 6:
				num1, num2 = tn()
				self.method = RandomNumber(num1, num2)

			case 7:
				console.print('a² + b² = c²')
				toSolveFor = input('Solve for: ')
				if toSolveFor not in ['a', 'b', 'c']: raise ValueError('Not a, b, or c')

				if toSolveFor != 'a': a = float(input('a = '))
				if toSolveFor != 'b': b = float(input('b = '))
				if toSolveFor != 'c': c = float(input('c = '))
				if	(
						toSolveFor not in ['b', 'c'] and 
						(b > c)
					) or (
						toSolveFor not in ['a', 'c'] and 
						(a > c)
					): raise ValueError('"c" is not the greatest value')
				
				if toSolveFor == 'a': self.method = PythagoreanTheorem(b, c, toSolveFor)
				if toSolveFor == 'b': self.method = PythagoreanTheorem(a, c, toSolveFor)
				if toSolveFor == 'c': self.method = PythagoreanTheorem(a, b, toSolveFor)

			case 8: self.method = ArithmeticSQ()
			case 9: self.method = GeometricSQ()
			case _: raise ValueError('Invalid Option')
	
	def postCalculation(self):
		console.clear()
		console.linebreak(beg='', end=console.endl)

		console.print(self.method.output())

		console.print('Press enter to continue')
		console.linebreak(end='')

		input()
		console.clear()

if __name__ == '__main__':
	ChoiceMenu()