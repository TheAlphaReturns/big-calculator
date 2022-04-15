from modules.error.err import InvalidOptionError
from modules.error.err import Error
from modules.utils.Console import console

def PythagoreanTheoremInput():
	console.print('a² + b² = c²')
	toSolveFor = console.input('Solve for: ')
	if toSolveFor not in ['a', 'b', 'c']: raise InvalidOptionError(toSolveFor)

	if toSolveFor != 'a': a = float(console.input('a = '))
	if toSolveFor != 'b': b = float(console.input('b = '))
	if toSolveFor != 'c': c = float(console.input('c = '))
	if	(
			toSolveFor not in ['b', 'c'] and 
			(b > c)
		) or (
			toSolveFor not in ['a', 'c'] and 
			(a > c)
		): raise Error('"c" is not the greatest value')

	if toSolveFor == 'a': num1 = b; num2 = c
	if toSolveFor == 'b': num1 = a; num2 = c
	if toSolveFor == 'c': num1 = a; num2 = b

	return num1, num2, toSolveFor