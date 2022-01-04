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

    (DEVELOPER MODE)
    ----------------

    Developer mode functions can only be set up manually by removing the '#DEVELOPER MODE -' in the source code.

        * takes no additional arguments.
        * Requirements:
            '# DEVELOPER MODE -' removed in the code.

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
)

    # import duality package decorators.
    # DEVELOPER MODE - from duality import track, record

    # initial launch.
    # DEVELOPER MODE - @track.entry('init')
    # DEVELOPER MODE - @record.entry(option_name = 'init', option_description = 'initial launch.')
    def __init__(self):
        pass

    # class information.
    # DEVELOPER MODE - @track.entry('string')
    # DEVELOPER MODE - @record.entry(option_name = 'string', option_description = 'class information.')
    def __str__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    # class information.
    # DEVELOPER MODE - @track.entry('representation')
    # DEVELOPER MODE - @record.entry(option_name = 'repr', option_description = 'shows object details.')
    def __repr__(self):
        return f'EOQ defining object that contains annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.'

    # executes the calculation of EOQ over the defined parameters.
    # DEVELOPER MODE - @track.entry('execution')
    # DEVELOPER MODE - @record.entry(option_name = 'execution', option_description = 'executes the calculation of EOQ over the defined parameters.')
    def execute(self, annual_demand_quantity, order_fixed_cost, annual_holding_cost):
        self.annual_demand_quantity = annual_demand_quantity
        self.order_fixed_cost = order_fixed_cost
        self.annual_holding_cost = annual_holding_cost
        print(f'EOQ has been set up with annual demand quantity of {self.annual_demand_quantity} pieces, fixed cost of the order of {self.order_fixed_cost} and with the annual holding cost of {self.annual_holding_cost}.')
        import math
        eoq = math.sqrt((((2 * self.annual_demand_quantity) * self.order_fixed_cost) / self.annual_holding_cost))
        print('EOQ is: ', eoq)
        return eoq
