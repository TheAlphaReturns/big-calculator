from modules.utils.Console import console

class PrimeFactors:
	def __init__(self, number):
		self.number = number
		self.getPF()

	def getPF(self):
		i = 2
		self.factors = []
		
		while i * i <= self.number:
			if self.number % i:
				i += 1
			else:
				self.number //= i
				self.factors.append(i)
		
		if self.number > 1:
			self.factors.append(self.number)

	def output(self, returns='formatted'):
		if returns == 'formatted': return f'Answers: {", ".join(str(x) for x in self.factors)}'
		elif returns == 'bare': return self.factors

		return None