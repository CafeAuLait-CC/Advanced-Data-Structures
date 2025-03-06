#
#  sparse_table.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/4/25.
#

import numpy as np
import math
from tqdm import tqdm

class SparseTable:
    def __init__(self, data: np.ndarray):
        """
        Initialize the Sparse Table with the given data.
        
        Args:
            data (np.ndarray): Input array to build the Sparse Table.
        """
        self.n = len(data)
        self.k = math.floor(math.log2(self.n)) + 1
        self.st = np.zeros((self.k, self.n), dtype=data.dtype)
        
        # Fill the first level (j=0)
        self.st[0] = data
        
        # Initialize progress bar for levels
        with tqdm(total=self.k - 1, desc="Initializing Sparse Table", leave=False) as pbar:
            for j in range(1, self.k):
                # Calculate the maximum i for current j
                max_i = self.n - (1 << j)
                for i in range(max_i + 1):
                    self.st[j, i] = max(self.st[j-1, i], self.st[j-1, i + (1 << (j-1))])
                pbar.update(1)


    def query_max(self, l: int, r: int) -> int:
        """
        Compute the maximum value in the range [l, r].
        
        Args:
            l (int): Start index (0-based).
            r (int): End index (0-based).
        
        Returns:
            int: Maximum value in the range.
        """
        length = r - l + 1  # Length of the range
        k = math.floor(math.log2(length))  # Find the largest power of 2 <= length
        # Compute max of two overlapping ranges covering [l, r]
        return max(self.st[k, l], self.st[k, r - (1 << k) + 1])

