from vandal.misc.global_functions import *

#gives a random value of mean and standard deviation inputed, if rounded = 'y', value will be rounded.
def random_value(mean, st_dev, **rounded):
        import random
        if rounded.get('rounded') == 'y':
                random_value = round(random.gauss(mean, st_dev))
        else:
                random_value = random.gauss(mean, st_dev)
        return random_value

#gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = 'y', values will be rounded.
def random_pool(mean, st_dev, pool_size, **rounded):
        import random
        if rounded.get('rounded') == 'y':
                random_pool = [round(random.gauss(mean, st_dev)) for y in range(pool_size)]
        else:
                random_pool = [random.gauss(mean, st_dev) for y in range(pool_size)]
        return random_pool

#splits the data using a split method character.
def split_values(data, split_method):
        split_values = []
        for i in data:
                i = i.split(split_method)
                split_values.append(i)
        return split_values

#joins the data using a join metod character.
def join_values(data, join_method):
        join_values = []
        for i in data:
                i = join_method.join(i)
                join_values.append(i)
        return join_values

#replaces a defined value with a desired value.
def replace_values(data, replaced_value, replacing_value):
        replaced_values = []
        for i in data:
                i = i.split(replaced_value)
                replaced_values.append(i)
        replace_values = []
        for i in replaced_values:
                i = replacing_value.join(i)
                replace_values.append(i)
        return replace_values

#manually sorts data depending on defined array of indexes.
def list_sort(data, array):
        redefined_data = []
        for d in array:
                t = data[d]
                redefined_data.append(t)
        return redefined_data

#sorts the indicies in a list of values based on the index array defined as [x,x,x].
def index_sort(data, split_method, index_array):
        result = []
        remixed_data = []
        array_count = 0
        for i in data:
                n = i.split(split_method)
                result.append(n)
        array_lenght = len(result)
        for i in result:
                y1 = [i[x] for x in index_array]
                y2 = split_method.join(y1)
                remixed_data.append(y2)
                if array_count == array_lenght:
                        break
                array_count += 1
        return remixed_data

#automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.
def auto_sort(data, split_method, trigger = lambda x: x[0]):
        split_values = []
        merged_final = []
        for i in data:
                i = i.split(split_method)
                split_values.append(i)
        auto_sort = sorted(split_values, key= trigger)
        for i in auto_sort:
                d = '-'.join(i)
                merged_final.append(d)
        return merged_final

#shows detailed overview of available functions.
def help():
        print('vandal.essence CALLABLE FUNCTIONS:\n')
        print('.help() - shows available functions in the module.\n')
        print('.random_value(mean, st_dev, **rounded) - gives a random value of mean and standard deviation inputed, if rounded = \'y\', value will be rounded.\n')
        print('.random_pool(mean, st_dev, pool_size, **rounded) - gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = \'y\', values will be rounded.\n')
        print('.split_values(data, split_method) - splits the data using a split method character.\n')
        print('.join_values(data, join_method) - joins the data using a join metod character.\n')
        print('.replace_values(data, replaced_value, replacing_value) - replaces a defined value with a desired value.\n')
        print('.list_sort(data, array) - manually sorts data depending on defined array of indexes.\n')
        print('.index_sort(data, split_method, index_array) - sorts the indicies in a list of values based on the index array defined as [x,x,x].\n')
        print('.auto_sort(data, split_method, trigger = lambda x: x[0]) - automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.')
