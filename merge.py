def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Splitting the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort() for the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merging the sorted left and right halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0  # Index for the left half
    j = 0  # Index for the right half

    # Comparing elements from the left and right halves and merging them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Appending the remaining elements, if any
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

my_list = [4, 2, 7, 1, 9, 3]
sorted_list = merge_sort(my_list)
print(sorted_list)
