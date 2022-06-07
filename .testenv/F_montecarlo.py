# makes multiple instances of the object available.
from vandal.plugins.metaclass import Meta

# imports custom types.
from vandal.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
    AnyType,
)

import pandas as pd
import numpy as np

# makes multiple instances of the object available.
from vandal.plugins.metaclass import Meta

# imports custom types.
from vandal.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
    AnyType,
)


# stores menu options over functions and class methods for listing.
class Record(metaclass = Meta):

    # initializes the object and function it is decorating.
    def __init__(
        self,
        ) -> ReturnType:

        self.basic_menu : ListType = []
        self.descriptive_menu : ListType = []
        self.dictionary_menu : DictionaryType = {}
        self.individual_dict : DictionaryType = {}
        self.reset_dict : DictionaryType = {}
        self.poolsize : IntegerType = 0
        self.stored_keys : ListType = []
        self.print_val_dict : ListType = {}

        self.hidden_basic_menu : ListType = []
        self.hidden_descriptive_menu : ListType = []
        self.hidden_dictionary_menu : DictionaryType = {}
        self.contains_autoinit : BooleanType = False


    # option_name - stores the name for the config and display functions.
    # option_description - stores the description of the function for the config and display functions.
    # autoinit (True/False) - automatically initializes the function without storing into the dictionary menu.
    # print_val (True/False) - enables the print of function output.
    # -
    # creates and entry that is stored in a basic menu, descriptive menu and a dictionary menu.
    # DEFAULT: record.entry(option_name, option_description = '', autoinit = False, print_val = False).
    def entry(
        self, 
        option_name : StringType = '', 
        option_description : StringType = '',
        autoinit: BooleanType = False,
        print_val: BooleanType = False,
        ) -> StringDictionary:

        self.option_name = option_name
        self.option_description = option_description
        self.dict_name = self.option_name
        self.print_val = print_val
        self.individual_dict[self.dict_name] = {}
        self.reset_dict[self.dict_name] = {}
        self.print_val_dict[self.option_name] = self.print_val

        def record_function(func):

            if autoinit == False:
                self.dictionary_menu[self.option_name] = func
                self.basic_menu += [self.option_name]
                self.descriptive_function = str(self.option_name) + ' - ' + str(self.option_description)
                self.descriptive_menu += [self.descriptive_function]
            
            elif autoinit == True:
                self.hidden_dictionary_menu[self.option_name] = func
                self.hidden_basic_menu += [self.option_name]
                self.descriptive_function = str(self.option_name) + ' - ' + str(self.option_description)
                self.hidden_descriptive_menu += [self.descriptive_function]
                self.contains_autoinit = True

            def _wrap(*args, **kwargs):

                return func(*args, **kwargs)

            return _wrap

        return record_function


    # style ('decorator' - appends to a function.)
    # style ('function' - executes as a standalone function.)
    # method ('basic' - shows just record.entry stored names.)
    # method ('descriptive' - shows record.entry stored names and record.entry.option_description as a help menu.)
    # method ('dictionary' - creates a dictionary of record.entry names and the function they are appended on.)
    # return_option ('logs' - executes the function, but returns logs.)
    # return_option ('function' - shows logs, but returns the function.)
    # -
    # outputs saved menu as a function or decorator.
    # DEFAULT: record.display(style = 'decorator', method = 'dictionary', return_option = 'logs').
    def display(
        self,
        style : StringType = 'decorator', 
        method : StringType = 'dictionary', 
        return_option : StringType = 'logs',
        ) -> StringDictionary:

        if style == 'decorator':
            if return_option == 'logs':
                if method == 'basic':
                    def wrapper(func):
                        def decorator(self,*args, **kwargs):
                            func(*args, **kwargs)
                            return self.basic_menu
                        return decorator
                        
                    return wrapper

                elif method == 'descriptive':
                    def wrapper(func):
                        def decorator(self,*args, **kwargs):
                            func(*args, **kwargs)
                            return self.descriptive_menu
                        return decorator

                    return wrapper

                elif method == 'dictionary':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            func(*args, **kwargs)
                            return self.dictionary_menu
                        return decorator

                    return wrapper

            elif return_option == 'function':
                if method == 'basic':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            print(self.basic_menu)
                            return func(*args, **kwargs)
                        return decorator

                    return wrapper

                elif method == 'descriptive':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            print(self.descriptive_menu)
                            return func(*args, **kwargs)
                        return decorator

                    return wrapper

                elif method == 'dictionary':
                    def wrapper(func):
                        def decorator(self, *args, **kwargs):
                            print(self.dictionary_menu)
                            return func(*args, **kwargs)
                        return decorator

                    return wrapper
                
        elif style == 'function':
            if method == 'basic':
                return self.basic_menu

            elif method == 'descriptive':
                return self.descriptive_menu

            elif method == 'dictionary':
                return self.dictionary_menu


    # type ('static' - adapts to the execution of static non-self methods and functions.)
    # type ('dynamic' - adapts to the execution of dynamic class self methods and functions.)
    # display_headline - displays the desired headline.
    # display_message - displays input value message.
    # output_message - confirmation of the chosen value.
    # method ('descriptive' - shows stored option_name and it's description.)
    # method ('basic' - shows only the stored option_name.)
    # alignment ('basic' - shows all stored option_name and option_description values in a row.)
    # alignment ('newline' -shows all stored option_name and option_description values in a new line.)
    # queue (True/False) - enables stacking of functions and executing them in a chain.
    # show_dtypes (True/False) - shows the dtype of the input value.
    # -
    # creates an executeable menu from defined entries on top of functions.
    # DEFAULT: record.config(type = 'static', display_headline ='AVAILABLE OPTIONS', display_message = 'ENTER THE OPTION: ', output_message = 'YOU HAVE CHOSEN: ', method = 'descriptive', alignment = 'newline', queue = False, show_dtypes = True).
    def config(
        self, 
        type : StringType = 'static', 
        display_headline : StringType ='AVAILABLE OPTIONS', 
        display_message : StringType = 'ENTER THE OPTION: ', 
        output_message : StringType = 'YOU HAVE CHOSEN: ', 
        method : StringType = 'descriptive', 
        alignment : StringType = 'newline',
        queue: BooleanType = False,
        show_dtypes: BooleanType = True,
        ) -> DictionaryType:

        self.display_headline = display_headline
        self.display_message = display_message
        self.output_message = output_message
        self.queue = queue
        self.show_dtypes = show_dtypes
        self.yield_name = 0 # list item counter that enables iterating through the list.

        # assert type.
        if type != 'static' and type != 'dynamic':
            type = 'static'
            print('WARNING: Automactically forced type to static due to invalid type choice.')
            print('Write type = \'static\' or type = \'dynamic\' in the config option to change how this impacts the behaviour of executed functions in the menu.')
            print('')

        if alignment == 'basic':

            if method == 'basic':
                show_menu = self.display(style = 'function', method = 'basic')
                print(self.display_headline)
                print('-----------------')
                print(show_menu)

            elif method == 'descriptive':
                show_menu = self.display(style = 'function', method = 'descriptive')
                print(self.display_headline)
                print('-----------------')
                print(show_menu)

            else:
                print('INVALID METHOD CHOSEN, THE PROGRAM WILL CONTINUE WITHOUT DISPLAYED OPTIONS.\n')

        elif alignment == 'newline':

            if method == 'basic':
                show_menu = self.display(style = 'function', method = 'basic')
                print(self.display_headline)
                print('-----------------')
                for line in show_menu:
                    print(line)

            elif method == 'descriptive':
                show_menu = self.display(style = 'function', method = 'descriptive')
                print(self.display_headline)
                print('-----------------')
                for line in show_menu:
                    print(line)
            else:
                print('INVALID METHOD CHOSEN, THE PROGRAM WILL CONTINUE WITHOUT DISPLAYED OPTIONS.\n')

        if queue == False:

            self.option = input('\n' + self.display_message)

            self.print_option = self.print_val_dict[self.option]

            print(self.output_message, self.option + '\n')

            # executes autoinit function.
            if self.contains_autoinit == True:

                try:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i](self)
                except:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i]()

            if type == 'static':

                try:
                    if self.print_option == False:
                        return self.dictionary_menu[self.option](self)
                    else:
                        return print(self.dictionary_menu[self.option](self))

                except:
                    if self.print_option == False:
                        return self.dictionary_menu[self.option]()
                    else:
                        return print(self.dictionary_menu[self.option]())

            elif type == 'dynamic':

                try:
                    return self.dictionary_menu[self.option]()
                except:
                    return self.dictionary_menu[self.option](self)

        if queue == True:
            # executes autoinit functions.
            if self.contains_autoinit == True:

                try:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i](self)
                except:
                    for i in self.hidden_dictionary_menu:
                        self.hidden_dictionary_menu[i]()

            # enables a loop to execute functions in a chain.
            self.queue_handler()

            if type == 'static':

                print(self.tmp_name_list[self.yield_name])

                for tmp_func in self.tmp_list:

                    self.clone_dict = self.tmp_name_list[self.yield_name]

                    self.print_option = self.tmp_print_list[self.yield_name]

                    print(self.tmp_name_list[self.yield_name])

                    self.redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(self, **self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(**self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1

            elif type == 'dynamic':
                
                for tmp_func in self.tmp_list:

                    self.clone_dict = self.tmp_name_list[self.yield_name]

                    self.print_option = self.tmp_print_list[self.yield_name]

                    print(self.tmp_name_list[self.yield_name])

                    self.redefine()

                    try:
                        if self.print_option == False:
                            tmp_func(**self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(**self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1
                    except:
                        if self.print_option == False:
                            tmp_func(self, **self.individual_dict[self.clone_dict])
                            print('')
                            self.yield_name += 1
                        else:
                            print(tmp_func(self, **self.individual_dict[self.clone_dict]))
                            print('')
                            self.yield_name += 1

        return

    # variable - name of the function argument input is being passed as.
    # type - type of the data being passed ('int', 'float', 'str', 'bool', 'list', 'tuple', 'dict' and 'vector' supported).
    # -
    # function that stores the input value in a dictionary.
    def store(self, variable, type):
        self.type = type
        self.variable = variable
        self.individual_dict[self.dict_name][self.variable] = self.type
        self.reset_dict[self.dict_name][self.variable] = self.type
        return self.dict_name

    # function that casts an input of a certain data type and formats it before sending as a function argument.
    def redefine(self):
        if self.show_dtypes == True:
                print(self.reset_dict)
        for i in self.individual_dict[self.clone_dict]:
            self.format = self.reset_dict[self.clone_dict][i]
            if self.format != 'list':
                self.new_i = input(f'Enter the {i}: ')
            self.dtypes = {
            'int': self.set_int,
            'float': self.set_float,
            'str': self.set_str,
            'list' : self.set_list,
        }
            self.new_i = self.dtypes[self.format]()
            self.individual_dict[self.clone_dict][i] = self.new_i
        return self.individual_dict[self.clone_dict]

    # converts input to int.
    def set_int(self):
        self.new_i = int(self.new_i)
        return self.new_i

    # converts input to float.
    def set_float(self):
        self.new_i = float(self.new_i)
        return self.new_i

    # converts input to string.
    def set_str(self):
        self.new_i = str(self.new_i)
        return self.new_i

    # converts input to string.
    def set_list(self):
        self.range = int(input('Number of list values: '))
        self.new_i = []
        for i in range(0, self.range):
            tmp_list_element = int(input(f'Enter the value: '))
            self.new_i.append(tmp_list_element)
        return self.new_i


    # iterate (True/False) - enables the functionality of queue, do not change!
    # -
    # enables a loop for the queue.
    def queue_handler(
        self,
        iterate: BooleanType = True,
        ) -> ReturnType:

        self.print_val_list = []
        self.tmp_list = []
        self.iterate = iterate
        self.tmp_name_list = []
        self.tmp_print_list = []
        while self.iterate == True:

            self.option = input('\n' + self.display_message)

            self.tmp_name_list += [self.option]

            self.print_val_list += self.option

            print(self.output_message, self.option + '\n')

            self.tmp_list += [self.dictionary_menu[self.option]]

            self.tmp_print_list += [self.print_val_dict[self.option]]

            choice = input('Continue? (Y/N): ')

            choice = choice.upper()

            if choice != 'Y':

                self.iterate = False
                print('')
        
        return self.tmp_list


# coloring.
from colorama import Fore, init 

init()

# type hints and annotations.
from vandal.plugins.metaclass import Meta
from vandal.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
    AnyType,
)

app = Record()

# object that contains the simulation data.
class MonteCarlo:

    '''

    (OBJECT INFO)
    -------------

    eg. MonteCarlo = vandal.MonteCarlo()

    vandal.MonteCarlo - main class that stores the simulation data.

        * takes 5 additional arguments.
            list_of_values - pandas dataframe of values.
            time_seq - desired time sequence.
            num_sims - desired number of simulation iterations.
            ref_col (default: ref_col = 0) - column index of the dictionary values.
            ref_row (default: ref_row = 0) - row index on which the starting point of the simulation is created.
        * Requirements:
            data stored as dictionary of key, value pair | list | numpy array | pandas DataFrame.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.MonteCarlo.function()

        .execute() - executes a Monte Carlo simulation on a defined data set.
            * takes 1 additional argument.
                filtered (defualt: filtered = True) - filters the print option and leaves just the return object.

        .graph() - plots the Monte Carlo simulation on a graph.
            * takes 5 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True).
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                perform_block (default: perform_block = True) - False/True may be used depending on the IDE requirements.

        .get_risk() - calculates the risk of value decrease over time.
            * takes 1 additional argument.
                risk_sims (default: risk_sims = 5000) - number of simulations to perform the risk percantage.

        .get_stats() - shows the statistics of the Monte Carlo simulation.
            * takes no additional arguments.

        .get_change() - shows the percentage of Monte Carlo simulation value change for every iteration.
            * takes no additional arguments.

        .hist() - plots the histogram of Monte Carlo simulation.
            * takes 7 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), set_bins = None, perform_block = True, method = 'b').
            If method = 'e' is chosen, no customization arguments apply.
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                perform_block (default: perform_block = True) - False/True may be used depending on the IDE requirements.
                method - default method is Basic histogram and it's performed by automation. In order to plot Empirical rule histogram add method = 'e' as the last argument. - NOTE: method of a histogram must be placed within quotation marks.
                set_bins - sets the amount of bins of the histogram. (default: set_bins = self.time_seq)
            * automatically executes the .get_stats() function in order to get standard deviation for the Empirical rule plotting.

    MCapp (EXECUTABLE CLI MODULE)
    -------------------------

    vandal.MCapp is an executable function that runs the Command Line Interface of the vandal MonteCarlo module.
        print(help(vandal.MCapp)) in order to see available features.
        
    '''

    # metadata of the used library.
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

    # initial launch.
    @app.entry('init', 'initializes object')
    def __init__(
        self, 
        list_of_values : NumberVectorAlike = app.store('list_of_values', 'list'), 
        time_seq : IntegerType = app.store('time_seq', 'int'), 
        num_sims : IntegerType = app.store('num_sims', 'int'),
        ref_col : IntegerType = 0, 
        ref_row : IntegerType = 0,
        ) -> ReturnType:

        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims
        self.ref_col = ref_col
        self.ref_row = ref_row

        return 

    # class information.
    def __str__(
        self,
        ) -> StringType:

        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    # class information.
    def __repr__(
        self,
        ) -> StringType:

        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    # executes a Monte Carlo simulation on a defined data set.
    @app.entry('execute', 'executes the function')
    def execute(
        self,
        filtered : BooleanType = True,
        ) -> NumberArrayAlike:

        if filtered == False:
            print(Fore.GREEN + f'Monte Carlo has been set up for {self.num_sims} simulations in a period of {self.time_seq} time measurement units and executed.' + Fore.RESET)
            print(Fore.RED + 'NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.' + Fore.RESET)
        
        from vandal.hub.toolkit import random_value
        import pandas as pd

        # this removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        # end of pandas warning removal block.

        try:
            self.list_of_values = pd.DataFrame(self.list_of_values)
            self.list_of_values = self.list_of_values.iloc[:, self.ref_col]
        except:
            raise KeyError('Impossible to reach a defined key, value pair. Data types supported: dictionary, list, numpy array, pandas DataFrame. Make sure to set index row_col on an existing field. Must be of type: int.')

        today_value = self.list_of_values.iloc[self.ref_col]
        data = pd.DataFrame()
        loading = 0

        for num_sim in range(self.num_sims):
            rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
            count = 0
            index_array = []
            index_array += [today_value * (1 + rand_change)]

            if index_array[count] > (index_array[-1] * 3):
                raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation cannot be executed properly.')

            for num_day in range(self.time_seq):
                rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                if count == self.time_seq:
                    break
                index_array += [index_array[count] * (1 + rand_change)]
                count += 1

                if index_array[count] > (index_array[-1] * 3):
                    raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation function cannot be executed properly.')

            loading += 1
            print(end = '\r')
            print(loading, 'iterations out of', self.num_sims, 'executed so far', end = '')

            data[num_sim] = index_array
        print(end = '\r')
        print(Fore.GREEN + 'Monte Carlo simulation set up and ready to plot.' + Fore.RESET)
        self.results = data

        return data

    # shows the percentage of Monte Carlo simulation value change for every iteration.
    def get_change(
        self,
        ) -> NumberArrayAlike:

        return self.results.pct_change()

    # calculates the risk of negative values occuring.
    @app.entry('get_risk', print_val=True)
    def get_risk(
        self, 
        risk_sims : IntegerType = 5000,
        ) -> NumberType:

        import random
        import pandas as pd

        # this removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        # end of pandas warning removal block.

        today_value = self.list_of_values.iloc[self.ref_row]
        percent_change = self.list_of_values.pct_change()
        data = pd.DataFrame()
        smaller = []

        for num_sim in range(risk_sims):
            random_change = random.choice(percent_change)
            index_array = []

            index_array += [today_value * (1 + (random_change))]
            data[num_sim] = index_array

            for sim in data[num_sim]:
                if sim < today_value:
                    smaller += [sim]
        NRisk = len(smaller) / num_sim * 100

        assert (NRisk < 100), '\nTime sequence and/or number of iterations are too low for the proper risk calculation.'

        return str(round(NRisk, 2)) + '%'

    # plots the Monte Carlo simulation on a graph.
    def graph(
        self, 
        graph_title : StringType = 'Monte Carlo simulation', 
        x_title : StringType = 'X axis', 
        y_title : StringType = 'Y axis', 
        plot_size : TupleType = (25,10), 
        perform_block : BooleanType = True,
        ) -> GraphType:

        print(Fore.GREEN + '\nMonteCarlo() plotting initialized.' + Fore.RESET)
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('vandal (c) David Kundih, 2021-2022', fontsize = 14, weight = 'regular', loc = 'right')
        plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
        plt.plot(self.results)
        plt.axhline(y = self.results[0][0], color = 'k', linestyle = 'solid')
        plt.xlabel(x_title, fontsize = 18, weight = 'semibold')
        plt.ylabel(y_title, fontsize = 18, weight = 'semibold')
        plt.show(block = perform_block)
        print(Fore.GREEN + 'MonteCarlo() plotting finished.' + Fore.RESET)

        return

    # shows the statistics of the Monte Carlo simulation.
    def get_stats(
        self,
        ) -> AnyArrayAlike:
        
        import numpy as np
        import pandas as pd

        mean_value = np.mean(self.results.loc[self.time_seq])
        mean_value = round((mean_value),2)
        standard_deviation = round(np.std(self.results.loc[self.time_seq]),2)
        standard_deviation = round((standard_deviation),2)
        maximum_value = np.max(self.results.loc[self.time_seq])
        maximum_value = round((maximum_value),2)
        minimum_value = np.min(self.results.loc[self.time_seq])
        minimum_value = round((minimum_value),2)
        self.standard_deviation = standard_deviation
        self.mean_value = mean_value

        stats = {
            'Mean value' : mean_value, 
            'Standard deviation' : standard_deviation, 
            'Maximum value ' : maximum_value, 
            'Minimum value' : minimum_value,
            }

        stats = pd.DataFrame(stats, index = ['Statistics'])
        stats = stats.transpose()

        return stats 

    # plots the histogram of Monte Carlo simulation.
    def hist(
        self, 
        graph_title : StringType = 'Histogram of value frequencies', 
        x_title : StringType = 'X axis', 
        y_title : StringType = 'Y axis', 
        plot_size : TupleType = (25,10), 
        perform_block : BooleanType = True,
        set_bins : IntegerType = None,
        **method : StringType,
        ) -> GraphType:

        self.get_stats()
        std_plus = self.mean_value + self.standard_deviation
        std_minus = self.mean_value - self.standard_deviation
        std_plus2 = self.mean_value + (self.standard_deviation * 2)
        std_minus2 = self.mean_value - (self.standard_deviation * 2)
        std_plus3 = self.mean_value + (self.standard_deviation * 3)
        std_minus3 = self.mean_value - (self.standard_deviation * 3)

        if self.time_seq > 50:
            print(Fore.RED + 'NOTE: Time sequence defined greatly impacts the lenght of histogram plotting.\n' + Fore.RESET)

        print(Fore.GREEN + 'Histogram plotting initiated...' + Fore.RESET)
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('vandal (c) David Kundih, 2021-2022', fontsize = 14, weight = 'regular', loc = 'right')

        if method.get("method") != "e":
            print(Fore.GREEN + 'CHOSEN METHOD: Basic histogram model.' + Fore.RESET)
            plt.suptitle(graph_title, fontsize = 25, weight = 'bold')

        if method.get("method") == "e":
            print(Fore.GREEN + 'CHOSEN METHOD: Empirical rule.' + Fore.RESET)
            plt.suptitle('Value division based on the Empirical rule', fontsize = 25, weight = 'bold')
            plt.axvline(x = std_plus, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus, color = 'r', linestyle = 'dashed')
            plt.axvline(x = self.mean_value, color = 'k', linestyle = 'solid')
            plt.axvline(x = std_plus2, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus2, color = 'r', linestyle = 'dashed')
            plt.axvline(x = std_plus3, color = 'g', linestyle = 'dashed')
            plt.axvline(x = std_minus3, color = 'r', linestyle = 'dashed')

        if set_bins == None:
            set_bins = self.time_seq
            
        plt.hist(self.results, bins = set_bins, ec = 'm')
        plt.xlabel(x_title, weight = 'semibold')
        plt.ylabel(y_title, weight= 'semibold')
        plt.show(block = perform_block)
        print(Fore.GREEN + 'Histogram plotting finished.', Fore.RESET)

        return



# runs module as an app.
if __name__ == '__main__':
    app.config(type='dynamic', queue=True)
