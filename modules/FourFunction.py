from modules.Console import console

class FourFunction:
	def __init__(self, mathInput: str):
		self.math = mathInput
	
		self.evalmath()
	
	def evalmath(self):
		try: self.answer = eval(self.mathInput)
		except SyntaxError: raise ValueError('Invalid Math')

	
	def output(self):
		return f'Answer: {self.answer}'
