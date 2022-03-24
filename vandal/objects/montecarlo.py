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
)

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
    def __init__(
        self, 
        list_of_values : NumberVectorAlike = None, 
        time_seq : IntegerType = None, 
        num_sims : IntegerType = None,
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

    
# CLI application.
def MCapp():

    '''
    
    runs as:

        *IDE: vandal.MCapp()
        *TERMINAL: python -m vandal -e montecarlo / python -m vandal --entry montecarlo
        
    '''

    print(Fore.YELLOW + 'MonteCarlo app is initializing...', Fore.RESET)
    
    # relevant imports.
    import os
    import pandas as pd
    from vandal.misc._meta import (
        __version__,
        __APPversion__,
    )
    from vandal.objects.montecarlo import MonteCarlo
    from vandal.hub.toolkit import (
        save_to,
        file_handler,
    )
    os.system('cls')

    # greeting.
    print(Fore.YELLOW + '\n - vandal Command Line Interface Application © David Kundih -', __APPversion__)
    print(Fore.YELLOW + ' - vandal package version -', 'v',__version__, Fore.RESET, '\n')
    print(Fore.YELLOW + 'DATA INPUT OPTIONS', Fore.RESET)
    print('0 | Manual input')
    print('1 | File input\n')

    inputchoice = input('Enter the option number: ')

    # manual input.
    if inputchoice == '0':
        iter = True
        print(Fore.RED + '\nWrite any non-number value to stop.', Fore.RESET)
        data = []

        while iter:
            try:
                listinput = input('Enter a value: ')
                listinput = listinput.replace(",", ".")
                listinput = float(listinput)

                data.append(listinput)
            except:
                print('')
                iter = False

        data = pd.DataFrame(data)
        data = data[0]

    # file input.
    elif inputchoice == '1':
        inputfile = input('Enter the file destination: ')

        data = file_handler(file = inputfile)

    # error on input.
    else:
        raise KeyError('Invalid input, please choose one of the stated options.')

    # simulation parameters and execution.
    simulations = int(input('Enter number of simulations: ') or 100)
    period = int(input('Enter desired period: ') or 50)

    MC = MonteCarlo(list_of_values = data, num_sims = simulations, time_seq = period)
    print('')
    executed = MC.execute(filtered = False)

    # options after defining the parameters. 
    while True:
        action = input('\n>>> ACTIONS: graph, change, values, stats, risk, hist, help, home: ')

        if action == 'graph':
            print('')

            title = input('Title: ')
            x_axis = input('X axis title:')
            y_axis = input('Y axis title:')

            MC.graph(graph_title = title, x_title = x_axis, y_title = y_axis)

        if action == 'change':
            print(Fore.YELLOW + '\nSAVE OPTIONS', Fore.RESET)
            print('0 | csv')
            print('1 | xlsx')
            print('2 | json')

            file_type = input('\nEnter the number or name of file type: ')

            output = MC.get_change()

            try:
                save_to(file = output, prefix = 'vandal.MonteCarlo - ' , func_name = 'change', choice = file_type)
            except:
                raise Exception('=== UNABLE TO SAVE, PLEASE SELECT ONE OF THE OPTIONS AND/OR RUN THE TERMINAL AS AN ADMINISTRATOR. ===')

        if action == 'values':
            print(Fore.YELLOW + '\nSAVE OPTIONS', Fore.RESET)
            print('0 | csv')
            print('1 | xlsx')
            print('2 | json')

            file_type = input('\nEnter the number or name of file type: ')

            try:
                save_to(file = executed, prefix = 'vandal.MonteCarlo - ', func_name = 'values', choice = file_type)
            except:
                raise Exception('=== UNABLE TO SAVE, PLEASE RUN THE TERMINAL AS AN ADMINISTRATOR. ===')

        if action == 'stats' or action == 'statistics':
            print('\n', MC.get_stats())

        if action == 'risk':
            sample = int(input('Number of iterations to measure risk on: ') or 5000)

            executed_risk = MC.get_risk(risk_sims = sample)

            print(Fore.YELLOW + '\nRisk for this option is' + Fore.RESET, executed_risk[:-1], Fore.YELLOW + '%.' + Fore.RESET)

        if action == 'hist' or action == 'histogram':
            print('')
            x_axis = input('X axis title:')
            y_axis = input('Y axis title:')
            print(Fore.YELLOW + '\nHISTOGRAM METHODS', Fore.RESET)
            print('0 | Basic Histogram')
            print('1 | Empirical Rule Histogram')

            method = input('\nEnter the histogram method number: ')

            if method == '0':
                MC.hist(x_title = x_axis, y_title = y_axis)
            elif method == '1':
                MC.hist(x_title = x_axis, y_title = y_axis, method = 'e')
            else:
                print(Fore.RED + '=== INVALID METHOD. ===\n', Fore.RESET)

        if action == 'home':
            print(Fore.YELLOW + 'Exiting...', Fore.RESET)
            
            break
        
        if action == 'help':
            print(Fore.YELLOW + '\nhttps://github.com/dkundih/vandal', Fore.RESET)

# runs module as an app.
if __name__ == '__main__':
    MCapp()
