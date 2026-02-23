# Assignment 5 – Quicksort Implementation, Analysis, and Randomization

## Overview

This project implements and analyzes both Deterministic and Randomized versions of the Quicksort algorithm in Python. 

The implementation includes a robustness improvement using **tail recursion elimination** to prevent stack overflow in worst-case scenarios. This ensures the algorithm runs safely even on large sorted or reverse-sorted inputs.

The project includes:

- Deterministic Quicksort
- Randomized Quicksort
- Theoretical time and space complexity analysis
- Empirical performance benchmarking
- Comparison of input distributions

## Repository Structure

Assignment-5-Quicksort/

- quicksort.py → Sorting algorithm implementations  
- benchmark.py → Empirical performance testing  
- report.pdf → Detailed theoretical and experimental analysis  
- README.md → Project documentation  

## Implementation Details

### Deterministic Quicksort

- Uses the **last element as pivot**.
- Implements **tail recursion elimination**.
- Recursively sorts the smaller partition first.
- Iteratively processes the larger partition.
- Guarantees recursion depth of O(log n) instead of O(n).

This prevents Python's default recursion limit from being exceeded during worst-case inputs.

### Randomized Quicksort

- Selects pivot randomly from the subarray.
- Reduces probability of worst-case O(n²).
- Also uses tail recursion elimination.
- Expected time complexity remains O(n log n).

## Time Complexity Analysis

| Case        | Deterministic | Randomized |
|------------|---------------|------------|
| Best Case   | O(n log n)    | O(n log n) |
| Average Case| O(n log n)    | O(n log n) |
| Worst Case  | O(n²)         | O(n²) (rare) |

Worst-case occurs when partitions are highly unbalanced.

Randomization reduces likelihood of encountering worst-case behavior.

## Space Complexity

- In-place sorting (no auxiliary arrays).
- Recursion stack:
  - Average Case: O(log n)
  - Worst Case: O(n)
- With tail recursion elimination, practical recursion depth is reduced to O(log n).

## Empirical Analysis

The benchmark compares both versions on:

- Random inputs
- Sorted inputs
- Reverse-sorted inputs

Input sizes tested:
- 1,000
- 5,000
- 10,000

### Observations

- On random input, both versions perform similarly.
- On sorted/reverse input:
  - Deterministic version slows down.
  - Randomized version performs significantly better.
- Tail recursion elimination prevents stack overflow errors.

## How to Run

### 1. Run basic quicksort test

### 2. Run empirical benchmark
