#imports essential functions from the vandal module.
from vandal.misc.global_functions import *

#shows detailed overview of available functions.
def help():  
    print('vandal.eoq CALLABLE FUNCTIONS:\n')
    print('.help() - information about the available functions in the vandal.eoq module.\n * takes no additional arguments.\n')
    print('.Configuration() - main class that defines the data needed for the calculation.\n * takes 4 additional arguments.\n   annual_demand_quantity - integer of demanded quantity in a year.\n   order_fixed_cost - integer or float presenting the fixed cost of the order.\n   annual_holding_cost - cost of holding the goods in a year.\n   log_summary (default: log_summary = False) - event log of executed functions.')

#object that contains the calculation data.
class Configuration:

    #shows detailed overview of available functions. Performing this action will not be tracked in class logs.
    def help():
        print('vandal.eoq.Configuration CALLABLE FUNCTIONS:\n')
        print('.help() - information about the available functions in the vandal.eoq.Configuration class.\n * takes no additional arguments.\n')
        print('.execute() - executes the calculation of EOQ over the defined parameters.\n * takes no additional arguments.\n')
        print('.get_logs() - shows the event log of executed functions.\n * takes no additional arguments.\n * Requirements:\n   vandal.eoq.Configuration.execute().\n   log_summary = True.\n')
 
    #initial value configuration.
    def __init__(self, annual_demand_quantity, order_fixed_cost, annual_holding_cost, log_summary = False):
        self.annual_demand_quantity = annual_demand_quantity
        self.order_fixed_cost = order_fixed_cost
        self.annual_holding_cost = annual_holding_cost
        self.log_summary = log_summary
        print(f'EOQ has been set up with annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.')

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
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    #class information.
    @classLog('__repr__()')
    def __repr__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    #executes the calculation of EOQ over the defined parameters.
    @classLog('execute()')
    def execute(self):
        import math 
        eoq = math.sqrt((((2 * self.annual_demand_quantity) * self.order_fixed_cost) / self.annual_holding_cost))
        return eoq

    @classLog('get_logs()')
    def get_logs(self):
        f = open('vandal Logs.txt', 'r')
        print(f.read())