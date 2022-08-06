'''

vandal - Data science, Data manipulation and Machine learning library.
=====================================================================

This is a connection to the __init__ file of the vandal library.

AVAILABLE FEATURES IN THE LIBRARY:

    TOOLKIT (MODULE FUNCTIONS)
    --------------------------

    set of available data manipulation functions from the vandal library.
        print(help(any_function_listed_below)) in order to see the function details or print(help(vandal.toolkit)) for all functions at once.

        FUNCTIONS (ACCESSIBLE DIRECTLY FROM THE LIBRARY)
        ------------------------------------------------

            random_value(mean, st_dev, **rounded) - gives a random value of mean and standard deviation inputed, if rounded = 'y', value will be rounded.

            random_pool(mean, st_dev, pool_size, **rounded) - gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = 'y', values will be rounded.

            split_values(data, split_method) - splits the data using a split method character.

            join_values(data, join_method) - joins the data using a join metod character.

            replace_values(data, replaced_value, replacing_value) - replaces a defined value with a desired value.

            list_sort(data, array) - manually sorts data depending on defined array of indexes.

            index_sort(data, split_method, index_array) - sorts the indicies in a list of values based on the index array defined as [x,x,x].

            auto_sort(data, split_method, trigger = lambda x: x[0]) - automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.

            create_password(length) - creates a random password with adjustable lenght (default: length = 8).

            save_to(file, prefix, func_name, choice) - file saver for code clarity.

            file_handler(file) - handles the file extension upon import.
            
            paint_text(text, color, print_trigger = True) - paints the text with a desired color ('r', 'g', 'b', 'k', 'c', 'm', 'y').

    EXAMPLE (MODULE FUNCTIONS)
        --------------------------

        set of example functions to perform machine learning and data science operations over.
            print(help(any_function_listed_below)) in order to see the function details or print(help(vandal.example)) for all functions at once.

        FUNCTIONS (ACCESSIBLE DIRECTLY FROM THE LIBRARY)
        ------------------------------------------------

            linear_regression(x_range = (1, 500), y_factor = 2, deviation = 50, min_value = 1) -> ReturnType: - creates an example linear regression data set where x is index 0 and y is index 1.


    MONTECARLO (OBJECT)
    -------------------

    vandal.MonteCarlo is a module for performing the Monte Carlo simulation over the defined data with a lot of useful features.
        print(help(vandal.MonteCarlo)) in order to see available features.

    EOQ (OBJECT)
    ------------

    vandal.EOQ is a module for finding an Economic order quantity over the defined data with a lot of useful features.
        print(help(vandal.EOQ)) in order to see available features.

    Dijkstra (OBJECT)
    -----------------

    vandal.Dijkstra is a module for finding the optimal route between the defined nodes from the place of origin to the final destination.
        print(help(vandal.Dijkstra)) in order to see available features.

    MCapp (EXECUTABLE CLI MODULE)
    -------------------------

    vandal.MCapp is an executable function that runs the Command Line Interface of the vandal MonteCarlo module.
        print(help(vandal.MCapp)) in order to see available features.

    EOQapp (EXECUTABLE CLI MODULE)
    -------------------------

    vandal.EOQapp is an executable function that runs the Command Line Interface of the vandal EOQ module.
        print(help(vandal.EOQapp)) in order to see available features.

'''

# ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

# colorama imports.
from colorama import (
    Fore,
    init,
)

init()

# meta data imports from the vandal library.
from vandal.misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
    __APPversion__,
)

# imports plugins.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# metaclass.
metaclass = [
    'Meta',
]

# object and module imports.
from vandal.hub import toolkit
from vandal.hub import example
from vandal.objects.eoq import(
    EOQ,
    EOQapp,
)
from vandal.objects.montecarlo import (
    MonteCarlo,
    MCapp,
)
from vandal.objects.dijkstra import Dijkstra

# hub toolkit imports.
from vandal.hub.toolkit import (
    random_value,
    random_pool,
    split_values,
    join_values,
    replace_values,
    list_sort,
    index_sort,
    auto_sort,
    create_password,
    file_handler,
    save_to,
    paint_text,
)

# hub example imports.
from vandal.hub.example import linear_regression

# all relevant contents.
__all__ = [
    'random_value',
    'random_pool',
    'split_values',
    'join_values',
    'replace_values',
    'list_sort',
    'index_sort',
    'auto_sort',
    'create_password',
    'file_handler',
    'save_to',
    'paint_text',
    'toolkit',
    'example',
    'linear_regression',
    'MonteCarlo',
    'MCapp',
    'EOQ',
    'EOQapp',
    'Dijkstra',
    'VandalTypes',
    'Meta',
]
