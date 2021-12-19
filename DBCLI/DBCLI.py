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

#WIP
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
	print('Raspoloživi JMBAG:')
	for i in df.index:
		print(i)
	print('')
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
		print(Fore.GREEN + 'OPCIJE: jmbaginfo, baza, kriterij, dodaj, izbriši, izlaz', Fore.RESET)
		print('')
		action = input('Unesi opciju: ')
		if action == 'jmbaginfo':
			print('Raspoloživi JMBAG:')
			for i in df.index:
				print(i)
			print('')
			jmbag_input = int(input('Unesi jmbag: '))
			print(jmbag_info(jmbag = jmbag_input))
			print('')
		if action == 'baza':
			print(df)
		if action == 'kriterij':
			print(Fore.GREEN + 'RASPOLOŽIVI KRITERIJI', Fore.RESET)
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
		if action == 'dodaj':
			new_user = []
			new_jmbag = int(input('Unesi JMBAG novog korisnika: '))
			for col in df.columns:
				new_input = input(f'Unesi {col}: ')
				new_user.append(new_input)
			df.loc[new_jmbag] = new_user
			print(Fore.GREEN + 'SPREMI SLJEDEĆI UNOS?', Fore.RESET)
			print(df.loc[new_jmbag])
			answer = input('Unesi 0 za otkazivanje, 1 za spremanje unosa: ')
			if answer == '1':
				df.to_excel('testbase.xlsx')
				print(Fore.GREEN + 'Spremljeno.', Fore.RESET)
				break
		if action == 'izbriši':
			print(df)
			deleted_user = int(input('Unesi JMBAG korisnika kojeg želiš izbrisati: '))
			answer = input('Unesi 0 za otkazivanje, 1 za spremanje unosa: ')
			if answer == '1':
				df.drop(index = deleted_user, inplace = True)
				df.to_excel('testbase.xlsx')
				print(Fore.GREEN + 'Spremljeno.', Fore.RESET)
				break

if __name__ == '__main__':
	CLI()
