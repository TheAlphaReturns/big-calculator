from modules.Console import console

class ArithmeticSQ:
	def __init__(self):
		console.clear()
		console.linebreak(beg='')
		console.print(
			'	1) Calculate Common Difference (Given two indexes and their values) \n' +
			'	2) Calculate for an index (Given a(1) and Common Difference)'
		)
		console.linebreak(end='')

		try: self.input = int(input())
		except ValueError: raise ValueError('Not a Number')

		self.evaluateInput()

		if True in [isinstance(self.method, i) for i in [self.twoIndexes]]:
			indexyn = input('Would you like to calculate an index? [y/n] ')
			if indexyn.lower() in ['y', 'yes']: 
				index = input('Enter the index to solve for (Value "n" in "a(n) = x") ')
				index1 = input('Enter the first index in the sequence (Value "x" in "a(1) = x") ')

				self.method2 = self.calculateIndex(index, index1, float(self.method.output()[8:]))
		
		self.generateOutput()
	
	def evaluateInput(self):
		console.clear()
		console.linebreak(beg='')

		match self.input:
			case 1:
				index1 = int(input('Enter the first index of which you know the value '))
				index1_value = float(input(f'Enter the value of index {index1} '))

				index2 = int(input('Enter the second index for which you know the value'))
				index2_value = float(input(f'Enter the value of index {index2}'))

				self.method = self.twoIndexes(index1, index1_value, index2_value)
			case 2:
				solve = int(input('Enter the index to solve for '))
				index1 = float(input('Enter the first index in the sequence '))
				cd = float(input('Enter the common difference '))

				self.method = self.calculateIndex(solve, index1, cd)
			case _: raise ValueError('Invalid Input')

	def generateOutput(self):
		self.out = ''
		self.out += self.method.output()

		try: self.method2
		except AttributeError: self.method2 = '_dummy'
		if isinstance(self.method2, self.calculateIndex):
			self.out += f'{console.endl}a({self.method2.index}) = {self.method2.output()[8:]}'
	
	def output(self):
		return self.out
	
	class twoIndexes:
		def __init__(self, index1: int, index1_value: float, index2: int, index2_value: float):
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
