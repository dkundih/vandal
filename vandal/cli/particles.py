# dependency imports.
import colorama, traceback
from colorama import Fore
import os

# initiates coloring.
colorama.init()

# vandal version.
from vandal.misc._meta import __version__

# vandalCLI version.
__CLIversion__ = 'v1.25'

# intro to the client.
def greet():
    print(Fore.GREEN + '\n - vandal Command Line Interface © David Kundih -', __CLIversion__)
    print(Fore.GREEN + ' - vandal package version - ', __version__, Fore.RESET)

# menu.
def menu():
    print('-----------------------------')
    print(Fore.CYAN + 'AVAILABLE FEATURES', Fore.RESET)
    print(' 1 | Monte Carlo simulation')
    print(' 2 | Dijkstra algorithm')
    print(' 3 | Economic Order Quantity')
    print(' 4 | Exit')
    print('-----------------------------')

# main client.
def App():

    '''
    (FUNCTION INFO)
    ---------------
    vandal.App - main client that serves as an access to other module clients.
    '''

    while True:
        os.system('cls')
        greet()
        menu()
        choice = input('Choose an option: ')
        if choice == '1':
            print(Fore.GREEN + '=== ENTERING MONTECARLO CLIENT... ===\n', Fore.RESET)
            MonteCarloCLI()
        elif choice == '2':
            print(Fore.GREEN + '=== ENTERING DIJKSTRA CLIENT... ===\n', Fore.RESET)
            DijkstraCLI()
        elif choice == '3':
            print(Fore.GREEN + '=== ENTERING EOQ CLIENT... ===\n', Fore.RESET)
            EOQCLI()
        elif choice == '4':
            print(Fore.GREEN + 'Exiting...', Fore.RESET)
            break
        else:
            print(Fore.RED + '=== OPTION NOT EXISTENT OR AVAILABLE, PLEASE WRITE THE EXISTING NUMBER FROM THE MENU TO CONTINUE. ===', Fore.RESET)

# MonteCarlo client extension.
def MonteCarloCLI():

    '''
    (FUNCTION INFO)
    ---------------
    vandal.MonteCarloCLI - MonteCarlo client extension.
    '''

    from vandal.objects import MonteCarlo
    import pandas as pd
    file = input('File path: ').replace("'", '"').strip('"')
    if str(file).endswith('.csv'):
        data = pd.read_csv(file)
        print(Fore.CYAN + 'AVAILABLE COLUMNS: ', Fore.RESET)
        for col in data.columns:
            print(col)
    elif str(file).endswith('.xlsx'):
        data = pd.read_excel(file)
        print(Fore.CYAN + 'AVAILABLE COLUMNS: ', Fore.RESET)
        for col in data.columns:
            print(col)
    elif str(file).endswith('.json'):
        data = pd.read_json(file)
        print(Fore.CYAN + 'AVAILABLE COLUMNS: ', Fore.RESET)
        for col in data.columns:
            print(col)
    else:
        raise Exception('=== ONLY CSV, XLSX AND JSON FILES SUPPORTED. ===\n')
    file_col = input('\nEnter column name: ').replace("'", '"').strip('"')
    try:
        data = data[file_col]
    except:
        raise Exception('=== INVALID COLUMN NAME. ===\n')
    MC = MonteCarlo()
    simulations = int(input('Enter number of simulations: ') or 100)
    period = int(input('Enter desired period: ') or 50)
    executed = MC.execute(list_of_values = data, num_sims = simulations, time_seq = period)
    while True:
        action = input('ACTIONS: graph, change, values, stats, risk, hist, home, help: ')
        if action == 'graph':
            title = input('Title: ')
            x_axis = input('X axis title:')
            y_axis = input('Y axis title:')
            MC.graph(graph_title = title, x_title = x_axis, y_title = y_axis)
        if action == 'change':
            print('1 | csv')
            print('2 | xlsx')
            print('3 | json')
            file_type = input('\nEnter the number or name of file type:')
            output = MC.get_change()
            try:
                save_to(output, 'change', choice = file_type)
            except:
                raise Exception('=== UNABLE TO SAVE, PLEASE SELECT ONE OF THE OPTIONS AND/OR RUN THE TERMINAL AS AN ADMINISTRATOR. ===\n')
        if action == 'values':
            print('1 | csv')
            print('2 | xlsx')
            print('3 | json')
            file_type = input('\nEnter the number or name of file type:')
            try:
                save_to(executed, 'values', choice = file_type)
            except:
                raise Exception('=== UNABLE TO SAVE, PLEASE RUN THE TERMINAL AS AN ADMINISTRATOR. ===\n')
        if action == 'stats' or action == 'statistics':
            MC.get_stats()
        if action == 'risk':
            sample = int(input('Number of iterations to measure risk on: ') or 5000)
            MC.get_risk(risk_sims = sample)
        if action == 'hist' or action == 'histogram':
            x_axis = input('X axis title:')
            y_axis = input('Y axis title:')
            print('1 | Basic Histogram')
            print('2 | Empirical Rule Histogram')
            method = input('Enter histogram method: ')
            if method == '1':
                MC.hist(x_title = x_axis, y_title = y_axis)
            elif method == '2':
                MC.hist(x_title = x_axis, y_title = y_axis, method = 'e')
            else:
                print(Fore.RED + '=== INVALID METHOD. ===\n', Fore.RESET)
        if action == 'home':
            break
        if action == 'help':
            print(Fore.YELLOW + 'https://github.com/dkundih/vandal\n', Fore.RESET)

# save helper for cleaner code.
def save_to(file, func_name, choice):
    import pandas as pd
    import os
    if choice == '1' or choice == 'csv':
        extension = '.csv'
        file.to_csv('vandal.MonteCarlo - ' + func_name + extension)
        print(os.path.join(os.getcwd() + '\vandal.MonteCarlo - ' + func_name + extension))
    elif choice == '2' or choice == 'xlsx':
        extension = '.xlsx'
        file.to_excel('vandal.MonteCarlo - ' + func_name + extension)
        print(os.path.join(os.getcwd() + '\vandal.MonteCarlo - ' + func_name + extension))
    elif choice == '3' or choice == 'json':
        extension = '.json'
        file.to_json('vandal.MonteCarlo - ' + func_name + extension)
        print(os.path.join(os.getcwd() + '\vandal.MonteCarlo - ' + func_name + extension))
    else:
        print(Fore.RED + '=== NO OPTION CHOSEN, EXITING THE MENU... =\n', Fore.RESET)

# Dijkstra client extension.
def DijkstraCLI():

    '''
    (FUNCTION INFO)
    ---------------
    vandal.DijkstraCLI - Dijkstra client extension.
    '''

    from vandal.objects import Dijkstra
    while True:
        action = input('ACTIONS: home, help: ')
        if action == 'home':
            break
        if action == 'help':
            print(Fore.YELLOW + 'https://github.com/dkundih/vandal\n', Fore.RESET)

# EOQ client extension.
def EOQCLI():

    '''
    (FUNCTION INFO)
    ---------------
    vandal.EOQCLI - EOQ client extension.
    '''

    from vandal.objects import EOQ
    while True:
        action = input('ACTIONS: home, help: ')
        if action == 'home':
            break
        if action == 'help':
            print(Fore.YELLOW + 'https://github.com/dkundih/vandal\n', Fore.RESET)

# runs client.
if __name__ == '__main__':
    App()
