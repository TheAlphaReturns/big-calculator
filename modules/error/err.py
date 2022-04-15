import sys

class Error(Exception):
	def __init__(self, error=""):
		sys.tracebacklimit = 0
		print('\033[H\033[J', end='') # cant import Console bc circle dep
		super().__init__(error)

class NaNError(Error):
	def __init__(self, badNumber=""):
		super().__init__(f'{badNumber} not a number')

class InvalidOptionError(Error):
	def __init__(self, badOption=""):
		super().__init__(f'invalid option {badOption}')