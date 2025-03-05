import numpy as np
from tqdm import tqdm

class SegmentTree:
    def __init__(self, data: np.ndarray):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1  # Next power of 2
        
        # Initialize with zeros (sum and max)
        self.tree_sum = np.zeros(2 * self.size, dtype=np.int64)
        self.tree_max = np.zeros(2 * self.size, dtype=np.int64)
        
        # Bottom-up initialization
        self.tree_sum[self.size:self.size + self.n] = data
        self.tree_max[self.size:self.size + self.n] = data
        for i in tqdm(range(self.size - 1, 0, -1), desc="Initializing Segment Tree", leave=False):
            self.tree_sum[i] = self.tree_sum[2*i] + self.tree_sum[2*i+1]
            self.tree_max[i] = max(self.tree_max[2*i], self.tree_max[2*i+1])

    def update(self, index: int, value: int):
        pos = index + self.size
        self.tree_sum[pos] = value
        self.tree_max[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree_sum[pos] = self.tree_sum[2*pos] + self.tree_sum[2*pos+1]
            self.tree_max[pos] = max(self.tree_max[2*pos], self.tree_max[2*pos+1])

    def query_sum(self, l: int, r: int) -> int:
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                res += self.tree_sum[l]
                l += 1
            if r % 2 == 0:
                res += self.tree_sum[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def query_max(self, l: int, r: int) -> int:
        max_val = -np.inf
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                max_val = max(max_val, self.tree_max[l])
                l += 1
            if r % 2 == 0:
                max_val = max(max_val, self.tree_max[r])
                r -= 1
            l >>= 1
            r >>= 1
        return max_val