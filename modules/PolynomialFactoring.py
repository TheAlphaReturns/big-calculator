from modules.utils.Console import console
from modules.error.err import NaNError, InvalidOptionError

from modules.factoring.agt1 import agt1
from modules.factoring.aeq1 import aeq1

def clearThenLineBR():
	console.clear()
	console.linebreak(beg='')

class PolyFactor:
	def __init__(self):
		self.getInput()
		self.evaluateChoice()

	def getInput(self):
		console.clear()
		console.linebreak(beg='')
		console.print(
			'	1) Trinomials where A=1 \n' +
			'	2) Trinomails where A>1 '
		)
		console.linebreak(end='')

		try: self.choice = int(console.input())
		except ValueError: raise NaNError() from None

	def evaluateChoice(self):
		console.clear()
		console.linebreak(beg='')

		match self.choice:
			case 1:
				variable = console.input('Variable: ')

				clearThenLineBR()
				try: num1 = int(console.input(f'{variable}² + {variable}*'))
				except: raise NaNError()
			
				clearThenLineBR()
				try: num2 = int(console.input(f'{variable}² + {num1}{variable} + '))
				except: raise NaNError()

				self.method = aeq1(variable, num1, num2)

			case 2:
				variable = console.input('Variable: ')

				clearThenLineBR()
				try: num1 = int(console.input(f'{variable}²*'))
				except: raise NaNError()

				clearThenLineBR()
				try: num2 = int(console.input(f'{num1}{variable}² + {variable}*'))
				except: raise NaNError()
			
				clearThenLineBR()
				try: num3 = int(console.input(f'{num1}{variable}² + {num2}{variable} + '))
				except: raise NaNError()

				self.method = agt1(variable, num1, num2, num3)


	def output(self, returns = 'formatted'):
		return self.method.output(returns)