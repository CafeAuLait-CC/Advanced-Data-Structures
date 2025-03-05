#
#  helper.py
#  Advanced Data Structure
#
#  Created by Generative AI (DeepSeek) on 3/4/25.
#


import time
import argparse
import numpy as np
from tqdm import tqdm


def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Benchmark data structures.")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Run the full benchmark with multiple rounds and generate plots."
    )
    return parser.parse_args()


def benchmark_updates(data_structure, operations):
    """
    Benchmark update operations for a data structure.
    Returns: total_time
    """
    start_time = time.perf_counter()
    
    # Progress bar for updates
    with tqdm(total=len(operations), desc="Performing updates", leave=False) as pbar:
        for op in operations:
            data_structure.update(op["index"], op["value"])
            pbar.update(1)
    
    total_time = time.perf_counter() - start_time
    return total_time


def benchmark_queries(data_structure, operations, query_type):
    """
    Benchmark query operations for a data structure.
    Returns: total_time
    """
    start_time = time.perf_counter()
    
    # Progress bar for queries
    with tqdm(total=len(operations), desc=f"Performing {query_type} queries", leave=False) as pbar:
        for op in operations:
            if query_type == "sum":
                data_structure.query_sum(op["l"], op["r"])
            elif query_type == "max":
                data_structure.query_max(op["l"], op["r"])
            pbar.update(1)
    
    total_time = time.perf_counter() - start_time
    return total_time


def print_results(update_results, query_results, dataset_size):
    """
    Print the current benchmark results in a tabular format.
    """
    print("\nCurrent Benchmark Results:")
    print(f"Dataset Size: {dataset_size:,}")
    print("-" * 60)
    print("{:<20} {:<20} {:<20}".format("Data Structure", "Update Time (s)", "Query Time (s)"))
    print("-" * 60)
    
    # Print update results
    for name, data in update_results.items():
        if data["sizes"] and data["sizes"][-1] == dataset_size:
            update_time = data["times"][-1]
            print("{:<20} {:<20.4f} {:<20}".format(name, update_time, "N/A"))
    
    # Print query results
    for name, data in query_results.items():
        if data["sizes"] and data["sizes"][-1] == dataset_size:
            query_time = data["times"][-1]
            print("{:<20} {:<20} {:<20.4f}".format(name, "N/A", query_time))
    
    print("-" * 60)