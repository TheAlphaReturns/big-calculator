from modules.ArithmeticSQ import ArithmeticSQ
from modules.AverageCalculator import AverageCalculator
from modules.FourFunction import FourFunction
from modules.GCF import GCF
from modules.GeometricSQ import GeometricSQ
from modules.LCM import LCM
from modules.PolynomialFactoring import PolyFactor
from modules.PrimeFactors import PrimeFactors
from modules.PythagoreanTheorem import PythagoreanTheorem
from modules.RandomNumber import RandomNumber
from modules.SimplifyFraction import SimplifyFraction
from modules.SquareRootSimplifier import SquareRootSimplifier


from modules.inputs.AverageCalculatorInput import AverageCalculatorInput
from modules.inputs.FourFunctionInput import FourFunctionInput
from modules.inputs.OneNumber import OneNumberInput
from modules.inputs.PythagoreanTheoremInput import PythagoreanTheoremInput
from modules.inputs.SquareRootInput import SquareRootInput
from modules.inputs.TwoNumbers import TwoNumberInput

calculators = [
	{
		'index': 1,
		'name': 'Arithmatic Sqeuences',
		'class': ArithmeticSQ,
		'input': None,
	},
	{
		'index': 2,
		'name': 'Average Calculator',
		'class': AverageCalculator,
		'input': AverageCalculatorInput,
	},
	{
		'index': 3,
		'name': 'Four Function Calculator',
		'class': FourFunction,
		'input': FourFunctionInput,
	},
	{
		'index': 4,
		'name': 'GCF',
		'class': GCF,
		'input': TwoNumberInput,
	},
	{
		'index': 5,
		'name': 'Geometric Sqeuences',
		'class': GeometricSQ,
		'input': None,
	},
	{
		'index': 6,
		'name': 'LCM',
		'class': LCM,
		'input': TwoNumberInput,
	},
	{
		'index': 7,
		'name': 'Polynomial Factoring',
		'class': PolyFactor,
		'input': None,
	},
	{
		'index': 8,
		'name': 'Prime Factors',
		'class': PrimeFactors,
		'input': OneNumberInput,
	},
	{
		'index': 9,
		'name': 'Pythagorean Theorem',
		'class': PythagoreanTheorem,
		'input': PythagoreanTheoremInput,
	},
	{
		'index': 10,
		'name': 'Random Number Generator',
		'class': RandomNumber,
		'input': TwoNumberInput,
	},
	{
		'index': 11,
		'name': 'Simplify Fraction',
		'class': SimplifyFraction,
		'input': TwoNumberInput
	},
	{
		'index': 12,
		'name': 'Square Root Simplifier',
		'class': SquareRootSimplifier,
		'input': SquareRootInput,
	}
]