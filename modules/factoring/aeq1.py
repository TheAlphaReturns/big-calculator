class aeq1:
	def __init__(self, variable, sum, prod):
		res1, res2 = self.getAddMult(sum, prod)
		self.answer = self.generateOutput(variable, res1, res2)
	
	def getAddMult(self, sum, prod):
		res1 = 0
		res2 = 0
		
		factors = []
		for factor in range(-abs(prod), abs(prod + 1)):
			if factor == 0:
				continue
			if prod % factor == 0:
				factors.append(factor)

		for factor in factors:
			if factor + (prod / factor) == sum:
				res1, res2 = factor, (prod / factor)
				break
			elif factor	- (prod / factor) == sum: 
				res1, res2 = factor, -(prod / factor)
				break
			elif -factor + (prod / factor) == sum: 
				res1, res2 = -factor, (prod / factor)
				break
			elif -factor - (prod / factor) == sum: 
				res1, res2 = -factor, -(prod / factor)
				break 

		return res1, res2

	def generateOutput(self, variable, res1, res2):
		res1 = int(res1)
		res2 = int(res2)

		return f'({variable} + {res1})({variable} + {res2})'

	def output(self, returns = 'formatted'):
		if returns == 'formatted': return f'Answer: {self.answer}'
		elif returns == 'bare': return self.answer

		return None