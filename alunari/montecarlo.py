#imports essential functions from the alunari module.
from alunari import essence
from alunari.global_functions import *

def help():  
    print('*** NOTE: alunari.montecarlo works only for sequential data with reasonable standard deviation, otherwise simulated data would expand to infinity.\nIf exponential increase in data is detected, error is raised automatically. ***\n')
    print('alunari.montecarlo CALLABLE FUNCTIONS:\n')
    print('.help() - information about the available functions in the alunari.montecarlo module.\n * takes no additional arguments.\n')
    print('.Configuration() - main class that defines the data, desired time sequence and number of simulations.\n * takes 3 additional arguments.\n   list_of_values - pandas dataframe of values.\n   time_seq - desired time sequence.\n   num_sims - desired number of simulation iterations.\n * Requirements:\n   pandas Python module\n   pd.DataFrame() function.')

#object that contains the simulation data.
class Configuration:
    
    #initial value configuration.
    def __init__(self, list_of_values, time_seq, num_sims): 
        self.list_of_values = list_of_values
        self.time_seq = time_seq
        self.num_sims = num_sims

    #class information.
    def __str__(self):
        return f'This is a Monte Carlo defining function that performs {self.num_sims} simulations over the defined data in a time period of {self.time_seq}.'

    #class information.
    def __repr__(self):
        return f'This is a Monte Carlo defining function that performs {self.num_sims} simulations over the defined data in a time period of {self.time_seq}.'
        
    #information about the available functions in the module.
    def help():  
        print('alunari.montecarlo.Configuration CALLABLE FUNCTIONS:\n')
        print('.help() - information about the available functions in the class.\n * takes no additional arguments.\n')
        print('.execute() - executes a Monte Carlo simulation on a defined data set.\n * takes 1 optional argument (default: ref_value_index = 0)\n   ref_value_index - index of a reference value as a simulation starting point.\n * Requirements:\n   alunari.montecarlo.Configuration().\n * Limitations:\n If exponential increase in data values is detected, automatically raises error.\n')
        print('.graph() - plots the Monte Carlo simulation on a graph.\n * takes 4 optional customization arguments. (default: graph_title = \'Monte Carlo simulation\', x_title = \'X axis\', y_title = \'Y axis\', plot_size = (25,10).)\n   graph_title - title of the graph\n   x_title - title of the X axis.\n   y_title - title on the Y axis.\n   plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.\n * Requirements:\n   alunari.montecarlo.Configuration.execute().\n')
        print('.get_risk() - calculates the risk of negative values occuring.\n * takes no additional arguments.\n * Requirements:\n   alunari.montecarlo.Configuration.execute().\n')
        print('.get_stats() - shows the statistics of the Monte Carlo simulation.\n * takes no additional arguments.\n * Requirements:\n   alunari.montecarlo.Configuration.execute().\n')
        print('.get_change() - shows the percentage of Monte Carlo simulation value change for every iteration.\n * takes no additional arguments.\n * Requirements:\n   alunari.montecarlo.Configuration.execute().\n')
        print('.hist() - plots the histogram of Monte Carlo simulation.\n * takes 5 optional customization arguments. (default: graph_title = \'Monte Carlo simulation\', x_title = \'X axis\', y_title = \'Y axis\', plot_size = (25,10), method = \'b\'.)\nIf method = \'e\' is chosen, no customization arguments apply.\n   graph_title - title of the graph\n   x_title - title of the X axis.\n   y_title - title on the Y axis.\n   plot_size - desired size of the graph. eg. - (x_lenght_num, y_lenght_num). - NOTE: values must be inside the parentheses and divided by a comma.\n   method - default method is Basic histogram and it\'s performed by automation. In order to plot Empirical rule histogram add method = \'e\' as the last argument. - NOTE: method of a histogram must be placed within quotation marks.\n * Requirements:\n   alunari.montecarlo.Configuration.execute().\n   alunari.montecarlo.Configuration.get_stats().')

    #executes a Monte Carlo simulation on a defined data set.
    def execute(self, ref_value_index = 0):
            print('Monte Carlo simulation has been executed')
            print('NOTE: Use data with reasonable standard deviation in order to prevent exponential growth of the function that cannot be plotted properly, recognize such abnormal values by a + sign anywhere in the data executed below.\nThe model that will be able to handle big standard deviations is currently being worked on, thank you for your patience.\n')
            import pandas as pd
            self.ref_value_index = ref_value_index
            today_value = self.list_of_values.iloc[ref_value_index]
            data = pd.DataFrame()
            loading = 0

            for num_sim in range(self.num_sims):
                rand_change = essence.random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
                count = 0
                index_array = []
                simulated_index = today_value * (1 + rand_change)
                index_array.append(simulated_index)
                
                if simulated_index > (index_array[-1] * 2):
                    raise Exception('Variation between data is too big, due to detection of exponentional increase of values or non-sequential data Monte Carlo simulation cannot be executed properly.')
                        
                for num_day in range(self.time_seq):
                    
                    rand_change = essence.random_value(self.list_of_values.pct_change().mean(), self.list_of_values.pct_change().std())
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
    def get_change(self):
        return self.results.pct_change()
   
    #calculates the risk of negative values occuring.
    def get_risk(self):
        import pandas as pd
        import random
        today_value = self.list_of_values.iloc[self.ref_value_index]
        percent_change = self.list_of_values.pct_change()
        data = pd.DataFrame()
        smaller = []

        for num_sim in range(self.time_seq): 
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
    def graph(self, graph_title = 'Monte Carlo simulation', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10)):
        print('MonteCarlo() plotting initialized.')
        import matplotlib.pyplot as plt
        plt.figure(figsize = plot_size)
        plt.title('alunari (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')
        plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
        plt.plot(self.results)
        plt.axhline(y = self.results[0][0], color = 'k', linestyle = 'solid')
        plt.xlabel(x_title, fontsize = 18, weight = 'semibold')
        plt.ylabel(y_title, fontsize = 18, weight = 'semibold')
        plt.show()
        print('MonteCarlo() plotting finished.')
   
    #shows the statistics of the Monte Carlo simulation.
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
    def hist(self, graph_title = 'Histogram of value frequencies', x_title = 'X axis', y_title = 'Y axis', plot_size = (25,10), **method):
        std_plus = self.mean_value + self.standard_deviation
        std_minus = self.mean_value - self.standard_deviation
        std_plus2 = self.mean_value + (self.standard_deviation * 2)
        std_minus2 = self.mean_value - (self.standard_deviation * 2)
        std_plus3 = self.mean_value + (self.standard_deviation * 3)
        std_minus3 = self.mean_value - (self.standard_deviation * 3)

        if self.time_seq > 50:
            print('NOTE: Time sequence defined greatly impacts the lenght of histogram plotting.\n')

        if method.get("method") == "e":
            print('CHOSEN METHOD: Empirical rule.')   
            print('Histogram plotting initiated...')
            import matplotlib.pyplot as plt
            plt.figure(figsize = plot_size)
            plt.title('alunari (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')
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

        else:
            print('CHOSEN METHOD: Basic histogram model.')
            print('Histogram plotting initiated...')
            import matplotlib.pyplot as plt
            plt.figure(figsize = plot_size)
            plt.title('alunari (c) David Kundih, 2021.', fontsize = 14, weight = 'regular', loc = 'right')
            plt.suptitle(graph_title, fontsize = 25, weight = 'bold')
            plt.hist(self.results, bins = self.time_seq , ec = 'm')
            plt.xlabel(x_title, weight = 'semibold')
            plt.ylabel(y_title, weight= 'semibold')
            plt.show()
            print('Histogram plotting finished.')

#general setup confirmation.
def main():
    print('Setup successful.')

if __name__ == '__main__':
        main()