'''
NOTE: vandal package runs on top of the duality package, in order to see more about the actual code visit the duality package repositories at:
	https://github.com/dkundih/duality
	https://pypi.org/project/duality

This is a connection to the main folder of the vandal package.

AVAILABLE MODULES IN THE PACKAGE:
	HUB
	---
	vandal.hub is a hub of data manipulation tools.
		print(help(vandal.hub)) in order to see available features.
	MONTECARLO
	---
	vandal.MonteCarlo is a module for performing the Monte Carlo simulation over the defined data with a lot of useful features.
		print(help(vandal.MonteCarlo)) in order to see available features.
	EOQ
	---
	vandal.EOQ is a module for finding an Economic order quantity over the defined data with a lot of useful features.
		print(help(vandal.EOQ)) in order to see available features.

'''

#imports essential functions from the duality package.
from duality import EOQ
from duality.hub import hub
from duality import MonteCarlo

#imports meta data from the vandal package.
from vandal.misc._meta import (
	__author__,
	__copyright__,
	__credits__,
	__license__,
	__version__,
	__documentation__,
	__contact__,
	__donate__
)