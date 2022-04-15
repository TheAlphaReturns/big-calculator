from modules.utils.Console import console
from modules.SimplifyFraction import SimplifyFraction
from modules.error.err import Error

class agt1:
	def __init__(self, variable, a, sum, prod):
		sum, prod = self.getSumProd(a, sum, prod)
		res1, res2 = self.getAddMult(sum, prod)
		self.answer = self.generateOutput(variable, a, res1, res2)
	
	def getSumProd(self, a, sum, prod):
		if a == 1:
			return sum, prod
		else:
			return sum, a*prod

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
			if factor + (prod / factor) == sum: res1, res2 = factor, (prod / factor)
			elif factor	- (prod / factor) == sum: res1, res2 = factor, -(prod / factor)
			elif -factor + (prod / factor) == sum: res1, res2 = -factor, (prod / factor)
			elif -factor - (prod / factor) == sum: res1, res2 = -factor, -(prod / factor) 

		return res1, res2

	def generateOutput(self, variable, a, res1, res2):
		preVar1 = ''
		preVar2 = ''

		res1 = int(res1)
		res2 = int(res2)
		a = int(a)

		if res1 % a == 0 and res2 % a != 0:
			res1 = res1 / a
			res2, preVar2 = SimplifyFraction(res2, a).output(returns='bare')
		elif res1 % a != 0 and res2 % a == 0:
			res2 = res2 / a
			res1, preVar1 = SimplifyFraction(res1, a).output(returns='bare')
		elif res1 % a != 0 and res2 % a != 0:
			res1, preVar1 = SimplifyFraction(res1, a).output(returns='bare')
			res2, preVar2 = SimplifyFraction(res2, a).output(returns='bare')
		else:
			raise Error('Oops, it looks like you forgot to take out the gcf!')

		if type(preVar1) is float: preVar1 = int(preVar1)
		if type(preVar2) is float: preVar2 = int(preVar2)
		res1 = int(res1)
		res2 = int(res2)
		a = int(a)

		return f'({preVar1}{variable} + {res1})({preVar2}{variable} + {res2})'

	def output(self, returns = 'formatted'):
		if returns == 'formatted': return f'Answer: {self.answer}'
		elif returns == 'bare': return self.answer

		return None