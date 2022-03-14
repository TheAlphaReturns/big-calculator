from modules.Console import console

class AverageCalculator:
	def __init__(self, to_avg: list):
		self.to_avg = to_avg
		self.calculateInputs()
		self.output()
	
	def calculateInputs(self):
		self.total = sum(self.to_avg)
		self.total /= len(self.to_avg)
	
	def output(self):
		return f'Answer: {self.total}'