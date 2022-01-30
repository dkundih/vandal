# imports all relevant contents.
import vandal
from vandal.objects import montecarlo

# coloring.
import colorama
from colorama import Fore, init

init()

# runs the main CLI client that leads to individual apps.
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--entry', help = 'start Monte Carlo application.', type = str,
    choices = ['montecarlo'])
    args = parser.parse_args()

    if args.entry == 'montecarlo':
        print(Fore.YELLOW + '=== ENTERING MONTECARLO CLIENT... ===\n', Fore.RESET)
        vandal.objects.montecarlo.MCapp()
