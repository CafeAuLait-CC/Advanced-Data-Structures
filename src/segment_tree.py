#
#  segment_tree.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/4/25.
#

import numpy as np
from tqdm import tqdm

class SegmentTree:
    def __init__(self, data: np.ndarray):
        """
        Initialize the Segment Tree with the given data.
        
        Args:
            data (np.ndarray): Input array to build the Segment Tree.
        """
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1  # Find the next power of 2 >= n
        
        # Initialize with zeros (sum and max)
        self.tree_sum = np.zeros(2 * self.size, dtype=np.int64)  # Sum tree
        self.tree_max = np.zeros(2 * self.size, dtype=np.int64)  # Max tree
        
        # Bottom-up initialization
        self.tree_sum[self.size:self.size + self.n] = data  # Fill leaves with data
        self.tree_max[self.size:self.size + self.n] = data  # Fill leaves with data
        for i in tqdm(range(self.size - 1, 0, -1), desc="Initializing Segment Tree", leave=False):
            self.tree_sum[i] = self.tree_sum[2*i] + self.tree_sum[2*i+1]  # Compute sum for internal nodes
            self.tree_max[i] = max(self.tree_max[2*i], self.tree_max[2*i+1])  # Compute max for internal nodes

    def update(self, index: int, value: int):
        """
        Update the value at the specified index in the Segment Tree.
        
        Args:
            index (int): Index to update (0-based).
            value (int): New value to set at the index.
        """
        pos = index + self.size  # Convert to leaf position
        self.tree_sum[pos] = value  # Update sum tree
        self.tree_max[pos] = value  # Update max tree
        while pos > 1:
            pos >>= 1  # Move to parent
            self.tree_sum[pos] = self.tree_sum[2*pos] + self.tree_sum[2*pos+1]  # Recompute sum
            self.tree_max[pos] = max(self.tree_max[2*pos], self.tree_max[2*pos+1])  # Recompute max

    def query_sum(self, l: int, r: int) -> int:
        """
        Compute the sum of values in the range [l, r].
        
        Args:
            l (int): Start index (0-based).
            r (int): End index (0-based).
        
        Returns:
            int: Sum of values in the range.
        """
        res = 0
        l += self.size  # Convert to leaf position
        r += self.size  # Convert to leaf position
        while l <= r:
            if l % 2 == 1:
                res += self.tree_sum[l]  # Add left child
                l += 1
            if r % 2 == 0:
                res += self.tree_sum[r]  # Add right child
                r -= 1
            l >>= 1  # Move to parent
            r >>= 1  # Move to parent
        return res

    def query_max(self, l: int, r: int) -> int:
        """
        Compute the maximum value in the range [l, r].
        
        Args:
            l (int): Start index (0-based).
            r (int): End index (0-based).
        
        Returns:
            int: Maximum value in the range.
        """
        max_val = -np.inf
        l += self.size  # Convert to leaf position
        r += self.size  # Convert to leaf position
        while l <= r:
            if l % 2 == 1:
                max_val = max(max_val, self.tree_max[l])  # Update max with left child
                l += 1
            if r % 2 == 0:
                max_val = max(max_val, self.tree_max[r])  # Update max with right child
                r -= 1
            l >>= 1  # Move to parent
            r >>= 1  # Move to parent
        return max_val
