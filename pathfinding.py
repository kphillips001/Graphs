# An example set of data
# The items in the grid represent individual nodes (vertices you can travel to)
# Anything with a value of 0 is considered a "Wall" that you cannot walk through
# anything with a number of 1 or more represents the individual cost of each grid item
# A 1 means its pretty cheap to walk there (imagine we smooth paved road)
# A 17 (or whatever number you want) means that this grid item is very expensive to walk to (imagine a swamp, you can still go there, but dont)

travel_grid = [ 
    [('A', 1), ('B', 1), ('C', 1), ('D', 1), ('E', 1)],

    [('E', 17), ('F', 1), ('G', 17), ('H', 17), ('I', 1)],

    [('J', 1), ('K', 1), ('L', 0), ('M', 1), ('N', 1)],

    [('O', 1), ('P', 1), ('Q', 0), ('R', 1), ('S', 1)],

    [('T', 1), ('U', 0), ('V', 0), ('X', 1), ('Y', 1)]
]

# The a_star algorithm will find the best path from a start coordinate to an end coordinate
# the example below starts at coordinates (0,0 ) == (A, 1)
# And it ends at (4, 4) == (Y, 1)

# this class helps us keep track of a bunch of data for each node that we add to our queue
# Think back to the guided projects, we had to keep track of paths, 
# if we wanted to we could have used this class and just stored the self.path parameter
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, coords=None):
        self.coords = coords
        self.path = []
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.coords == other.coords


# Very similar looking get_neighbors function as we had for our islands problem
def get_neighbors(row, col, grid):
    # Look Up down left and right for other values of 1
    neighbors = [] # all tuples of coordinates that are neighbors of current (row, col)

    # check North
    if row > 0 and grid[row-1][col][1] >= 1:
        neighbors.append( (row-1, col ) )

    # check south:
    if row < len(grid) - 1 and grid[row + 1][col][1] >= 1:
        neighbors.append((row + 1, col))

    # check west: 
    if col > 0 and grid[row][col-1][1] >= 1:
        neighbors.append((row, col - 1))

    if col < len(grid[0]) - 1 and grid[row][col+1][1] >= 1:
        neighbors.append((row, col + 1))

    return neighbors


def a_star(start_coords, end_coords):
    # create the queue
    queue = []

    visited_coords = set()        

    # create the node that we will push onto the queue
    start_node = Node(start_coords)
    # Create the initial path for the start node, its just an array of 1 item
    start_node.path = [start_coords]

    queue.append(start_node)

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node.coords not in visited_coords:
            # add the coords to visited
            visited_coords.add(current_node.coords)

            # CHECK IF WE FOUND OUR DESTINATION
            if current_node.coords == end_coords:
                print("YAY WE FOUND IT")
                return current_node.path

            # ADD NEIGHBORS TO THE QUEUE
            for neighbor_coords in get_neighbors(current_node.coords[0], current_node.coords[1], travel_grid):
                row = neighbor_coords[0]
                col = neighbor_coords[1]
                # Get the cost of this node from the travel_grid data
                grid_item = travel_grid[row][col] # ex: (B, 1)
                # this is the individual cost of the new node we want to go to
                grid_item_cost = grid_item[1]

                neighbor_node = Node(neighbor_coords)
                # Calculate the COST of this new node
                # G is the TOTAL COST to this node, from the start
                neighbor_node.g = grid_item_cost + current_node.g
                # compute the guesstimate from the neighbor to the END NODE
                neighbor_node.h = (end_coords[0] - row)**2 + (end_coords[1] - col) ** 2
                # Using the F = G * H formula
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Add this neighbor to the queue, and keep track of path
                new_path = list(current_node.path)
                new_path.append(neighbor_node.coords)
                neighbor_node.path = new_path
                queue.append(neighbor_node)
                # Sort the queue based on each nodes F value, so that cheaper nodes are at the front
                queue.sort(key = lambda node: node.f)



path = a_star((0,0), (4, 4))
print(path)

for coord in path:
    print(f'GO TO {travel_grid[coord[0]][coord[1]]}')