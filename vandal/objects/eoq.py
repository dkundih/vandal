# coloring.
from colorama import Fore, init 

init()

# type hints and annotations.
from vandal.plugins.metaclass import Meta
from vandal.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
)

# object that contains the calculation data.
class EOQ:

    '''

    (OBJECT INFO)
    -------------

    eg. EOQ = vandal.EOQ()

    vandal.EOQ - main class that stores the data required for an EOQ simulation.
        * takes 3 additional arguments.
            annual_demand_quantity - integer of demanded quantity in a year.
            order_fixed_cost - integer or float presenting the fixed cost of the order.
            annual_holding_cost - cost of holding the goods in a year.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.EOQ.function()

        .execute() - executes the calculation of EOQ over the defined parameters.
            * takes 1 additional argument.
                filtered (defualt: filtered = True) - filters the print option and leaves just the return object.

    EOQapp (EXECUTABLE CLI MODULE)
    -------------------------

    vandal.EOQapp is an executable function that runs the Command Line Interface of the vandal EOQ module.
        print(help(vandal.EOQapp)) in order to see available features.
        
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
    def __init__(
        self,
        annual_demand_quantity : NumberType = None,
        order_fixed_cost : NumberType = None, 
        annual_holding_cost : NumberType = None,
    ) -> ReturnType:

        self.annual_demand_quantity = annual_demand_quantity
        self.order_fixed_cost = order_fixed_cost
        self.annual_holding_cost = annual_holding_cost
        
        return

    # class information.
    def __str__(
        self,
        ) -> StringType:

        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    # class information.
    def __repr__(
        self,
        ) -> StringType:

        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    # executes the calculation of EOQ over the defined parameters.
    def execute(
        self, 
        filtered = True,
        ) -> NumberType:

        if filtered == False:
            print(Fore.GREEN + 'EOQ has been set up with annual demand quantity of ' + Fore.RESET + f'{self.annual_demand_quantity}' + Fore.GREEN + ' pieces, fixed cost of the order of ' + Fore.RESET + f'{self.order_fixed_cost}' + Fore.GREEN + ' and with the annual holding cost of ' + Fore.RESET + f'{self.annual_holding_cost}.')
        
        import math
        eoq = math.sqrt((((2 * self.annual_demand_quantity) * self.order_fixed_cost) / self.annual_holding_cost))
        eoq = round(eoq, 2)

        if filtered == False:
            print(Fore.GREEN + 'EOQ is:', Fore.RESET, eoq)

        return eoq

def EOQapp():
    
    '''
    
    runs as:

        *IDE: vandal.EOQapp()
        *TERMINAL: python -m vandal -e eoq / python -m vandal --entry eoq
        
    '''

    print(Fore.YELLOW + 'EOQ app is initializing...', Fore.RESET)
    
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
    
    adq = float(input('Enter the annual demand quantity: '))
    ofc = float(input('Enter the fixed cost of the order: '))
    ahc = float(input('Enter the annual holding cost: '))

    EOQObj = EOQ(annual_demand_quantity = adq, order_fixed_cost = ofc, annual_holding_cost = ahc)
    print('')
    EOQObj.execute(filtered = False)

if __name__ == '__main__':
    EOQapp()
