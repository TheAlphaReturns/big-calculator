from modules.Console import console

class GeometricSQ:
	def __init__(self):
		console.clear()
		console.linebreak(beg='')
		console.print(
			'	1) Calculate Common Ratio (Given a(x) and a(x-1)) \n' +
			'	2) Calculate for an index (Given a(1) and Common Ratio)'
		)
		console.linebreak(end='')

		try: self.input = int(input())
		except ValueError: raise ValueError('Not a Number')

		self.evaluateInput()

		if True in [isinstance(self.method, i) for i in [self.twoIndexes]]:
			indexyn = input('Would you like to calculate an index? [y/n] ')
			if indexyn.lower() in ['y', 'yes']: 
				index = int(input('Enter the index to find '))
				index1 = float(input('Enter the first index in the sequence (Value "x" in "a(1) = x") '))

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
				cr = float(input('Enter the common ratio '))

				self.method = self.calculateIndex(solve, index1, cr)
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
			self.index2 = self.index2
			self.index1_value = index1_value
			self.index2_value = index2_value
			self.calculateCommonRatio()
		
		def calculateCommonRatio(self):
			self.cr = (self.index2_value / self.index1_value) ** (1 / (self.index2 - self.index1))

		def output(self):
			return f'Answer: {self.cr}'
	
	class calculateIndex:
		def __init__(self, index: int, index1: float, cr: float):
			self.index = index
			self.index1 = index1
			self.cr = cr

			self.calculateIndex()
		
		def calculateIndex(self):
			self.indexValue = self.index1 * (self.cr) ** (self.index - 1)
		
		def output(self):
			return f'Answer: {self.indexValue}'