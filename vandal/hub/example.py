# dependencies import.
import random
from logistics.plugins.types import *

'''

(MODULE FUNCTIONS)
--------------------------

vandal.example is a set of example functions to perform machine learning and data science operations over.

		linear_regression(x_range = (1, 500), y_factor = 2, deviation = 50, min_value = 1) -> ReturnType: - creates an example linear regression data set where x is index 0 and y is index 1.

'''

# creates an example linear regression data set where x is index 0 and y is index 1.
def linear_regression(
    x_range : TupleType = (1, 500),
    y_factor : NumberType = 2,
    deviation: NumberType = 50,
    min_value: NumberType = 1,
	) -> ReturnType:
	x = [i for i in range(*x_range)]
	y = [i * y_factor for i in x]
	y = [random.gauss(i, deviation) for i in y]
	data = [x, y]
	data = [[data[0][i] for i in range(len(data[0])) if data[1][i] > min_value], [round(data[1][i], 2) for i in range(len(data[1])) if data[1][i] > min_value]]
	return data
