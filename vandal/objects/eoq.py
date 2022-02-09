# coloring.
import colorama
from colorama import Fore, init 

init()

# object that contains the calculation data.
class EOQ:

    '''

    (OBJECT INFO)
    -------------

    vandal.EOQ - main class.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.EOQ.function()

        .execute() - executes the calculation of EOQ over the defined parameters.
        * takes 3 additional arguments.
            annual_demand_quantity - integer of demanded quantity in a year.
            order_fixed_cost - integer or float presenting the fixed cost of the order.
            annual_holding_cost - cost of holding the goods in a year.

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
        __donate__,
        __APPversion__,
    )

    # initial launch.
    def __init__(self):
        pass

    # class information.
    def __str__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    # class information.
    def __repr__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    # executes the calculation of EOQ over the defined parameters.
    def execute(self, annual_demand_quantity, order_fixed_cost, annual_holding_cost):
        self.annual_demand_quantity = annual_demand_quantity
        self.order_fixed_cost = order_fixed_cost
        self.annual_holding_cost = annual_holding_cost
        print(Fore.GREEN + 'EOQ has been set up with annual demand quantity of ' + Fore.RESET + f'{self.annual_demand_quantity}' + Fore.GREEN + ' pieces, fixed cost of the order of ' + Fore.RESET + f'{self.order_fixed_cost}' + Fore.GREEN + ' and with the annual holding cost of ' + Fore.RESET + f'{self.annual_holding_cost}.')
        import math
        eoq = math.sqrt((((2 * self.annual_demand_quantity) * self.order_fixed_cost) / self.annual_holding_cost))
        print(Fore.GREEN + 'EOQ is:', Fore.RESET, eoq)
        return eoq

def EOQapp():
    
    '''
    
    runs as:

        *IDE: vandal.EOQapp()
        *TERMINAL: python -m vandal -e eoq / python -m vandal --entry eoq
        
    '''

    # relevant imports.
    import os
    from vandal.misc._meta import (
        __version__,
        __APPversion__,
    )
    from vandal.objects.eoq import EOQ
    os.system('cls')

    # greeting.
    print(Fore.YELLOW + '\n - vandal Command Line Interface Application © David Kundih -', __APPversion__)
    print(Fore.YELLOW + ' - vandal package version -', 'v',__version__, Fore.RESET, '\n')
    EOQObj = EOQ()
    adq = int(input('Enter the annual demand quantity: '))
    ofc = int(input('Enter the fixed cost of the order: '))
    ahc = int(input('Enter the annual holding cost: '))
    print('')
    EOQObj.execute(annual_demand_quantity = adq, order_fixed_cost = ofc, annual_holding_cost = ahc)

if __name__ == '__main__':
    EOQapp()