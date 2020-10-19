'''
- build a graph with the ancestor and (parent, child) pairs
- perform DFS on given starting node
'''

def earliest_ancestor(ancestors, starting_node):
    # build graph
    vert = {}

    for pair in ancestors:
        v = pair[1]

        if v not in vert:
            vert[v] = set()
        
        vert[v].add(pair[0])
    
    paths = []
    # search graph depth first
    def dfs_search(path, visited=set()):
        current = path[-1]

        if current not in vert:
            paths.append(path)
        else:
            children = vert[current]
            for v in children:
                if v not in visited:
                    visited.add(v)
                    new_path = list(path)
                    new_path.append(v)
                    dfs_search(new_path, visited)
    dfs_search([starting_node])

    max_length_index = 0
    for i in range(1, len(paths)):
        if len(paths[i]) > len(paths[max_length_index]):
            max_length_index = i
        elif len(paths[i]) == len(paths[max_length_index]):
            if paths[i][-1] < paths[max_length_index][-1]:
                max_length_index = i
    
    if len(paths[max_length_index]) > 1:
        return paths[max_length_index][-1]
    
    return -1