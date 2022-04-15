from modules.utils.Console import console

def SquareRootInput():
	console.print('Input a square root, or one with a factor.')
	console.print('This program relies heavily on pattern matching')
	console.print('and string modification. \n')
	
	console.print('For these reasons, please input in this format:')
	console.print('factor*sqrt(number) or')
	console.print('sqrt(number)')
	console.linebreak(end='')
	
	sqrtInput = console.input() 

	return sqrtInput