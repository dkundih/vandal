# object that contains the required data.
class Dijkstra:

    '''

    (OBJECT INFO)
    -------------

    vandal.Dijkstra - main class that contains the data of defined nodes, origin and the desired destination.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.Dijkstra.function()

        .execute() -  contains the data of defined nodes, origin and the desired destination, executes a Dijkstra algorithm route scan on a defined path.
        * takes 3 additional arguments.
            nodes - dictionary of dictionaries of nodes with their corelating weights.

            eg.
            nodes = {
            'a':{'b':8,'c':5},
            'b':{'c':2,'d':4},
            'c':{'b':5,'d':4,'e':3},
            'd':{'e':5},
            'e':{'d':6}
            }

            origin - origin node as a starting point.
            destination - destination node of the desired route.

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
        return f'Dijkstra defining object that stores the configuration data for finding the path within {self.nodes} from {self.origin} => {self.destination}.'

    # class information.
    def __repr__(self):
        return f'Dijkstra defining object that stores the configuration data for finding the path within {self.nodes} from {self.origin} => {self.destination}.'

    # executes a Dijkstra algorithm route scan on a defined path.
    def execute(self, nodes, origin, destination, log_summary = False):
        self.nodes = nodes
        self.origin = origin
        self.destination = destination
        self.log_summary = log_summary
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
            print('Optimal path: ' + str(output_path), '\nMinimal distance: ' + str(optimal_distance[self.destination]))
