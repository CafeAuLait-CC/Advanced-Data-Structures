#
#  generate_data.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/4/25.
#


import numpy as np

def generate_dataset(n: int, dataset_type: str = "random", max_val: int = 1000) -> np.ndarray:
    """
    Generate a dataset of size `n` with values up to `max_val`.
    Supported dataset types: "random", "sparse_peaks", "increasing", "decreasing", "all_equal".
    """
    if dataset_type == "random":
        # Random values between 0 and max_val
        return np.random.randint(0, max_val + 1, dtype=np.int32, size=n)
    
    elif dataset_type == "sparse_peaks":
        # Mostly low values with occasional spikes
        data = np.random.randint(0, max_val // 10, dtype=np.int32, size=n)
        # Add 5% spikes
        num_spikes = n // 20
        spike_indices = np.random.choice(n, size=num_spikes, replace=False)
        data[spike_indices] = np.random.randint(max_val // 2, max_val + 1, size=num_spikes)
        return data
    
    elif dataset_type == "increasing":
        # Linearly increasing values
        return np.linspace(0, max_val, num=n, dtype=np.int32)
    
    elif dataset_type == "decreasing":
        # Linearly decreasing values
        return np.linspace(max_val, 0, num=n, dtype=np.int32)
    
    elif dataset_type == "all_equal":
        # All values equal to max_val / 2
        return np.full(n, max_val // 2, dtype=np.int32)
    
    else:
        raise ValueError(f"Unknown dataset type: {dataset_type}")

def generate_operations(n: int, num_ops: int = 1000, 
                       query_ratio: float = 0.7, 
                       max_query_range: int = 100,
                       query_type: str = "sum") -> list:
    """
    Generate a workload of operations (updates or queries).
    
    Args:
        n: Size of the dataset (for valid indices).
        num_ops: Total number of operations to generate.
        query_ratio: Fraction of operations that are queries (vs updates).
        max_query_range: Maximum range size for queries.
        query_type: Type of query to generate ("sum" or "max").
    
    Returns:
        List of operations formatted as dictionaries.
        Example: {"type": "query_sum", "l": 5, "r": 10}
    """
    if query_type not in ["sum", "max"]:
        raise ValueError("query_type must be 'sum' or 'max'")
    
    # Generate operation types
    if query_ratio == 1.0:
        # Generate only queries
        op_types = np.full(num_ops, "query")
    elif query_ratio == 0.0:
        # Generate only updates
        op_types = np.full(num_ops, "update")
    else:
        # Generate a mix of queries and updates
        op_types = np.random.choice(["query", "update"], size=num_ops, p=[query_ratio, 1 - query_ratio])
    
    # Initialize lists to store operations
    ops = []
    
    # Generate queries
    query_mask = op_types == "query"
    num_queries = np.sum(query_mask)
    if num_queries > 0:
        query_l = np.random.randint(0, n, size=num_queries)
        query_r = np.minimum(query_l + np.random.randint(1, max_query_range, size=num_queries), n-1)
        
        for i in range(num_queries):
            ops.append({
                "type": f"query_{query_type}",  # Only generate the specified query type
                "l": int(query_l[i]),
                "r": int(query_r[i])
            })
    
    # Generate updates
    update_mask = op_types == "update"
    num_updates = np.sum(update_mask)
    if num_updates > 0:
        update_indices = np.random.randint(0, n, size=num_updates)
        update_values = np.random.randint(0, 1000, size=num_updates)
        
        for i in range(num_updates):
            ops.append({
                "type": "update",
                "index": int(update_indices[i]),
                "value": int(update_values[i])
            })
    
    return ops