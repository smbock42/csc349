from stack_array import * #Needed for Depth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key #TODO: same as name? 
        self.adjacent_to = [] #TODO: I think this is working
        self.in_edges = [] #TODO: add in edges
        self.out_edges = [] #TODO: add out edges
        self.previsit = None #TODO: Add pre/post visit numbers
        self.postvisit = None #TODO: Add pre/post visit numbers
        self.component = None #TODO: not sure what component is? 


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        file = open(filename)
        self.dictionary = {}
        for line_number, line in enumerate(file):
            if line_number == 0:
                num_nodes = line.split()[0]
            else:

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

    def conn_components(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        #This method MUST use Depth First Search logic!
        stack = Stack(len(self.dictionary))
        visited = {}
        outputlist = []

        for vertex in self.get_vertices(): #iterate through vertices
            connectedcomponent = []
            if vertex not in visited:
                stack.push(vertex)
                visited[vertex] = "V"
            while not stack.is_empty():
                push = False
                currentvertex = stack.peek()
                for adjacent in self.get_vertex(currentvertex).adjacent_to: #iterate through adjacency list
                    if adjacent not in visited:
                        stack.push(adjacent)
                        push = True
                        visited[adjacent] = "V"
                        break
                if push == False:
                    connectedcomponent.append(stack.pop())
                    
                    
            if len(connectedcomponent) != 0: outputlist.append(sorted(connectedcomponent))
        return outputlist


    