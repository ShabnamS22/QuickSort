"""
quicksort.py

Deterministic and Randomized Quicksort Implementation
Quicksort Implementation and Analysis
"""

import random
import time


# ==========================================================
# PART 1: DETERMINISTIC QUICKSORT
# ==========================================================

def partition(arr, low, high):
    """
    Partition function using last element as pivot.

    Parameters:
        arr  : list of elements
        low  : starting index
        high : ending index

    Returns:
        pivot_index : final index of the pivot
    """

    # Choose last element as pivot
    pivot = arr[high]

    # i is index of smaller element
    i = low - 1

    # Traverse through all elements
    for j in range(low, high):
        # If current element is smaller than pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quicksort(arr, low, high):
    """
    Deterministic Quicksort (recursive using tail recursion elimination).

    Parameters:
        arr  : list to sort
        low  : starting index
        high : ending index
    Instead of recursively sorting both sides,
    recurse on the smaller side and iterate on larger side,
    gurantees recursion depth O(log n).
    """

    while low < high:
        # Partition array
        pivot_index = partition(arr, low, high)

        # Recur on smaller subarray first 
        if pivot_index - low < high - pivot_index:

            # Left side is smaller
            deterministic_quicksort(arr, low, pivot_index - 1)

            # Move to right side iteratively
            low = pivot_index + 1

        else: 

            # Right side is smaller
            deterministic_quicksort(arr, pivot_index + 1, high)

            # Move to left sidee iteratively
            high = pivot_index - 1

        

# ==========================================================
# PART 2: RANDOMIZED QUICKSORT
# ==========================================================

def randomized_partition(arr, low, high):
    """
    Randomized partition:
    Selects a random pivot and swaps with last element.
    """

    # Choose random index between low and high
    random_index = random.randint(low, high)

    # Swap random pivot with last element
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # Use regular partition logic
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    """
    Randomized Quicksort (recursive).
    """

    while low < high:
        pivot_index = randomized_partition(arr, low, high)

        if pivot_index - low < high - pivot_index:

            randomized_quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1

        else:

            randomized_quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1


# ==========================================================
# PART 3: TEST DRIVER
# ==========================================================

if __name__ == "__main__":

    # Example test
    test_array = [10, 7, 8, 9, 1, 5]

    print("Original Array:", test_array)

    arr_copy = test_array.copy()
    deterministic_quicksort(arr_copy, 0, len(arr_copy) - 1)
    print("Sorted (Deterministic):", arr_copy)

    arr_copy = test_array.copy()
    randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
    print("Sorted (Randomized):", arr_copy)