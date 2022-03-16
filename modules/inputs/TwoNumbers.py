from modules.error.err import NaNError

def TwoNumberInput():
	try: num1 = int(input('First Number: '))
	except ValueError: raise NaNError() from None
	
	try: num2 = int(input('Second Number: '))
	except ValueError: raise NaNError() from None

	return num1, num2