from alunari.misc.global_functions import *

#shows detailed overview of available functions.
def help():  
    print('alunari.eoq CALLABLE FUNCTIONS:\n')
    print('.help() - information about the available functions in the alunari.montecarlo module.\n * takes no additional arguments.\n')
    print('.Configuration() - main class that defines the data, desired time sequence and number of simulations.\n * takes 3 additional arguments.\n   list_of_values - pandas dataframe of values.\n   time_seq - desired time sequence.\n   num_sims - desired number of simulation iterations.\n * Requirements:\n   pandas Python module\n   pd.DataFrame() function.')
