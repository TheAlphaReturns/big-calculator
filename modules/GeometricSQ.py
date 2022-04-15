from modules.utils.Console import console

from modules.inputs.SQInput import SQInput
from modules.sequence.CalculateIndex import CalculateIndex
from modules.sequence.CommonX import CommonX
from modules.error.err import InvalidOptionError

class GeometricSQ:
	def __init__(self):
		self.input = SQInput.choice()
		
		self.evaluateInput()
	
	def evaluateInput(self):
		console.clear()
		console.linebreak(beg='')

		match self.input:
			case 1:
				index1, index1_value, index2, index2_value = SQInput.commonx()
				self.method = CommonX('g', index1, index1_value, index2, index2_value)
			
			case 2:
				solve, index1, cr = SQInput.index()
				self.method = CalculateIndex('g', solve, index1, cr)
			
			case _: raise InvalidOptionError(self.input)


	def output(self, returns = 'formatted'):
		return self.method.output(returns)