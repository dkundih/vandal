import pandas as pd
from colorama import Fore
import colorama
import os
import duality

colorama.init()

df = pd.read_excel(r'C:\Users\kundi\Sphere\vandal\DBCLI\testbase.xlsx')

df.set_index(df['JMBAG'], inplace = True)
df.drop(columns = 'JMBAG', inplace = True)

def get_name(request):
	return df.loc[request]['IME']

def get_surname(request):
	return df.loc[request]['PREZIME']

def get_department(request):
	return df.loc[request]['ODJEL']

def get_course(request):
	return df.loc[request]['STUDIJ']

def get_project(request):
	return df.loc[request]['SEMINAR']

def get_date(request):
	return df.loc[request]['DATUM']

def jmbag_info(jmbag):
	return df.loc[jmbag]

def criteria_search(column, key):
	return df[df[column] == key]

def menu():
	print(Fore.GREEN + 'RASPOLOŽIVE OPCIJE', Fore.RESET)
	print('1 | Informacije')
	print('2 | Liste')
	print('3 | Izlaz')

def sort_dates(argument):
	argument = argument.to_list()
	datelist = []
	for date in argument:
		datelist += [date[:-1]]
	datelist = duality.auto_sort(datelist, '.', trigger = lambda x: [x[2], x[1], x[0]])
	return datelist

def CLI():
	while True:
		os.system('cls')
		menu()
		print('')
		choice = input('Unesi broj željene opcije: ')
		if choice == '1':
			informacije()
		elif choice == '2':
			liste()
		elif choice == '3':
			print(Fore.RED + 'Izlazim iz aplikacije', Fore.RESET)
			break
		else:
			print(Fore.RED + 'Nevaljan odabir, pokušajte ponovno.', Fore.RESET)
			print('')
		
def informacije():
	identification = int(input('UNESI JMBAG: '))
	while True:
		print(Fore.GREEN + 'OPCIJE: ime, prezime, odjel, studij, seminar, datum, izlaz', Fore.RESET)
		print('')
		action = input('Unesi opciju: ')
		if action == 'ime':
			print(get_name(request = identification))
			print('')
		if action == 'prezime':
			print(get_surname(request = identification))
			print('')
		if action == 'odjel':
			print(get_department(request = identification))
			print('')
		if action == 'studij':
			print(get_course(request = identification))
			print('')
		if action == 'seminar':
			print(get_project(request = identification))
			print('')
		if action == 'datum':
			print(get_date(request = identification))
			print('')
		if action == 'izlaz':
			print('Izlazim...')
			break

def liste():
	while True:
		print(Fore.GREEN + 'OPCIJE: jmbaginfo, baza, sorting, kriterij, izlaz', Fore.RESET)
		print('')
		action = input('Unesi opciju: ')
		if action == 'jmbaginfo':
			jmbag_input = int(input('Unesi jmbag: '))
			print(jmbag_info(jmbag = jmbag_input))
			print('')
		if action == 'baza':
			print(df)
		if action == 'sorting':
			print(sort_dates(df['DATUM']))
			print('')
		if action == 'kriterij':
			print('RASPOLOŽIVI KRITERIJI')
			for col in df.columns:
				print(col)
			print('')
			column = input('Unesi kriterij: ')
			column = column.upper()
			key = input('Unesi traženi pojam: ')
			print(criteria_search(column = column, key = key))
			print('')
		if action == 'izlaz':
			print(Fore.RED + 'Izlazim...', Fore.RESET)
			break

if __name__ == '__main__':
	CLI()