import time
import random
import pandas as pd

# Deterministic Quicksort using middle element as pivot
# This helps avoid worst-case recursion on sorted arrays
# ---------------------------------------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]  # Select middle element as pivot

    # Using enumerate to loop with index and value
    # So we can exclude the pivot by checking index != mid
    left = [x for i, x in enumerate(arr) if x < pivot and i != mid]
    right = [x for i, x in enumerate(arr) if x >= pivot and i != mid]

    return quicksort(left) + [pivot] + quicksort(right)

# Randomized Quicksort
# Random pivot helps avoid worst-case scenarios
# ---------------------------------------------
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Choose random pivot
    pivot = arr[pivot_index]

    # Using enumerate again to get index and value,
    # which allows us to skip the pivot itself during partitioning
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x >= pivot and i != pivot_index]

    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Benchmark function to measure execution time
# ---------------------------------------------
def benchmark(sort_fn, arr):
    start = time.time()
    sort_fn(arr.copy())  # Sort a copy to preserve original array
    return time.time() - start

# Input sizes and input types for benchmarking
# ---------------------------------------------
sizes = [1000, 5000, 10000]  # Sizes of input arrays to test, it may vary
input_types = {
    "Random": lambda n: random.sample(range(n * 2), n),
    "Sorted": lambda n: list(range(n)),
    "Revers sorted": lambda n: list(range(n, 0, -1)),
}

# Run benchmarks and collect results
# ---------------------------------------------
results = []

for size in sizes:
    for label, generator in input_types.items():
        arr = generator(size)  # Generate input of specified type and size
        dt_time = benchmark(quicksort, arr)  # Deterministic sort
        rnd_time = benchmark(randomized_quicksort, arr)  # Randomized sort

        # Store results in a dictionary
        results.append({
            "Size": size,
            "Input Type": label,
            "Deterministic Time (s)": round(dt_time, 6),
            "Randomized Time (s)": round(rnd_time, 6)
        })

# Display results using pandas
# ---------------------------------------------
df = pd.DataFrame(results)
print("\n\t Quicksort Benchmark Results:\n")
print(df.to_string(index=False))

