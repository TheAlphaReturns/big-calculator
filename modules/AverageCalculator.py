from modules.utils.Console import console

class AverageCalculator:
	def __init__(self, to_avg: list):
		self.to_avg = to_avg
		self.calculateInputs()
		self.output()
	
	def calculateInputs(self):
		self.answer = sum(self.to_avg)
		self.answer /= len(self.to_avg)
	
	def output(self, returnType='string'):
		if returnType == 'string': return f'Answer: {self.answer}'
		else: return self.answer