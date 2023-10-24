import unittest
from graph import *

class TestList(unittest.TestCase):
    
    def test_lab2_example(self):
        g = Graph("lab2_example")
        self.assertEqual(g.conn_components(),[["v0","v4"],["v1","v2","v3"],["v5"]])