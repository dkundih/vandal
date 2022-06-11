# type hints and annotations.
from logistics.plugins.metaclass import Meta

# imports all data types.
from logistics.plugins.types import *

# package.
class Dijkstra:

    '''

    (OBJECT INFO)
    -------------

    eg. Dijkstra = vandal.Dijkstra()
    
    vandal.Dijkstra - main class that contains contains the data of defined nodes, origin and the desired destination.
        * takes 3 additional arguments.
            nodes - dictionary of dictionaries of nodes with their corelating weights.

            eg.
            nodes = {
            'a':{'b':8,'c':5},
            'b':{'c':2,'d':4},
            'c':{'b':5,'d':4,'e':3},
            'd':{'e':5},
            'e':{'d':6},
            }

            origin - origin node as a starting point.
            destination - destination node of the desired route.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.Dijkstra.function()

        .execute() - executes the Dijkstra algorithm on top of the defined data.
            * takes 1 additional argument.
                filtered (default: filtered = True) - filters the print option and leaves just the return object.

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

    def __init__(
        self,
        nodes : DictionaryType = None, 
        origin : StringType = None, 
        destination : StringType = None,
        ) -> ReturnType:

        '''
        * initial launch.
        '''
        
        self.nodes = nodes
        self.origin = origin
        self.destination = destination
        
        return

    def __str__(
        self,
        ) -> StringType:

        '''
        * class information.
        '''

        return f'Dijkstra defining object that stores the configuration data for finding the path within {self.nodes} from {self.origin} => {self.destination}.'

    def __repr__(
        self,
        ) -> StringType:

        '''
        * class information.
        '''

        return f'Dijkstra defining object that stores the configuration data for finding the path within {self.nodes} from {self.origin} => {self.destination}.'

    def execute(
        self,
        filtered : BooleanType = True,
        ) -> AnyArrayAlike:

        '''
        * executes a Dijkstra algorithm route scan on a defined path.

        - filtered (True/False) - filters the information about path.
        # DEFAULT: Dijkstra.execute(filtered : BooleanType = True.)
        '''

        import pandas as pd
        import numpy as np

        if filtered == False:
            print(f'Dijkstra has been set up for for finding the path from {self.origin} => {self.destination}.')
            
        Nodes = self.nodes
        preNode = {}
        optimal_distance = {}
        output_path = []

        for node in Nodes:
            optimal_distance[node] = float('inf')
        optimal_distance[self.origin] = 0

        while Nodes:
            closestNode = None
            for node in Nodes:
                if closestNode is None:
                    closestNode = node
                elif optimal_distance[node] < optimal_distance[closestNode]:
                    closestNode = node

            for secondaryNode, weight in self.nodes[closestNode].items():
                if weight + optimal_distance[closestNode] < optimal_distance[secondaryNode]:
                    optimal_distance[secondaryNode] = weight + optimal_distance[closestNode]
                    preNode[secondaryNode] = closestNode
            Nodes.pop(closestNode)

        liveNode = self.destination
        
        while liveNode != self.origin:
            try:
                output_path.insert(0, liveNode)
                liveNode = preNode[liveNode]
            except KeyError:
                print('Path unavailable.')
                break
        output_path.insert(0, self.origin)

        if optimal_distance[self.destination] != float('inf'):
            final_path = {'Optimal path' : [output_path], 'Minimal distance' : (optimal_distance[self.destination]),}
            final_path = pd.DataFrame(final_path, index = ['Output'])
            final_path = final_path.transpose() 

            return final_path

        else:
            final_path = {'Optimal path' : [None], 'Minimal distance' : None,}
            final_path = pd.DataFrame(final_path, index = ['Output'])
            final_path = final_path.transpose() 

            return final_path
