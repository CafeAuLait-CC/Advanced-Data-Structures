# Advanced Data Structures - COSC 520 Assignment 2

This project implements and benchmarks three advanced data structures: **Fenwick Tree**, **Segment Tree**, and **Sparse Table**. 

These structures are used to efficiently handle **range sum queries**, **range max queries**, and **point updates** in a simulated network bandwidth monitoring scenario.

---

## Setup

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CafeAuLait-CC/Advanced-Data-Structures.git
   cd Advanced-Data-Structures/
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Dataset

The program generates synthetic datasets to simulate network bandwidth usage across time intervals. The dataset types include:
- **Random**: Random values between 0 and a specified maximum value.
- **Sparse Peaks**: Mostly low values with occasional spikes.
- **Increasing**: Linearly increasing values.
- **Decreasing**: Linearly decreasing values.
- **All Equal**: All values are the same.

The dataset size can range from **1 million to 1 billion elements**, depending on the benchmark configuration.

**Note**: You do not need to download a pre-generated dataset to run the project. When you run the code, it will generate the dataset at runtime within seconds.

---

## Usage

### Running the Benchmark

1. **Single-Round Mode**:
   - Run the benchmark for a single dataset size (default: 1 million elements).
   - No plots are generated.
   ```bash
   python demo.py
   ```

2. **Full Mode**:
   - Run the benchmark for multiple dataset sizes (1M to 10M elements).
   - Generate plots for update and query times.
   ```bash
   python demo.py --full
   ```

### Expected Output

#### Single-Round Mode
```
Running benchmark for dataset size: 1,000,000
Dataset generated.
Generated 10,000 update operations.
Generated 10,000 sum query operations.
Generated 10,000 max query operations.
Fenwick Tree initialized.
Segment Tree initialized.
Sparse Table initialized.
Benchmarking updates...
Benchmarking sum queries...
Benchmarking max queries...

Current Benchmark Results:
Dataset Size: 1,000,000
------------------------------------------------------------
Data Structure       Update Time (s)       Query Time (s)      
------------------------------------------------------------
Fenwick Tree         0.0307                N/A                 
Segment Tree         0.0664                N/A                 
Fenwick Tree (Sum)   N/A                  0.0184               
Segment Tree (Sum)   N/A                  0.0099               
Segment Tree (Max)   N/A                  0.0174               
Sparse Table (Max)   N/A                  0.0043               
------------------------------------------------------------
```

#### Full Mode
```
Running benchmark for dataset size: 1,000,000
...
Current Benchmark Results:
Dataset Size: 1,000,000
------------------------------------------------------------
Data Structure       Update Time (s)       Query Time (s)      
------------------------------------------------------------
Fenwick Tree         0.0311                N/A                 
Segment Tree         0.0655                N/A                 
Fenwick Tree (Sum)   N/A                  0.0185               
Segment Tree (Sum)   N/A                  0.0102               
Segment Tree (Max)   N/A                  0.0175               
Sparse Table (Max)   N/A                  0.0047               
------------------------------------------------------------

Running benchmark for dataset size: 3,250,000
...
Current Benchmark Results:
Dataset Size: 3,250,000
------------------------------------------------------------
Data Structure       Update Time (s)       Query Time (s)      
------------------------------------------------------------
Fenwick Tree         0.0344                N/A                 
Segment Tree         0.0728                N/A                 
Fenwick Tree (Sum)   N/A                  0.0211               
Segment Tree (Sum)   N/A                  0.0113               
Segment Tree (Max)   N/A                  0.0182               
Sparse Table (Max)   N/A                  0.0055               
------------------------------------------------------------
...
Update results plotted and saved to 'update_results.png'.
Query results plotted and saved to 'query_results.png'.
```

After running in the **full** mode, two plots `update_results.png` and `query_results.png` will be saved to the current working directory.

---

## Unit Test

### Running the Tests
To ensure the correctness of the data structures, unit tests are provided for **Fenwick Tree**, **Segment Tree**, and **Sparse Table**.

1. You can run the tests altogether:
   ```bash
   python -m unittest
   ```

2. Or run the tests separately:
   ```bash
   python -m unittest tests/test_fenwick_tree.py
   python -m unittest tests/test_segment_tree.py
   python -m unittest tests/test_sparse_table.py
   ```

### Expected Output
If all tests pass, you’ll see:
```
.....
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

If any test fails, the output will indicate which test failed and why, helping you debug the issue.

---

## Project Structure

```
.
├── demo.py                  # Main script to run benchmarks
├── README.md                # README file
├── requirements.txt         # List of dependencies
├── src/                     # Source code for data structures and helpers
│   ├── __init__.py
│   ├── fenwick_tree.py      # Fenwick Tree implementation
│   ├── generate_data.py     # Dataset and operation generation
│   ├── helper.py            # Benchmarking and plotting utilities
│   ├── segment_tree.py      # Segment Tree implementation
│   └── sparse_table.py      # Sparse Table implementation
└── tests/                   # Unit tests
    ├── __init__.py
    ├── test_fenwick_tree.py # Tests for Fenwick Tree
    ├── test_segment_tree.py # Tests for Segment Tree
    └── test_sparse_table.py # Tests for Sparse Table
```

---

This project provides a comprehensive framework for benchmarking advanced data structures and ensures their correctness through unit tests. Let me know if you need further assistance!

## Acknowledgement

The source code of this project are written by generative AI ([DeepSeek](https://www.deepseek.com))
