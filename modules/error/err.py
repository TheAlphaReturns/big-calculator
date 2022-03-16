import sys
from modules.utils.Console import console

class Error(Exception):
	def __init__(self, error=""):
		sys.tracebacklimit = 0
		console.clear()
		super().__init__(error)

class NaNError(Error):
	def __init__(self, badNumber=""):
		super().__init__(f'{badNumber} not a number')

class InvalidOptionError(Error):
	def __init__(self, badOption=""):
		super().__init__(f'invalid option {badOption}')

