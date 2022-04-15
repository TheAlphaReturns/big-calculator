import os

inFileName = './main.py'
outFileName = './calc.bundle.py'

try: os.remove("calc.bundle.py")
except: pass

builtInImports = []
modules = []

def getModules(string):
	if string.startswith('from'):
			string = string[5:]
	elif string.startswith('import'):
			string = string[7:]
	else:
			string = ''

	return string

def addToTree(fileName):
	with open(fileName, 'r') as file:
		for i in file.readlines():
			i = getModules(i)

			if i.startswith('modules'):
				modules.append(f'./{"/".join(i.split(" ")[0].split("."))}.py')
			elif i != '':
				builtInImports.append(i.split('\n')[0])

def removeArrayDuplicates(array):
	array.reverse()
	included = []

	for i in array:
		if i not in included:
			included.append(i)

	included.reverse()
	return included

def copyFile(inFileObj, outFileObj):
	for i in inFileObj.readlines():
		
		if i.startswith('import'): i = ''
		elif i.startswith('from') and 'import' in i: i = ''
		elif i.strip() in ['', '\n']: i = ''
		elif i == '\n': i = ''

		if i != i.split('#', 1)[0]:
			i = f'{i.split("#", 1)[0]}\n'

		if i != '':
			outFileObj.write(f'{i}')

	outFileObj.write('\n')

addToTree(inFileName)

while True:
	sizeOfModules = len(modules)

	for i in modules:
		addToTree(i)

	modules = removeArrayDuplicates(modules)
	builtInImports = removeArrayDuplicates(builtInImports)

	if len(modules) <= sizeOfModules:
		modules.reverse()
		break

with open(outFileName, 'a+') as bundle:
	for i in builtInImports:
		bundle.write(f'import {i}\n')
	
	for i in modules:
		copyFile(open(i, 'r'), bundle)
	
	copyFile(open(inFileName, 'r'), bundle)