# imports all relevant contents.
import vandal
from vandal.objects import (
    montecarlo,
    eoq,
)

# imports plugins.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# coloring.
from colorama import Fore, init

init()

# runs the main CLI client that leads to individual apps.
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--entry', help = 'start the desired application.', type = str,
    choices = ['montecarlo', 'eoq'])
    args = parser.parse_args()

    if args.entry == 'montecarlo':
        print(Fore.YELLOW + '=== ENTERING MONTECARLO CLIENT... ===\n', Fore.RESET)
        vandal.objects.montecarlo.MCapp()
    elif args.entry == 'eoq':
        print(Fore.YELLOW + '=== ENTERING ECONOMIC ORDER QUANTITY CLIENT... ===\n', Fore.RESET)
        vandal.objects.eoq.EOQapp()
