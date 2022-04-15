from modules.utils.Console import console

class CalculateIndex:
	def __init__(self, type: str, index: float, index1: float, cx: float):
		self.type = type
		self.index = index
		self.index1 = index1
		self.cx = cx

		self.calculateIndex()
	
	def calculateIndex(self):
		match self.type:
			case 'a': self.answer = self.index1 + (self.index - 1) * self.cx
			case 'g': self.answer = self.index1 * (self.cx ** (self.index - 1))
		
	def output(self, returns='formatted'):
		if returns == 'formatted': return f'Answer: {self.answer}'
		elif returns == 'bare': return self.answer

		return None