class Console:
	print = print

	def clear(self):
		self.print('\033[H\033[J', end='')
	
	def linebreak(self, beg='\n', end='\n'):
		self.print(f'{beg}{"-"*50}{end}')
	
	endl = '\n'

console = Console()