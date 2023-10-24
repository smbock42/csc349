import unittest
from graph import *

class TestList(unittest.TestCase):
    def test_graph_1(self):
        g = Graph("directed_graph_test_1")
        self.assertEqual(g.conn_components(),[["v0","v4"],["v1","v2","v3"],["v5"]])
        
    def test_graph_2(self):
        g = Graph("test")
        
if __name__ == "__main__":
    unittest.main()