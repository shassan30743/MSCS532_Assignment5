import random
import timeit

# Deterministic Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort Implementation
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Function to run and time both versions of Quicksort
def run_tests():
    # Input sizes
    sizes = [1000, 5000, 10000, 20000]
    
    for size in sizes:
        # Create test arrays
        random_array = [random.randint(1, size) for _ in range(size)]
        sorted_array = list(range(size))
        reverse_sorted_array = list(range(size, 0, -1))

        print(f"\nTesting arrays of size {size}...\n")

        # Timing deterministic Quicksort on random input
        deterministic_random_time = timeit.timeit(lambda: quicksort(random_array.copy()), number=10)
        print(f"Deterministic Quicksort on random array: {deterministic_random_time:.6f} seconds")

        # Timing deterministic Quicksort on sorted input
        deterministic_sorted_time = timeit.timeit(lambda: quicksort(sorted_array.copy()), number=10)
        print(f"Deterministic Quicksort on sorted array: {deterministic_sorted_time:.6f} seconds")

        # Timing deterministic Quicksort on reverse-sorted input
        deterministic_reverse_sorted_time = timeit.timeit(lambda: quicksort(reverse_sorted_array.copy()), number=10)
        print(f"Deterministic Quicksort on reverse-sorted array: {deterministic_reverse_sorted_time:.6f} seconds")

        # Timing randomized Quicksort on random input
        randomized_random_time = timeit.timeit(lambda: randomized_quicksort(random_array.copy()), number=10)
        print(f"Randomized Quicksort on random array: {randomized_random_time:.6f} seconds")

        # Timing randomized Quicksort on sorted input
        randomized_sorted_time = timeit.timeit(lambda: randomized_quicksort(sorted_array.copy()), number=10)
        print(f"Randomized Quicksort on sorted array: {randomized_sorted_time:.6f} seconds")

        # Timing randomized Quicksort on reverse-sorted input
        randomized_reverse_sorted_time = timeit.timeit(lambda: randomized_quicksort(reverse_sorted_array.copy()), number=10)
        print(f"Randomized Quicksort on reverse-sorted array: {randomized_reverse_sorted_time:.6f} seconds")

# Main function to start the test
if __name__ == "__main__":
    run_tests()
