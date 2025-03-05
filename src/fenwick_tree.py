#
#  fenwick_tree.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/4/25.
#

import numpy as np
from tqdm import tqdm

class FenwickTree:
    def __init__(self, data: np.ndarray):
        """
        Initialize the Fenwick Tree (Binary Indexed Tree) with the given data.
        
        Args:
            data (np.ndarray): Input array to build the Fenwick Tree.
        """
        self.n = len(data)
        self.tree = np.zeros(self.n + 1, dtype=np.int64)  # 1-based indexing
        
        # O(n) initialization
        self.tree[1:] = data  # Copy data into the tree (1-based indexing)
        for i in tqdm(range(1, self.n + 1), desc="Initializing Fenwick Tree", leave=False):
            parent = i + (i & -i)  # Calculate parent index using LSB
            if parent <= self.n:
                self.tree[parent] += self.tree[i]  # Propagate value to parent

    def update(self, index: int, new_val: int):
        """
        Update the value at the specified index in the Fenwick Tree.
        
        Args:
            index (int): Index to update (0-based).
            new_val (int): New value to set at the index.
        """
        delta = new_val - (self.query_prefix(index) - self.query_prefix(index - 1))  # Calculate delta
        i = index + 1  # Convert to 1-based index
        while i <= self.n:
            self.tree[i] += delta  # Update current node
            i += i & -i  # Move to next node using LSB

    def query_prefix(self, idx: int) -> int:
        """
        Compute the prefix sum up to the specified index.
        
        Args:
            idx (int): Index to compute prefix sum (0-based).
        
        Returns:
            int: Prefix sum up to the index.
        """
        res = 0
        i = idx + 1  # Convert to 1-based index
        while i > 0:
            res += self.tree[i]  # Add current node value
            i -= i & -i  # Move to parent node using LSB
        return res

    def query_sum(self, l: int, r: int) -> int:
        """
        Compute the sum of values in the range [l, r].
        
        Args:
            l (int): Start index (0-based).
            r (int): End index (0-based).
        
        Returns:
            int: Sum of values in the range.
        """
        return self.query_prefix(r) - self.query_prefix(l - 1)  # Use prefix sums to compute range sum
