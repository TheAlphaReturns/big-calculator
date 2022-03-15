def TwoNumberInput():
	try: num1 = int(input('First Number: '))
	except ValueError: raise ValueError('Not a Number')
	
	try: num2 = int(input('Second Number: '))
	except ValueError: raise ValueError('Not a Number')

	return num1, num2