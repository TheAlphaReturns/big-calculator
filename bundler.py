import os

try: os.remove("calc.bundle.py")
except: pass

def writeLinesNotImport(readfile, writefile):
	for i in readfile.readlines():
		if True not in [i.startswith(j) for j in ['import', 'from']]:
			writefile.write(i)


with open('calc.bundle.py', 'a+') as bundle:
	bundle.write('#!/usr/bin/env python3\n')
	bundle.write('import sys, math, random\n')

	# import console
	with open('modules/utils/Console.py', 'r') as console:
		bundle.write(console.read())


	# import errors
	with open('modules/error/err.py', 'r') as errFile:
		writeLinesNotImport(errFile, bundle)


	# import inputs
	for inputFile in os.listdir('modules/inputs'):
		inputFile = os.path.join('modules/inputs', inputFile)
		
		if inputFile.endswith('.py') and inputFile != 'modules/inputs/__init__.py':
			with open(inputFile, 'r') as inputFileObj:
				for i in inputFileObj.readlines():					
					if True not in [i.startswith(j) for j in ['import', 'from']]:
						if 'TwoNumberInput()' in i:
							bundle.write('def tn():\n')
						else: 
							bundle.write(i)
	
	# import sequence utils
	for sqFile in os.listdir('modules/sequence'):
		sqFile = os.path.join('modules/sequence', sqFile)
		
		if sqFile.endswith('.py') and sqFile != 'modules/sequence/__init__.py':
			with open(sqFile, 'r') as sqFileObj:
				writeLinesNotImport(sqFileObj, bundle)

	# import calculators
	for calcFile in os.listdir('modules'):
		calcFile = os.path.join('modules', calcFile)
		
		if calcFile.endswith('.py') and calcFile != 'modules/__init__.py':
			with open(calcFile, 'r') as calcFileObj:
				writeLinesNotImport(calcFileObj, bundle)

	# import main.py
	with open('main.py', 'r') as main:
		writeLinesNotImport(main, bundle)