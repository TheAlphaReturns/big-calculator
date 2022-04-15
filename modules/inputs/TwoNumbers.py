from modules.error.err import NaNError

def TwoNumberInput():
	try: num1 = int(input('First Number / Numerator / Start range: '))
	except ValueError: raise NaNError() from None
	
	try: num2 = int(input('Second Number / Denominator / End range: '))
	except ValueError: raise NaNError() from None

	return num1, num2