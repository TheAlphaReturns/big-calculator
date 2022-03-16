from modules.utils.Console import console
from modules.error.err import NaNError

class SQInput:
	def choice():
		console.clear()
		console.linebreak(beg='')
		console.print(
			'	1) Calculate Common Difference/Common Ratio \n' +
			'	2) Calculate for an index '
		)
		console.linebreak(end='')

		try: option = int(input())
		except ValueError: raise NaNError() from None

		return option

	def commonx():
		index1 = int(input('Enter the first index of which you know the value: '))
		index1_value = float(input(f'Enter the value of index {index1}: '))
		
		console.print()
		
		index2 = int(input('Enter the second index for which you know the value: '))
		index2_value = float(input(f'Enter the value of index {index2}: '))

		return index1, index1_value, index2, index2_value

	def index():
		solve = int(input('Enter the index to solve for: '))
		index1 = float(input('Enter the first index in the sequence: '))
		cx = float(input('Enter the common difference/common ratio: '))

		return solve, index1, cx