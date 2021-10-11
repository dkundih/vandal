#main functions
def help():
        print('vandal CALLABLE FUNCTIONS:\n')
        print('.essence() - main hub of data manipulation functions.\n')
        print('.montecarlo() - defines the parameters of MonteCarlo simulation.\n * takes 3 additional arguments.\n   list_of_values - pandas dataframe of values.\n   time_seq - desired time sequence.\n   num_sims - desired number of simulation iterations.\n * Requirements:\n   pandas Python module\n   pd.DataFrame() function.\n')
        print('.eoq() - defines the parameters of EOQ analysis.\n * takes 3 additional arguments.\n   list_of_values - pandas dataframe of values.\n   time_seq - desired time sequence.\n   num_sims - desired number of simulation iterations.\n * Requirements:\n   pandas Python module\n   pd.DataFrame() function.\n')
        print('--- MISCELLANEOUS ---\n')
        print('.help() - information about the available functions in the module.\n * takes no additional arguments.\n')
        print('.license() - shows the licence and terms of use.\n * takes no additional arguments.\n')
        print('.donate() - shows the donation link.\n * takes no additional arguments.\n')
        print('.contact() - shows the contact information.\n * takes no additional arguments.\n')
        print('.documentation() - shows the documentation link.\n * takes no additional arguments.\n')
        print('.main() - general setup confirmation.')

#MISCELLANEOUS LOGISTICS FUNCTIONS

#shows the license.
def license():
        print('Copyright (c) 2021- David Kundih. All rights reserved.\nLicensed under the Apache License, Version 2.0.\n\nFor more details about the license and terms of use visit the official vandal documentation linked at https://github.com/dkundih/vandal and https://pypi.org/project/vandal')

#shows the documentation.
def documentation():
        print('https://github.com/dkundih/vandal\nhttps://pypi.org/project/vandal')

#shows the donation options.
def donate():
        print('https://patreon.com/dkundih\nhttps://buymeacoffee.com/dkundih')

#shows the contact information.
def contact():
        print('dakundih@unin.hr\nkundihdavid@gmail.com')
    
#general setup confirmation.
def main():
    print('Setup successful.')

if __name__ == '__main__':
        main()