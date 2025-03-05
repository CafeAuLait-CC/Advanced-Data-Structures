'''
Application: Real-Time Network Bandwidth Monitor

Scenario:
A server tracks bandwidth usage (in MB) across n time intervals. The system must:

1. Update bandwidth usage at any interval (dynamic updates).

2. Answer two types of queries:

	- Total bandwidth used in a range [L, R] (sum query).
	- Peak bandwidth in a range [L, R] (max query).


Role of Each Data Structure:

1. Fenwick Tree (BIT):
	- Efficiently compute total bandwidth in [L, R] using prefix sums.
	- Handle point updates (e.g., adjusting usage at a specific interval).


2. Segment Tree:
	- Compute both sum and max over [L, R] with support for updates.
	- Demonstrate flexibility for mixed query types.

3. Sparse Table:
	- Precompute static peak bandwidth (max) for [L, R] (immutable historical data).
	- Highlight its advantage for read-only max queries with O(1) time.
'''

import time
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from generate_data import generate_dataset, generate_operations
from fenwick_tree import FenwickTree
from segment_tree import SegmentTree
from sparse_table import SparseTable

# ----------------- Configuration -----------------
num_runs = 5                     # Number of runs (adjustable)
min_size = 1_000_000             # Minimum dataset size (1 million)
max_size = 10_000_000            # Maximum dataset size (10 million)
num_operations = 10_000          # Number of operations per run
dataset_type = "random"          # Dataset type: "random", "sparse_peaks", etc.
max_val = 1000                   # Maximum bandwidth value
query_ratio = 0.7                # Ratio of queries to updates
# -------------------------------------------------

def benchmark(data_structure, operations, structure_type):
    """
    Benchmark a data structure by applying operations and measuring time.
    Returns: (total_time, processed_ops)
    """
    start_time = time.perf_counter()
    processed_ops = 0
    
    # Progress bar for operations
    with tqdm(total=len(operations), desc=f"Performing {structure_type} operations", leave=False) as pbar:
        for op in operations:
            try:
                if op["type"] == "update":
                    if structure_type in ["fenwick", "segment"]:
                        data_structure.update(op["index"], op["value"])
                        processed_ops += 1
                elif op["type"] == "query_sum":
                    if structure_type == "fenwick":
                        fenwick_sum = data_structure.query_sum(op["l"], op["r"])
                    elif structure_type == "segment":
                        seg_sum = data_structure.query_sum(op["l"], op["r"])  # Call query_sum
                    processed_ops += 1
                elif op["type"] == "query_max":
                    if structure_type == "segment":
                        seg_max = data_structure.query_max(op["l"], op["r"])  # Call query_max
                    elif structure_type == "sparse":
                        sparse_max = data_structure.query_max(op["l"], op["r"])
                    processed_ops += 1
            except:
                pass  # Skip unsupported operations
            pbar.update(1)  # Update progress bar
    
    total_time = time.perf_counter() - start_time
    return total_time, processed_ops

def main():
    # Initialize results storage
    results = {
        "Fenwick Tree": {"sizes": [], "times": []},
        "Segment Tree": {"sizes": [], "times": []},
        "Sparse Table": {"sizes": [], "times": []}
    }
    
    # Generate linearly spaced dataset sizes
    dataset_sizes = [int(min_size + i * (max_size - min_size) / (num_runs - 1)) for i in range(num_runs)]
    
    for size in dataset_sizes:
        print(f"\nRunning benchmark for dataset size: {size}")
        
        # Generate data
        print("Generating dataset...", end="\r")
        data = generate_dataset(size, dataset_type, max_val)
        print("Dataset generated.          ", end="\r")
        
        # Generate operations
        print("Generating operations...", end="\r")
        operations = generate_operations(size, num_ops=num_operations, query_ratio=query_ratio)
        print(f"Generated {len(operations)} operations.          ", end="\r")
        
        # Initialize data structures
        print("Initializing Fenwick Tree...", end="\r")
        fenwick = FenwickTree(data)
        print("Fenwick Tree initialized.          ", end="\r")
        
        print("Initializing Segment Tree...", end="\r")
        segment = SegmentTree(data)
        print("Segment Tree initialized.          ", end="\r")
        
        print("Initializing Sparse Table...", end="\r")
        sparse = SparseTable(data)
        print("Sparse Table initialized.          ", end="\r")
        
        # Benchmark each structure
        for name, struct, stype in [
            ("Fenwick Tree", fenwick, "fenwick"),
            ("Segment Tree", segment, "segment"),
            ("Sparse Table", sparse, "sparse")
        ]:
            print(f"Benchmarking {name}...", end="\r")
            time_taken, ops_processed = benchmark(struct, operations, stype)
            results[name]["sizes"].append(size)
            results[name]["times"].append(time_taken)
            print(f"{name}: {time_taken:.4f} sec, Ops Processed: {ops_processed}/{num_operations}          ")
    
    # Plot results
    print("\nPlotting results...", end="\r")
    plt.figure(figsize=(10, 6))
    for name, data in results.items():
        plt.plot(data["sizes"], data["times"], marker="o", label=name)

    # Set x-axis ticks to match dataset sizes
    plt.xticks(dataset_sizes, labels=[f"{size:,}" for size in dataset_sizes], rotation=45)

    plt.title("Dataset Size vs Execution Time")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    # plt.yscale("log")
    plt.grid(True, which="both", linestyle="--")
    plt.legend()

    # Save the plot
    plt.tight_layout()  # Adjust layout to prevent label overlap
    plt.savefig("benchmark_results.png")
    print("Results plotted and saved to 'benchmark_results.png'.          ")

if __name__ == "__main__":
    main()