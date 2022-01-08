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

    (DEVELOPER MODE)
    ----------------

    Developer mode functions can only be set up manually by removing the '#DEVELOPER MODE -' in the source code.

        * takes no additional arguments.
        * Requirements:
            '# DEVELOPER MODE -' removed in the code.

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
    )

    # import duality package decorators.
    # DEVELOPER MODE -  from duality.decorators.classparticles import track, record

    # initial launch.
    # DEVELOPER MODE - @track.entry('init')
    # DEVELOPER MODE - @record.entry(option_name = 'init', option_description = 'initial launch.')
    def __init__(self):
        pass

    # class information.
    # DEVELOPER MODE - @track.entry('string')
    # DEVELOPER MODE - @record.entry(option_name = 'string', option_description = 'class information.')
    def __str__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    # class information.
    # DEVELOPER MODE - @track.entry('representation')
    # DEVELOPER MODE - @record.entry(option_name = 'repr', option_description = 'shows object details.')
    def __repr__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    # executes a Monte Carlo simulation on a defined data set.
    # DEVELOPER MODE - @track.entry('execution')
    # DEVELOPER MODE - @record.entry(option_name = 'execution', option_description = 'executes a Monte Carlo simulation on a defined data set.')
    def execute(self, list_of_values, time_seq, num_sims, ref_value_index = 0):
        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims
        self.ref_value_index = ref_value_index
        print(f'Monte Carlo has been set up for {self.num_sims} simulations in a period of {self.time_seq} time measurement units.')
        from vandal.hub.toolkit import random_value
        print('Monte Carlo simulation has been executed.')
        print('NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.\nThe model that will be able to handle big standard deviations is currently being worked on, thank you for your patience.\n')
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
        print('Monte Carlo simulation set up and ready to plot.')
        self.results = data
        return data

    # shows the percentage of Monte Carlo simulation value change for every iteration.
    # DEVELOPER MODE - @track.entry('change')
    # DEVELOPER MODE - @record.entry(option_name = 'change', option_description = 'shows the percentage of Monte Carlo simulation value change for every iteration.')
    def get_change(self):
        return self.results.pct_change()

    # calculates the risk of negative values occuring.
    # DEVELOPER MODE - @track.entry('risk')
    # DEVELOPER MODE - @record.entry(option_name = 'risk', option_description = 'calculates the risk of negative values occuring.')
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

        print('\nRisk for this option is', round(NRisk,2), '%.')

    # plots the Monte Carlo simulation on a graph.
    # DEVELOPER MODE - @track.entry('graph')
    # DEVELOPER MODE - @record.entry(option_name = 'graph', option_description = 'plots the Monte Carlo simulation on a graph.')
    def graph(self, graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True):
        print('\nMonteCarlo() plotting initialized.')
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('vandal (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')
        plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
        plt.plot(self.results)
        plt.axhline(y = self.results[0][0], color = 'k', linestyle = 'solid')
        plt.xlabel(x_title, fontsize = 18, weight = 'semibold')
        plt.ylabel(y_title, fontsize = 18, weight = 'semibold')
        plt.show(block = perform_block)
        print('MonteCarlo() plotting finished.')

    # shows the statistics of the Monte Carlo simulation.
    # DEVELOPER MODE - @track.entry('statistics')
    # DEVELOPER MODE - @record.entry(option_name = 'statistics', option_description = 'shows the statistics of the Monte Carlo simulation.')
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
            print('\nNumber of simulations: ', self.time_seq)
            print('Number of iterations: ', self.num_sims)
            print('Mean value: ', mean_value)
            print('Standard deviation: ', standard_deviation)
            print('Maximum: ', maximum_value)
            print('Minimum: ', minimum_value, '\n')

    # plots the histogram of Monte Carlo simulation.
    # DEVELOPER MODE - @track.entry('histogram')
    # DEVELOPER MODE - @record.entry(option_name = 'histogram', option_description = 'plots the histogram of Monte Carlo simulation.')
    def hist(self, graph_title = 'Histogram of value frequencies', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), perform_block = True, **method):
        self.get_stats(filtered = True)
        std_plus = self.mean_value + self.standard_deviation
        std_minus = self.mean_value - self.standard_deviation
        std_plus2 = self.mean_value + (self.standard_deviation * 2)
        std_minus2 = self.mean_value - (self.standard_deviation * 2)
        std_plus3 = self.mean_value + (self.standard_deviation * 3)
        std_minus3 = self.mean_value - (self.standard_deviation * 3)

        if self.time_seq > 50:
            print('NOTE: Time sequence defined greatly impacts the lenght of histogram plotting.\n')

        print('Histogram plotting initiated...')
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('vandal (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')

        if method.get("method") != "e":
            print('CHOSEN METHOD: Basic histogram model.')
            plt.suptitle(graph_title, fontsize = 25, weight = 'bold')

        if method.get("method") == "e":
            print('CHOSEN METHOD: Empirical rule.')
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
        print('Histogram plotting finished.')

    # DEVELOPER MODE - @record.display()
    # DEVELOPER MODE - @track.entry('menu')
    # DEVELOPER MODE - @record.entry(option_name = 'menu', option_description = 'access saved menu particles from function execution.')
    # access saved menu particles from function execution.  
    def get_menu(self):
        return

    # DEVELOPER MODE - @track.display()
    # DEVELOPER MODE - @track.entry('logs')
    # DEVELOPER MODE - @record.entry(option_name = 'logs', option_description = 'access saved logs from function execution.')
    # access saved logs from function execution.
    def get_logs(self):
        return
