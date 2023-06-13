import timeit

def original_missing(arr, n):
    total = (n * (n + 1)) // 2
    return total - sum(arr)

def optimized_missing(arr, n):
    return n * (n + 1) // 2 - sum(arr)

arr = [1, 2, 3, 4, 5]
n = len(arr)

t_original = timeit.timeit("original_missing(arr, n)", setup="from __main__ import original_missing, arr, n")
t_optimized = timeit.timeit("optimized_missing(arr, n)", setup="from __main__ import optimized_missing, arr, n")

print("Original code:", t_original)
print("Optimized code:", t_optimized)
