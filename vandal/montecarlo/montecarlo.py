#imports essential functions from the vandal module.
from vandal.hub.hub import random_value
from vandal.misc.global_functions import *

#shows detailed overview of available functions.
def help():  
    print('*** NOTE: vandal.montecarlo works only for sequential data with reasonable standard deviation, otherwise simulated data would expand to infinity.\nIf exponential increase in data is detected, error is raised automatically. ***\n')
    print('vandal.montecarlo CALLABLE FUNCTIONS:\n')
    print('.help() - information about the available functions in the vandal.montecarlo module.\n * takes no additional arguments.\n')
    print('.Configuration() - main class that defines the data, desired time sequence and number of simulations.\n * takes 4 additional arguments.\n   list_of_values - pandas dataframe of values.\n   time_seq - desired time sequence.\n   num_sims - desired number of simulation iterations.\n   log_summary (default: log_summary = False) - event log of executed functions.\n * Requirements:\n   pandas Python module\n   pd.DataFrame() function.')

#object that contains the simulation data.
class Configuration:

    #shows detailed overview of available functions. Performing this action will not be tracked in class logs.
    def help():  
        print('vandal.montecarlo.Configuration CALLABLE FUNCTIONS:\n')
        print('.help() - information about the available functions in the class.\n * takes no additional arguments.\n')
        print('.execute() - executes a Monte Carlo simulation on a defined data set.\n * takes 1 optional argument (default: ref_value_index = 0)\n   ref_value_index - index of a reference value as a simulation starting point.\n * Requirements:\n   vandal.montecarlo.Configuration().\n * Limitations:\n If exponential increase in data values is detected, automatically raises error.\n')
        print('.graph() - plots the Monte Carlo simulation on a graph.\n * takes 4 optional customization arguments. (default: graph_title = \'Monte Carlo simulation\', x_title = \'X axis\', y_title = \'Y axis\', plot_size = (25,10).)\n   graph_title - title of the graph\n   x_title - title of the X axis.\n   y_title - title on the Y axis.\n   plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.\n * Requirements:\n   vandal.montecarlo.Configuration.execute().\n')
        print('.get_risk() - calculates the risk of value decrease over time.\n * takes 1 optional argument (default: risk_sims = 5000).\n * Requirements:\n   vandal.montecarlo.Configuration.execute().\n')
        print('.get_stats() - shows the statistics of the Monte Carlo simulation.\n * takes no additional arguments.\n * Requirements:\n   vandal.montecarlo.Configuration.execute().\n')
        print('.get_logs() - shows the event log of executed functions.\n * takes no additional arguments.\n * Requirements:\n   vandal.montecarlo.Configuration.execute().\n   log_summary = True.\n')
        print('.get_change() - shows the percentage of Monte Carlo simulation value change for every iteration.\n * takes no additional arguments.\n * Requirements:\n   vandal.montecarlo.Configuration.execute().\n')
        print('.hist() - plots the histogram of Monte Carlo simulation.\n * takes 5 optional customization arguments. (default: graph_title = \'Monte Carlo simulation\', x_title = \'X axis\', y_title = \'Y axis\', plot_size = (25,10), method = \'b\'.)\nIf method = \'e\' is chosen, no customization arguments apply.\n   graph_title - title of the graph\n   x_title - title of the X axis.\n   y_title - title on the Y axis.\n   plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.\n   method - default method is Basic histogram and it\'s performed by automation. In order to plot Empirical rule histogram add method = \'e\' as the last argument. - NOTE: method of a histogram must be placed within quotation marks.\n * Requirements:\n   vandal.montecarlo.Configuration.execute().\n   vandal.montecarlo.Configuration.get_stats().')

    #initial value configuration.
    def __init__(self, list_of_values, time_seq, num_sims, log_summary = False): 
        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims
        self.log_summary = log_summary
        print(f'Monte Carlo has been set up for {self.num_sims} simulations in a period of {self.time_seq} time measurement units.')

    #creates an event log that tracks the function execution time and duration.
    def classLog(func_name):
        def log(func):
                import time
                import datetime
                def logsaver(self, *args, **kwargs):
                    if self.log_summary == True:
                        start = time.time()
                        results = func(self, *args, **kwargs)
                        with open('vandal Logs.txt', 'a') as f:
                            f.write('Perfomed a function ' + func_name + ' at: ' + str(datetime.datetime.now()) + '.' + ' Time spent performing the action: ' + str(time.time() - start) + ' seconds.' + '\n')
                            return results
                    else:
                            results = func(self, *args, **kwargs)
                            return results
                return logsaver
        return log
        
    #class information.
    @classLog('__str__()')
    def __str__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    #class information.
    @classLog('__repr__()')
    def __repr__(self):
        return f'Monte Carlo defining object that stores the configuration data for creating {self.num_sims} simulations in a period of {self.time_seq} time measurement units.'

    #executes a Monte Carlo simulation on a defined data set.
    @classLog('execute()')
    def execute(self, ref_value_index = 0):
            print('Monte Carlo simulation has been executed')
            print('NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.\nThe model that will be able to handle big standard deviations is currently being worked on, thank you for your patience.\n')
            import pandas as pd
            #This removes pandas warning of highly fragmented DataFrame for newer pandas versions.
            from warnings import simplefilter
            simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
            #End of pandas warning removal block.
            self.ref_value_index = ref_value_index
            today_value = self.list_of_values.iloc[ref_value_index]
            data = pd.DataFrame()
            loading = 0

            for num_sim in range(self.num_sims):
                rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                count = 0
                index_array = []
                simulated_index = today_value * (1 + rand_change)
                index_array.append(simulated_index)
                
                if simulated_index > (index_array[-1] * 2):
                    raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation cannot be executed properly.')
                        
                for num_day in range(self.time_seq):
                    
                    rand_change = random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                    if count == self.time_seq:
                        break
                    simulated_index = index_array[count] * (1 + rand_change)
                    index_array.append(simulated_index)
                    count += 1

                    if simulated_index > (index_array[-1] * 2):
                        raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation function cannot be executed properly.')
                
                loading +=1
                print(end='\r')
                print(loading, 'iterations out of', self.num_sims, 'executed so far', end = '')
                
                data[num_sim] = index_array
            print(end='\r')
            print('Monte Carlo simulation set up and ready to plot.')
            self.results = data
            return data

    #shows the percentage of Monte Carlo simulation value change for every iteration.
    @classLog('get_change()')
    def get_change(self):
        return self.results.pct_change()
   
    #calculates the risk of negative values occuring.
    @classLog('get_risk()')
    def get_risk(self, risk_sims = 5000):
        import random
        import pandas as pd
        #This removes pandas warning of highly fragmented DataFrame for newer pandas versions.
        from warnings import simplefilter
        simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
        #End of pandas warning removal block.
        today_value = self.list_of_values.iloc[self.ref_value_index]
        percent_change = self.list_of_values.pct_change()
        data = pd.DataFrame()
        smaller = []

        for num_sim in range(risk_sims): 
            random_change = random.choice(percent_change)
            index_array = []

            simulated_index = today_value * (1 + (random_change))
            index_array.append(simulated_index)
            data[num_sim] = index_array

            for sim in data[num_sim]:
                if sim < today_value:
                    smaller.append(sim)
        NRisk = len(smaller) / num_sim * 100

        assert (NRisk < 100), 'Time sequence and/or number of iterations are too low for the proper risk calculation.'

        print('Risk for this option is', round(NRisk,2), '%.')
     
    #plots the Monte Carlo simulation on a graph.   
    @classLog('graph()')
    def graph(self, graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10)):
        print('MonteCarlo() plotting initialized.')
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('vandal (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')
        plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
        plt.plot(self.results)
        plt.axhline(y = self.results[0][0], color = 'k', linestyle = 'solid')
        plt.xlabel(x_title, fontsize = 18, weight = 'semibold')
        plt.ylabel(y_title, fontsize = 18, weight = 'semibold')
        plt.show()
        print('MonteCarlo() plotting finished.')
   
    #shows the statistics of the Monte Carlo simulation.
    @classLog('get_stats()')
    def get_stats(self): 
        import numpy as np
        print('Number of simulations: ', self.time_seq)
        print('Number of iterations: ', self.num_sims)
        mean_value = np.mean(self.results.loc[self.time_seq])
        mean_value = round((mean_value),2)
        print('Mean value: ', mean_value)
        standard_deviation = round(np.std(self.results.loc[self.time_seq]),2)
        standard_deviation = round((standard_deviation),2)
        print('Standard deviation: ', standard_deviation)
        maximum_value = np.max(self.results.loc[self.time_seq])
        maximum_value = round((maximum_value),2)
        print('Maximum: ', maximum_value)
        minimum_value = np.min(self.results.loc[self.time_seq])
        minimum_value = round((minimum_value),2)
        print('Minimum: ', minimum_value)
        self.standard_deviation = standard_deviation
        self.mean_value = mean_value

    #plots the histogram of Monte Carlo simulation.
    @classLog('hist()')
    def hist(self, graph_title = 'Histogram of value frequencies', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), **method):
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
        plt.show()
        print('Histogram plotting finished.')

    @classLog('get_logs()')
    def get_logs(self):
        f = open('vandal Logs.txt', 'r')
        print(f.read())