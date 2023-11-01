from sabock_lab2 import Graph
import sys
def main():
    filename = sys.argv[1]
    g = Graph()
    g.read_file(filename)
    
    return(g.strong_connectivity())


if __name__== "__main__":
    main()