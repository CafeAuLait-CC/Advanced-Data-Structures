#
#  test_fenwick_tree.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/5/25.
#


import unittest
import numpy as np
from src.fenwick_tree import FenwickTree


class TestFenwickTree(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.fenwick = FenwickTree(np.array(self.data, dtype=np.int32))

    def test_query_sum(self):
        # Test prefix sums
        self.assertEqual(self.fenwick.query_sum(0, 0), 1)  # Sum of [1]
        self.assertEqual(self.fenwick.query_sum(0, 1), 3)  # Sum of [1, 2]
        self.assertEqual(self.fenwick.query_sum(0, 4), 15)  # Sum of [1, 2, 3, 4, 5]
        self.assertEqual(self.fenwick.query_sum(2, 4), 12)  # Sum of [3, 4, 5]

    def test_update(self):
        # Update index 2 (value 3) to 10
        self.fenwick.update(2, 10)
        self.assertEqual(self.fenwick.query_sum(0, 4), 22)  # Sum of [1, 2, 10, 4, 5]
        self.assertEqual(self.fenwick.query_sum(2, 2), 10)  # Sum of [10]
