from modules.utils.Console import console
from modules.GCF import GCF

class SimplifyFraction:
	def __init__(self, num, denom):
		self.num, self.denom = self.simplify(num, denom)

	def simplify(self, num, denom):
		factor = GCF(num, denom).output('bare')
		return num / factor, denom / factor

	def output(self, returns='formatted'):
		if returns == 'formatted': return f'Answer: {self.num}/{self.denom}'
		elif returns == 'bare': return self.num, self.denom

		return None