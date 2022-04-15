from modules.utils.Console import console
from modules.error.err import NaNError

def AverageCalculatorInput():
	console.print('Please enter numbers.')
	console.print('Use "stop" to stop')
	console.linebreak(end='')

	to_avg = []
	while True:
		number = console.input()
		if number.lower() == 'stop':
			break
		
		try: number = float(number)
		except ValueError: raise NaNError(number) from None

		to_avg.append(number)

	return to_avg