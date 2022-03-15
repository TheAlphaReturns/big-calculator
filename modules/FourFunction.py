from modules.utils.Console import console

class FourFunction:
	def __init__(self, solve: str):
		self.solve = solve
	
		self.evalmath()
	
	def evalmath(self):
		try: self.answer = eval(self.solve)
		except SyntaxError: raise ValueError('Invalid Math')

	def output(self, returnType='string'):
		if returnType == 'string': return f'Answer: {self.answer}'
		else: return self.answer