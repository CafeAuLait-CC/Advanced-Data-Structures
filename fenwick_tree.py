import numpy as np
from tqdm import tqdm

class FenwickTree:
    def __init__(self, data: np.ndarray):
        self.n = len(data)
        self.tree = np.zeros(self.n + 1, dtype=np.int64)  # 1-based indexing
        
        # O(n) initialization
        self.tree[1:] = data
        for i in tqdm(range(1, self.n + 1), desc="Initializing Fenwick Tree", leave=False):
            parent = i + (i & -i)
            if parent <= self.n:
                self.tree[parent] += self.tree[i]

    def update(self, index: int, new_val: int):
        delta = new_val - (self.query_prefix(index) - self.query_prefix(index - 1))
        i = index + 1  # 1-based index
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query_prefix(self, idx: int) -> int:
        res = 0
        i = idx + 1  # 1-based index
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def query_sum(self, l: int, r: int) -> int:
        return self.query_prefix(r) - self.query_prefix(l - 1)