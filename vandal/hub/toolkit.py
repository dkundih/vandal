# coloring.
from colorama import Fore, init

init()

'''

(MODULE FUNCTIONS)
------------------

vandal.toolkit is a set of data manipulation tools that can be directly accessed from the main module as vandal.any_function_listed_below()

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

        file_handler(file) - handles the file extenstion upon import.
	
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
	__donate__
)

# gives a random value of mean and standard deviation inputed, if rounded = 'y', value will be rounded.
def random_value(mean, st_dev, **rounded):
        import random
        if rounded.get('rounded') == 'y':
                random_value = round(random.gauss(mean, st_dev))
        else:
                random_value = random.gauss(mean, st_dev)
        return random_value

# gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = 'y', values will be rounded.
def random_pool(mean, st_dev, pool_size, **rounded):
        import random
        if rounded.get('rounded') == 'y':
                random_pool = [round(random.gauss(mean, st_dev)) for y in range(pool_size)]
        else:
                random_pool = [random.gauss(mean, st_dev) for y in range(pool_size)]
        return random_pool

# splits the data using a split method character.
def split_values(data, split_method):
        split_values = []
        for i in data:
                split_values += [i.split(split_method)]
        return split_values

# joins the data using a join metod character.
def join_values(data, join_method):
        join_values = []
        for i in data:
                join_values += [join_method.join(i)]
        return join_values

# replaces a defined value with a desired value.
def replace_values(data, replaced_value, replacing_value):
        replaced_values = []
        for i in data:
                replaced_values += [i.split(replaced_value)]
        replace_values = []
        for i in replaced_values:
                replace_values += [replacing_value.join(i)]
        return replace_values

# manually sorts data depending on defined array of indexes.
def list_sort(data, array):
        redefined_data = []
        for d in array:
                redefined_data += [data[d]]
        return redefined_data

# sorts the indicies in a list of values based on the index array defined as [x,x,x].
def index_sort(data, split_method, index_array):
        result = []
        remixed_data = []
        array_count = 0
        for i in data:
                result += [i.split(split_method)]
        array_lenght = len(result)
        for i in result:
                y1 = [i[x] for x in index_array]
                remixed_data += [split_method.join(y1)]
                if array_count == array_lenght:
                        break
                array_count += 1
        return remixed_data

# automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.
def auto_sort(data, split_method, trigger = lambda x: x[0]):
        split_values = []
        merged_final = []
        for i in data:
                split_values += [i.split(split_method)]
        auto_sort = sorted(split_values, key = trigger)
        for i in auto_sort:
                merged_final += ['-'.join(i)]
        return merged_final

# creates a random password with adjustable lenght (default: length = 8).
def create_password(length = 8):
        import random
        particles = 'abcdefghijklmnoprstuxwyzqABCDEFGHIJKLMNOPRSTUXWYZQ0123456789'
        return ''.join(random.sample(particles, length))

# handles the file extenstion upon import.
def file_handler(file):
        import pandas as pd
        file = file.replace("'", '"').strip('"')
        if str(file).endswith('.csv'):
            data = pd.read_csv(file)
            print(Fore.YELLOW + '\nAVAILABLE COLUMNS' + Fore.RESET)
            for col in data.columns:
                print(col)
        elif str(file).endswith('.xlsx'):
            data = pd.read_excel(file)
            print(Fore.YELLOW + '\nAVAILABLE COLUMNS' + Fore.RESET)
            for col in data.columns:
                print(col)
        elif str(file).endswith('.json'):
            data = pd.read_json(file)
            print(Fore.YELLOW + '\nAVAILABLE COLUMNS' + Fore.RESET)
            for col in data.columns:
                print(col)
        else:
            raise Exception('=== ONLY CSV, XLSX AND JSON FILES SUPPORTED. ===\n')
        file_col = input('\nEnter column name: ').replace("'", '"').strip('"')
        try:
            data = data[file_col]
            return data
        except:
            raise Exception('=== INVALID COLUMN NAME. ===\n')

# file saver for code clarity.
def save_to(file, prefix, func_name, choice):
        import pandas as pd
        import os
        if choice == '0' or choice == 'csv':
                extension = '.csv'
                file.to_csv(prefix + func_name + extension)
                print(Fore.YELLOW + os.path.join(os.getcwd() + '\\' + prefix + func_name + extension) + Fore.RESET)
        elif choice == '1' or choice == 'xlsx':
                extension = '.xlsx'
                file.to_excel(prefix + func_name + extension)
                print(Fore.YELLOW + os.path.join(os.getcwd() + '\\' + prefix + func_name + extension) + Fore.RESET)
        elif choice == '2' or choice == 'json':
                extension = '.json'
                file.to_json(prefix + func_name + extension)
                print(Fore.YELLOW + os.path.join(os.getcwd() + '\\' + prefix + func_name + extension) + Fore.RESET)
        else:
                print('=== NO OPTION CHOSEN, EXITING THE MENU... =\n')
