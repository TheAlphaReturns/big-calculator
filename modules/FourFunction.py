from modules.utils.Console import console
from modules.error.err import InvalidOptionError, Error

class FourFunction:
	def __init__(self, solve: str):
		self.solve = solve
	
		self.evalmath()
	
	def evalmath(self):
		try: self.answer = eval(self.solve)
		except SyntaxError: raise InvalidOptionError(self.solve) from None

	def output(self, returns='formatted'):
		if returns == 'formatted': return f'Answer: {self.answer}'
		elif returns == 'bare': return self.answer

		return None