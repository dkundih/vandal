# coloring.
import colorama
from colorama import Fore, init 

init()

# object that contains the simulation data.
class MonteCarlo:

    '''

    (OBJECT INFO)
    -------------

    vandal.MonteCarlo - main class.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.MonteCarlo.function()

        .execute() - executes a Monte Carlo simulation on a defined data set.
            * takes 4 additional arguments.
            list_of_values - pandas dataframe of values.
            time_seq - desired time sequence.
            num_sims - desired number of simulation iterations.
            ref_value_index (default: ref_value_index = 0) - index on which the starting point of the simulation is created.
        * Requirements:
            pandas Python module.
            pd.DataFrame() defined data set.

        .graph() - plots the Monte Carlo simulation on a graph.
            * takes 5 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True).
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                perform_block (default: perform_block = True) - False/True may be used depending on the IDE requirements.

        .get_risk() - calculates the risk of value decrease over time.
            * takes 1 optional argument (default: risk_sims = 5000).

        .get_stats() - shows the statistics of the Monte Carlo simulation.
            * takes no additional arguments.

        .get_change() - shows the percentage of Monte Carlo simulation value change for every iteration.
            * takes no additional arguments.

        .hist() - plots the histogram of Monte Carlo simulation.
            * takes 6 optional customization arguments. (default: graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True, method = 'b').
            If method = 'e' is chosen, no customization arguments apply.
                graph_title - title of the graph.
                x_title - title of the X axis.
                y_title - title on the Y axis.
                plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.
                perform_block (default: perform_block = True) - False/True may be used depending on the IDE requirements.
                method - default method is Basic histogram and it's performed by automation. In order to plot Empirical rule histogram add method = 'e' as the last argument. - NOTE: method of a histogram must be placed within quotation marks.
            * automatically executes the .get_stats(filtered = True) function in order to get standard deviation for the Empirical rule plotting.

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
    def __init__(self):
        pass

    # class information.
    def __str__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    # class information.
    def __repr__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    # executes a Monte Carlo simulation on a defined data set.
    def execute(self, list_of_values, time_seq, num_sims, ref_value_index = 0):
        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims
        self.ref_value_index = ref_value_index
        print(Fore.GREEN + f'Monte Carlo has been set up for {self.num_sims} simulations in a period of {self.time_seq} time measurement units and executed.' + Fore.RESET)
        from vandal.hub.toolkit import random_value
        print(Fore.RED + 'NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.' + Fore.RESET)
        #print('The model that will be able to handle big standard deviations is currently being worked on, thank you for your patience.\n')
        import pandas as pd
        # this removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        # end of pandas warning removal block.
        today_value = self.list_of_values.iloc[self.ref_value_index]
        data = pd.DataFrame()
        loading = 0

        for num_sim in range(self.num_sims):
            rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
            count = 0
            index_array = []
            index_array += [today_value * (1 + rand_change)]

            if index_array[count] > (index_array[-1] * 2):
                raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation cannot be executed properly.')

            for num_day in range(self.time_seq):
                rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                if count == self.time_seq:
                    break
                index_array += [index_array[count] * (1 + rand_change)]
                count += 1

                if index_array[count] > (index_array[-1] * 2):
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
    def get_change(self):
        return self.results.pct_change()

    # calculates the risk of negative values occuring.
    def get_risk(self, risk_sims = 5000):
        import random
        import pandas as pd
        #This removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action = 'ignore', category = pd.errors.PerformanceWarning)
        #End of pandas warning removal block.
        today_value = self.list_of_values.iloc[self.ref_value_index]
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

        print(Fore.GREEN + '\nRisk for this option is' + Fore.RESET, round(NRisk,2), Fore.GREEN + '%.' + Fore.RESET)

    # plots the Monte Carlo simulation on a graph.
    def graph(self, graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True):
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

    # shows the statistics of the Monte Carlo simulation.
    def get_stats(self, filtered = False):
        import numpy as np
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
        if filtered == False:
            print(Fore.GREEN + '\nNumber of simulations: ' + Fore.RESET, self.time_seq)
            print(Fore.GREEN + 'Number of iterations: ' + Fore.RESET, self.num_sims)
            print(Fore.GREEN + 'Mean value: ' + Fore.RESET, mean_value)
            print(Fore.GREEN + 'Standard deviation: ' + Fore.RESET, standard_deviation)
            print(Fore.GREEN + 'Maximum: ' + Fore.RESET, maximum_value)
            print(Fore.GREEN + 'Minimum: ' + Fore.RESET, minimum_value)

    # plots the histogram of Monte Carlo simulation.
    def hist(self, graph_title = 'Histogram of value frequencies', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True, **method):
        self.get_stats(filtered = True)
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

        plt.hist(self.results, bins = self.time_seq , ec = 'm')
        plt.xlabel(x_title, weight = 'semibold')
        plt.ylabel(y_title, weight= 'semibold')
        plt.show(block = perform_block)
        print(Fore.GREEN + 'Histogram plotting finished.', Fore.RESET)

    # access saved menu particles from function execution.  
    def get_menu(self):
        return
        
    
# CLI application.
def MCapp():

    '''
    
    runs as:

        *IDE: vandal.MCapp()
        *TERMINAL: python -m vandal -e montecarlo / python -m vandal --entry montecarlo
        
    '''

    # relevant imports.
    import os
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
        import pandas as pd
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
    MC = MonteCarlo()
    simulations = int(input('Enter number of simulations: ') or 100)
    period = int(input('Enter desired period: ') or 50)
    print('')
    executed = MC.execute(list_of_values = data, num_sims = simulations, time_seq = period)

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
                save_to(file = executed, prefix = 'vandal.MonteCarlo - ' , func_name = 'change', choice = file_type)
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
            MC.get_stats()
        if action == 'risk':
            sample = int(input('Number of iterations to measure risk on: ') or 5000)
            MC.get_risk(risk_sims = sample)
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