"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        # enqueue a starting node
        # make a set to track if we've been there before
        #  while queue isnt empty:
            #  dequeue whatever is at the front, this is the current vert
            #  if we havent visited yet:
                # mark as visited
                #  get neighbors
                # for each of the neighbors:
                    # add to queue
        q = Queue()
        # store starting vert
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            vertex = q.dequeue()
            print(vertex)
            visited.add(vertex)

            for v in self.get_neighbors(vertex):
                if v not in visited:
                    q.enqueue(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        # add starting vert to stack
        s.push(starting_vertex)

        visited = set()

        while s.size():
            v = s.pop()
            # if the vert is not in visited set
            if v not in visited:
                # add it
                visited.add(v)
                print(v)
                # add neighbors to the stack
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # create visited set if none 
        if visited is None:
            visited = set()
        # check if starting vert is in visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            # call recursively for neighbors of starting vert
            for vrt in self.get_neighbors(starting_vertex):
                self.dft_recursive(vrt, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        q = Queue()
        # add start vert to q as list
        q.enqueue([starting_vertex])

        while q.size():
            # dq current path
            path = q.dequeue()
            # store the last vertex in path
            node = path[-1]

            # check if its in visited
            if node not in visited:
                # add it
                visited.add(node)
                # check for target and return the path
                if node == destination_vertex:
                    return path
                else:
                    # enq the path to each neighbor
                    for neighbor in self.get_neighbors(node):
                        q.enqueue(path + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size():
            # store the next item in the stack
            path = s.pop()
            # store the last vertex in path
            node = path[-1]

            if node not in visited:
                # add to visited
                visited.add(node)
                # if current node is our target, return to path
                if node == destination_vertex:
                    return path
                # loop over neighbors
                for neighbor in self.get_neighbors(node):
                    # add a path to each neighbor to the stack
                    s.push(path + [neighbor])
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if path == []:
            path = [starting_vertex]
        # base case if we have visited all nodes, no need for recursion
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            if starting_vertex == destination_vertex:
                return path
            
            # loop over the neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                # store dfs path of starting vert, recursive call passing in visited and the new path including neighbor
                result = self.dfs_recursive(neighbor, destination_vertex, visited, path + [neighbor])
                # if recursive call returns the path, it will be returned here
                if result:
                    return result
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
