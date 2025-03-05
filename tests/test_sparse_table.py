#
#  test_sparse_table.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/5/25.
#


import unittest
import numpy as np
from src.sparse_table import SparseTable

class TestSparseTable(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.sparse = SparseTable(np.array(self.data, dtype=np.int32))

    def test_query_max(self):
        # Test max queries
        self.assertEqual(self.sparse.query_max(0, 0), 1)  # Max of [1]
        self.assertEqual(self.sparse.query_max(0, 1), 2)  # Max of [1, 2]
        self.assertEqual(self.sparse.query_max(0, 4), 5)  # Max of [1, 2, 3, 4, 5]
        self.assertEqual(self.sparse.query_max(2, 4), 5)  # Max of [3, 4, 5]
