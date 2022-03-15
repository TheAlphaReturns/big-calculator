from modules.utils.Console import console

from modules.inputs.SQInput import SQInput
from modules.sequence.CalculateIndex import CalculateIndex
from modules.sequence.CommonX import CommonX

class ArithmeticSQ:
	def __init__(self):
		self.input = SQInput.choice()
		
		self.evaluateInput()
	
	def evaluateInput(self):
		console.clear()
		console.linebreak(beg='')

		match self.input:
			case 1:
				index1, index1_value, index2, index2_value = SQInput.commonx()
				self.method = CommonX('a', index1, index1_value, index2, index2_value)
			
			case 2:
				solve, index1, cd = SQInput.index()
				self.method = CalculateIndex('a', solve, index1, cd)
			
			case _: raise ValueError('Invalid Input')

	def output(self, returnType='string'):
		return self.method.output(returnType)
