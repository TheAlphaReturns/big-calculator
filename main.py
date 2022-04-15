import sys

from modules.utils.Console import console
from modules.utils.choices import calculators
from modules.error.err import InvalidOptionError, NaNError

if sys.version_info[0] < 3: raise EnvironmentError('Needs Python 3.10+')
if sys.version_info[0] >=3 and sys.version_info[1] < 10: raise EnvironmentError('Needs Python 3.10+ (Program uses match/case)')



class Menu:
	def __init__(self):
		while True:
			self.listOptions()
			self.getChoice()
			self.evaluateChoice()
			self.postCalculation()
	
	def listOptions(self):
		console.clear()
		console.linebreak(beg='')

		for i in calculators:
			console.print(f'\t{i["index"]}) {i["name"]}')
		console.print('\n\tq) Quit')

		console.linebreak(end='')

	def getChoice(self):
		self.choice = console.input()
		
		try: self.choice = int(self.choice)
		except ValueError:
			if self.choice.lower() in ['q', 'quit']:
				console.clear()
				sys.exit()
			else:
				raise NaNError(self.choice) from None
	
	def evaluateChoice(self):
		console.clear()
		console.linebreak(beg='')

		self.method = None

		for i in calculators:
			if i['input'] is None:
				if i['index'] == self.choice:
					self.method = i['class']()
					break
			else:
				if i['index'] == self.choice:
					inputs = i['input']()
					isIter = None

					try: _ = iter(inputs)
					except TypeError: isIter = False
					else: isIter = True

					if isIter: self.method = i['class'](*inputs)
					else: self.method = i['class'](inputs)

					break

		if self.method is None:
			raise InvalidOptionError(self.choice) from None
	
	def postCalculation(self):
		console.clear()
		console.linebreak(beg='', end=console.endl)

		console.print(self.method.output(returns = 'formatted'))

		console.print('Press enter to continue')
		console.linebreak(end='')

		console.input()
		console.clear()

if __name__ == '__main__':
	try: Menu()
	except KeyboardInterrupt:
		console.clear()
		sys.exit()