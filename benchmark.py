"""
benchmark.py

Empirical comparison of Deterministic and Randomized Quicksort.

This script:
1. Generates input arrays of different sizes.
2. Tests different input distributions:
      - Random
      - Sorted
      - Reverse-sorted
3. Measures execution time of both versions.
4. Prints comparison results.

Quicksort Implementation and Analysis
"""

import random
import time

# Import sorting functions from quicksort.py
from quicksort import deterministic_quicksort, randomized_quicksort


# ==========================================================
# DATA GENERATION FUNCTION
# ==========================================================

def generate_data(size, case_type):
    """
    Generates test data of a given size and distribution.

    Parameters:
        size (int)       : Number of elements in array
        case_type (str)  : Type of input distribution
                           ("random", "sorted", "reverse")

    Returns:
        list : Generated array
    """

    # Case 1: Random data
    # Generates 'size' integers randomly between 0 and size
    if case_type == "random":
        return [random.randint(0, size) for _ in range(size)]

    # Case 2: Already sorted data (ascending order)
    # Worst case for deterministic quicksort (last element pivot)
    elif case_type == "sorted":
        return list(range(size))

    # Case 3: Reverse sorted data (descending order)
    # Also worst case for deterministic quicksort
    elif case_type == "reverse":
        return list(range(size, 0, -1))


# ==========================================================
# TIME MEASUREMENT FUNCTION
# ==========================================================

def measure_time(sort_function, arr):
    """
    Measures execution time of a sorting function.

    Parameters:
        sort_function : Function reference (deterministic or randomized quicksort)
        arr (list)    : Input array

    Returns:
        float : Time taken in seconds
    """

    # Record start time using high-resolution timer
    start = time.perf_counter()

    # Execute sorting algorithm
    sort_function(arr, 0, len(arr) - 1)

    # Record end time
    end = time.perf_counter()

    # Return elapsed time
    return end - start


# ==========================================================
# MAIN BENCHMARK DRIVER
# ==========================================================

if __name__ == "__main__":

    # Different input sizes to test scalability
    sizes = [1000, 5000, 10000]

    # Different input distributions
    cases = ["random", "sorted", "reverse"]

    # Loop through each input size
    for size in sizes:
        print(f"\nInput Size: {size}")

        # Loop through each input type
        for case in cases:

            # Generate dataset
            data = generate_data(size, case)

            # Create separate copies so both algorithms
            # receive identical input
            arr1 = data.copy()
            arr2 = data.copy()

            # Measure deterministic quicksort time
            time_det = measure_time(deterministic_quicksort, arr1)

            # Measure randomized quicksort time
            time_rand = measure_time(randomized_quicksort, arr2)

            # Print formatted results
            print(
                f"{case.capitalize():10} | "
                f"Deterministic: {time_det:.6f}s | "
                f"Randomized: {time_rand:.6f}s"
            )

"""
Expected Observations:

1. Random input:
   - Both versions should perform around O(n log n).
   - Times should be similar.

2. Sorted input:
   - Deterministic version (last element pivot) may degrade toward O(n^2).
   - Randomized version should remain closer to O(n log n).

3. Reverse-sorted input:
   - Similar behavior to sorted input.

This empirical study validates the theoretical time complexity analysis.
"""