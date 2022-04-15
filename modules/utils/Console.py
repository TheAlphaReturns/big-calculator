from modules.error.err import InvalidOptionError, NaNError

class Console:
	print = print
	
	def input(self, prompt='', type='str'):
		given = input(prompt)
		
		if type not in ['str', 'int', 'float']: raise InvalidOptionError() from None

		if type == 'str': return given
		elif type == 'int':
			try: _ = int(given)
			except ValueError: raise NaNError(given) from None
			
			return int(given)
		elif type == 'float':
			try: _ = float(given)
			except ValueError: raise NaNError(given) from None

			return float(given)

	def clear(self):
		self.print('\033[H\033[J', end='')
	
	def linebreak(self, beg='\n', end='\n'):
		self.print(f'{beg}{"-"*50}{end}')
	
	endl = '\n'

console = Console()