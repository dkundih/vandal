# object that contains the required data.
class Dijkstra:

    '''

    (OBJECT INFO)
    -------------

    vandal.Dijkstra - main class that contains the data of defined nodes, origin and the desired destination.

    (OBJECT FUNCTIONS)
    ------------------

    eg. vandal.Dijkstra.function()

        .execute() - executes a Dijkstra algorithm route scan on a defined path.
        * takes 4 additional arguments.
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
            log_summary (default: log_summary = False) - event log of executed functions. - DEVELOPER MODE ONLY
        * automatically executes the .execute() function.

    (DEVELOPER MODE)
    ----------------

    Developer mode functions can only be set up manually by removing the '#DEVELOPER MODE -' in the source code.

        .get_logs() - shows the event log of executed functions.
        * takes no additional arguments.
        * Requirements:
            log_summary = True.
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

    # initial value configuration.
    def __init__(self):
        pass

    # DEVELOPER MODE - creates an event log that tracks the function execution time and duration.
    def classLog(func_name):
        def log(func):
                import time
                import datetime
                def logsaver(self, *args, **kwargs):
                    if self.log_summary == True:
                        start = time.time()
                        results = func(self, *args, **kwargs)
                        with open('vandal Logs.txt', 'a') as f:
                            f.write('Performed a function ' + func_name + ' at: ' + str(datetime.datetime.now()) + '.' + ' Time spent performing the action: ' + str(time.time() - start) + ' seconds.' + '\n')
                            return results
                    else:
                            results = func(self, *args, **kwargs)
                            return results
                return logsaver
        return log

    # DEVELOPER MODE - @classLog('__str__()')
    # class information.
    def __str__(self):
        return f'Dijkstra defining object that stores the configuration data for finding the path within {self.nodes} from {self.origin} => {self.destination}.'

    # DEVELOPER MODE - @classLog('__repr__()')
    # class information.
    def __repr__(self):
        return f'Dijkstra defining object that stores the configuration data for finding the path within {self.nodes} from {self.origin} => {self.destination}.'

    # DEVELOPER MODE - @classLog('execute() - built in function.')
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

    # DEVELOPER MODE - @classLog('get_logs()')
    # returns the saved logs of executed functions.
    def get_logs(self):
        f = open('vandal Logs.txt', 'r')
        print(f.read())
