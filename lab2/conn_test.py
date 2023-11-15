import unittest
from sabock_lab2 import *

class TestList(unittest.TestCase):
        
    def test_graph_1(self):
        g = Graph()
        g.read_file("lab2_example")
        self.assertEqual(g.strong_connectivity(),[[0,4],[1,2,3],[5]])
    
    def test_graph_2(self):
        g = Graph()
        g.read_file("directed_graph_test_1")
        self.assertEqual(g.strong_connectivity(),[[1,2,5],[3,4,8],[6,7]])
        
    def test_graph_3(self):
        g = Graph()
        g.read_file("directed_graph_test_2")
        self.assertEqual(g.strong_connectivity(),[[1,2,3,4],[5,6,7]])

    def test_graph_4(self):
        g = Graph()
        g.read_file("graph_test_3")
        self.assertEqual(g.strong_connectivity(),[[0,1,2,3],[4,5,6],[7]])
        
    def test_graph_5(self):
        g = Graph()
        g.read_file("graph_test_4")
        self.assertEqual(g.strong_connectivity(),[[0,1,2],[3],[4]])
        
    def test_graph_6(self):
        g = Graph()
        g.read_file("graph_test_5")
        self.assertEqual(g.strong_connectivity(),[[0,1,2],[3,4,5,6],[7],[8],[9]])
        
if __name__ == "__main__":
    unittest.main()