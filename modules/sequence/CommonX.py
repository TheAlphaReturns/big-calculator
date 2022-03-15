from modules.utils.Console import console

class CommonX:
	def __init__(self, type: str, index1: int, index1_value: float, index2: int, index2_value: float):
		self.type = type
		self.index1 = index1
		self.index2 = index2
		self.index1_value = index1_value
		self.index2_value = index2_value
		
		self.calculateCommonDifference()
	
	def calculateCommonDifference(self):
		match self.type:
			case 'a': self.answer = (self.index2_value - self.index1_value) / (self.index2 - self.index1)
			case 'g': self.answer = (self.index2_value / self.index1_value) ** (1 / (self.index2 - self.index1))
		
	def output(self, returnType='string'):
		if returnType == 'string': return f'Answer: {self.answer}'
		else: return self.answer