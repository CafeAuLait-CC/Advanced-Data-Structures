#
#  test_segment_tree.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/5/25.
#


import unittest
import numpy as np
from src.segment_tree import SegmentTree

class TestSegmentTree(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.segment = SegmentTree(np.array(self.data, dtype=np.int32))

    def test_query_sum(self):
        # Test sum queries
        self.assertEqual(self.segment.query_sum(0, 0), 1)  # Sum of [1]
        self.assertEqual(self.segment.query_sum(0, 1), 3)  # Sum of [1, 2]
        self.assertEqual(self.segment.query_sum(0, 4), 15)  # Sum of [1, 2, 3, 4, 5]
        self.assertEqual(self.segment.query_sum(2, 4), 12)  # Sum of [3, 4, 5]

    def test_query_max(self):
        # Test max queries
        self.assertEqual(self.segment.query_max(0, 0), 1)  # Max of [1]
        self.assertEqual(self.segment.query_max(0, 1), 2)  # Max of [1, 2]
        self.assertEqual(self.segment.query_max(0, 4), 5)  # Max of [1, 2, 3, 4, 5]
        self.assertEqual(self.segment.query_max(2, 4), 5)  # Max of [3, 4, 5]

    def test_update(self):
        # Update index 2 (value 3) to 10
        self.segment.update(2, 10)
        self.assertEqual(self.segment.query_sum(0, 4), 22)  # Sum of [1, 2, 10, 4, 5]
        self.assertEqual(self.segment.query_max(0, 4), 10)  # Max of [1, 2, 10, 4, 5]
