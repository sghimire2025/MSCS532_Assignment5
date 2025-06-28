# MSCS532_Assignment5

## Author
- Suresh Ghimire  
- Email: [sghimire38288@ucumberlands.edu]

---

# Part 1: Quicksort Algorithm — Implementation and Analysis

## Overview

This project implements both **Deterministic** and **Randomized** versions of the Quicksort algorithm using Python. It focuses on analyzing their theoretical time and space complexities and validating those insights through empirical benchmarking using different input distributions and sizes.

---

## 1. Implementation

- **Deterministic Quicksort**: Uses the middle element of the array as the pivot.
- **Randomized Quicksort**: Selects a random element as pivot to reduce the likelihood of worst-case scenarios.
- Both versions follow a recursive divide-and-conquer approach:
  - Select a pivot
  - Partition the array
  - Recursively sort the left and right subarrays

---

# Part 2: Empirical Performance Evaluation

This section benchmarks both versions of Quicksort on three input distributions — random, sorted, and reverse sorted — across different array sizes. Results are tabulated and compared to theoretical expectations.

---

## Features

- Clean, recursive implementations of both deterministic and randomized Quicksort.
- Benchmarking setup that:
  - Measures execution time using Python's `time` module
  - Compares results for arrays of size 1,000, 5,000, and 10,000
  - Tests on random, sorted, and reverse-sorted data
- Results are neatly displayed in tabular format using the `pandas` library.

---

## Benchmark Observations

- Both versions perform well on random input, consistent with the average-case time complexity of O(n log n).
- Randomized Quicksort shows more stable performance across input types due to its pivot selection strategy.
- The deterministic version occasionally performs better on sorted inputs, thanks to favorable mid-pivot placement.

---

## How to Run

1. Make sure Python 3.x is installed on your system.
2. Install the required `pandas` library (for result tabulation):
   ```bash
   pip install pandas
   ```
3. Run the script:
   ```bash
   python quick_sort.py
   ```

Note: The script prints all results directly to the terminal.
