import sys

class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 
        
    def __iter__(self):
        while not self.is_empty():
            yield self.pop()
    
    def __repr__(self):
        return str(self.items)
    
    def __len__(self):
        return self.num_items

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity
    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError("Your stack is full")
        self.items[self.num_items] = item
        self.num_items += 1
        
        
    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError("Your stack is empty")
        x = self.items[self.num_items-1]
        self.items[self.num_items-1] = None
        self.num_items -= 1
        return x
    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError("Your stack is empty")
        return self.items[self.num_items-1]
    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = int(key) #TODO: same as name? 
        self.in_edges = [] #TODO: add in edges
        self.out_edges = [] #TODO: add out edges
        self.previsit = None #TODO: Add pre/post visit numbers
        self.postvisit = None #TODO: Add pre/post visit numbers
        self.component = None #TODO: not sure what component is? 


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self):
        self.dictionary = {}
        
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        
    
    def read_file(self,filename):
        file = open(filename)
        for line_number, line in enumerate(file):
            if line_number == 0:
                num_nodes = int(line.split()[0])
                if num_nodes == 0:
                    raise ValueError("Graph must have one or more vertices")
            else:
                line = line.replace("\n","")
                split = line.split(", ")
                v1, v2 = (int(split[0]), int(split[1]))
                if len(split) != 0:
                    self.add_vertex(v1)
                    self.add_vertex(v2)
                    self.add_edge(v1,v2)
        file.close()
    # def __iter__(self):
    #     for vertex in self.get_vertices():
    #         yield vertex



    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.dictionary:
            self.dictionary[key] = Vertex(key)
            return f"Added Vertex: {key}"
        return f"Vertex: {key} Already In Graph"
        

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.dictionary[v1].out_edges.append(v2)
        self.dictionary[v2].in_edges.append(v1)
        return f"Added Edge ({v1}, {v2})"



    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key not in self.dictionary:
            return None
        return self.dictionary[key]

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        return sorted(self.dictionary.keys())
    
    def transpose(self):
        transposed_graph = Graph()
        for vertex in self.get_vertices():
            for adjacent in self.get_vertex(vertex).out_edges:
                transposed_graph.add_vertex(adjacent)
                transposed_graph.add_vertex(vertex)
                transposed_graph.add_edge(adjacent,vertex)
        return transposed_graph
                
            
    def DFS(self, vertex,stack,visited):
        #add implemenation
        visited[vertex] = True
        for adjacent in self.get_vertex(vertex).out_edges:
            if not visited[adjacent]:
                self.DFS(adjacent, stack, visited)
        stack.push(vertex)
                
    def strong_connectivity(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        #This method MUST use Depth First Search logic!
        #add implementation
        
        stack = Stack(len(self.get_vertices()))
        visited = {vertex: False for vertex in self.get_vertices()}
        
        for vertex in self.get_vertices():
            if not visited[vertex]:
                self.DFS(vertex, stack, visited)
                
        transpose_graph = self.transpose()
        
        visited = {vertex: False for vertex in self.get_vertices()}

        connected_components = []
        
        while not stack.is_empty():
            vertex = stack.pop()
            if not visited[vertex]:
                component = []
                transpose_stack = Stack(len(self.get_vertices()))
                transpose_graph.DFS(vertex,transpose_stack,visited)
                while not transpose_stack.is_empty():
                    component.append(transpose_stack.pop())
                connected_components.append(sorted(component))
        
        return sorted(connected_components)
    
    
def main():
    filename = sys.argv[1]
    G = Graph()
    G.read_file(filename)
    components = G.strong_connectivity()
    print(components)
    return components
if __name__ == '__main__':
    main()