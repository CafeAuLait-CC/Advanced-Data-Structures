#
#  demo.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/4/25.
#


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


import matplotlib.pyplot as plt

from src.fenwick_tree import FenwickTree
from src.segment_tree import SegmentTree
from src.sparse_table import SparseTable

from src.generate_data import generate_dataset, generate_operations
from src.helper import parse_args, benchmark_updates, benchmark_queries, print_results


# ----------------- Configuration -----------------
num_runs = 5                     # Number of runs (adjustable)
min_size = 1_000_000             # Minimum dataset size (1 million)
max_size = 10_000_000            # Maximum dataset size (10 million)
num_operations = 10_000          # Number of operations per run
dataset_type = "random"          # Dataset type: "random", "sparse_peaks", "increasing", "decreasing", "all_equal"
max_val = 1000                   # Maximum bandwidth value
# -------------------------------------------------


def main():
    args = parse_args()
    
    # Initialize results storage
    update_results = {
        "Fenwick Tree": {"sizes": [], "times": []},
        "Segment Tree": {"sizes": [], "times": []}
    }
    query_results = {
        "Fenwick Tree (Sum)": {"sizes": [], "times": []},
        "Segment Tree (Sum)": {"sizes": [], "times": []},
        "Segment Tree (Max)": {"sizes": [], "times": []},
        "Sparse Table (Max)": {"sizes": [], "times": []}
    }
    
    # Generate dataset sizes
    if args.full:
        dataset_sizes = [int(min_size + i * (max_size - min_size) / (num_runs - 1)) for i in range(num_runs)]
    else:
        dataset_sizes = [min_size]  # Run only one round
    
    for size in dataset_sizes:
        print(f"\nRunning benchmark for dataset size: {size}")
        
        # Generate data
        print("Generating dataset...", end="\r")
        data = generate_dataset(size, dataset_type, max_val)
        print("Dataset generated.          ")
        
        # Generate update operations
        print("Generating update operations...", end="\r")
        update_ops = generate_operations(size, num_ops=num_operations, query_ratio=0.0)  # 100% updates
        print(f"Generated {len(update_ops)} update operations.          ")
        
        # Generate sum query operations
        print("Generating sum query operations...", end="\r")
        sum_query_ops = generate_operations(size, num_ops=num_operations, query_ratio=1.0, query_type="sum")  # 100% sum queries
        print(f"Generated {len(sum_query_ops)} sum query operations.          ")
        
        # Generate max query operations
        print("Generating max query operations...", end="\r")
        max_query_ops = generate_operations(size, num_ops=num_operations, query_ratio=1.0, query_type="max")  # 100% max queries
        print(f"Generated {len(max_query_ops)} max query operations.          ")
        
        # Initialize data structures
        print("Initializing Fenwick Tree...", end="\r")
        fenwick = FenwickTree(data)
        print("Fenwick Tree initialized.          ")
        
        print("Initializing Segment Tree...", end="\r")
        segment = SegmentTree(data)
        print("Segment Tree initialized.          ")
        
        print("Initializing Sparse Table...", end="\r")
        sparse = SparseTable(data)
        print("Sparse Table initialized.          ")
        
        # Benchmark updates
        print("Benchmarking updates...")
        fenwick_update_time = benchmark_updates(fenwick, update_ops)
        segment_update_time = benchmark_updates(segment, update_ops)
        
        update_results["Fenwick Tree"]["sizes"].append(size)
        update_results["Fenwick Tree"]["times"].append(fenwick_update_time)
        update_results["Segment Tree"]["sizes"].append(size)
        update_results["Segment Tree"]["times"].append(segment_update_time)
        
        # Benchmark sum queries
        print("Benchmarking sum queries...")
        fenwick_sum_time = benchmark_queries(fenwick, sum_query_ops, "sum")
        segment_sum_time = benchmark_queries(segment, sum_query_ops, "sum")
        
        query_results["Fenwick Tree (Sum)"]["sizes"].append(size)
        query_results["Fenwick Tree (Sum)"]["times"].append(fenwick_sum_time)
        query_results["Segment Tree (Sum)"]["sizes"].append(size)
        query_results["Segment Tree (Sum)"]["times"].append(segment_sum_time)
        
        # Benchmark max queries
        print("Benchmarking max queries...")
        segment_max_time = benchmark_queries(segment, max_query_ops, "max")
        sparse_max_time = benchmark_queries(sparse, max_query_ops, "max")
        
        query_results["Segment Tree (Max)"]["sizes"].append(size)
        query_results["Segment Tree (Max)"]["times"].append(segment_max_time)
        query_results["Sparse Table (Max)"]["sizes"].append(size)
        query_results["Sparse Table (Max)"]["times"].append(sparse_max_time)
        
        # Print current benchmark results
        print_results(update_results, query_results, size)
    
    # Generate plots only in full mode
    if args.full:
        # Plot update results
        plt.figure(figsize=(10, 6))
        for name, data in update_results.items():
            plt.plot(data["sizes"], data["times"], marker="o", label=name)
        
        plt.title("Dataset Size vs Update Time")
        plt.xlabel("Dataset Size")
        plt.ylabel("Update Time (seconds)")
        plt.xticks(dataset_sizes, labels=[f"{size:,}" for size in dataset_sizes], rotation=45)
        plt.grid(True, which="both", linestyle="--")
        plt.legend()
        plt.tight_layout()
        plt.savefig("update_results.png")
        print("Update results plotted and saved to 'update_results.png'.          ")
        
        # Plot query results
        plt.figure(figsize=(10, 6))
        for name, data in query_results.items():
            plt.plot(data["sizes"], data["times"], marker="o", label=name)
        
        plt.title("Dataset Size vs Query Time")
        plt.xlabel("Dataset Size")
        plt.ylabel("Query Time (seconds)")
        plt.xticks(dataset_sizes, labels=[f"{size:,}" for size in dataset_sizes], rotation=45)
        plt.grid(True, which="both", linestyle="--")
        plt.legend()
        plt.tight_layout()
        plt.savefig("query_results.png")
        print("Query results plotted and saved to 'query_results.png'.          ")

if __name__ == "__main__":
    main()
