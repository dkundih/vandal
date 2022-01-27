# imports all relevant contents.
import vandal
from vandal.objects import montecarlo
from colorama import Fore
import colorama

colorama.init()

# runs the main CLI client that leads to individual apps.
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--entry', help = 'Enter options', type = str,
    choices = ['montecarlo'])
    args = parser.parse_args()

    if args.entry == 'montecarlo':
        print(Fore.GREEN + '=== ENTERING MONTECARLO CLIENT... ===\n', Fore.RESET)
        vandal.objects.montecarlo.MCapp()
