import numpy as np
import math
from tqdm import tqdm

class SparseTable:
    def __init__(self, data: np.ndarray):
        self.n = len(data)
        self.k = math.floor(math.log2(self.n)) + 1
        self.st = np.zeros((self.k, self.n), dtype=data.dtype)
        
        # Calculate total number of iterations for progress bar
        total_iterations = sum(self.n - (1 << j) + 1 for j in range(1, self.k))
        
        # Initialize progress bar
        with tqdm(total=total_iterations, desc="Initializing Sparse Table", leave=False) as pbar:
            # Fill the first level (j=0)
            self.st[0] = data
            
            # Fill subsequent levels (j=1 to k-1)
            for j in range(1, self.k):
                i = 0
                while i + (1 << j) <= self.n:
                    self.st[j, i] = max(self.st[j-1, i], self.st[j-1, i + (1 << (j-1))])
                    i += 1
                    pbar.update(1)  # Update progress bar

    def query_max(self, l: int, r: int) -> int:
        length = r - l + 1
        k = math.floor(math.log2(length))
        return max(self.st[k, l], self.st[k, r - (1 << k) + 1])