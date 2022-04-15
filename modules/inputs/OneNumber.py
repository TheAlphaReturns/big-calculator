from modules.error.err import NaNError

def OneNumberInput():
	try: num1 = int(input('Number: '))
	except ValueError: raise NaNError() from None

	return num1