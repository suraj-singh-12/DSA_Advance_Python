def find_max_difference(arr):
    if len(arr) < 2:
        return -1
    min_so_far = arr[0]
    max_diff = arr[1] - arr[0]
    best_i = 0
    best_j = 1
    temp_i = 0
    for j in range(1, len(arr)):
        if arr[j] - min_so_far > max_diff:
            max_diff = arr[j] - min_so_far
            best_i = temp_i
            best_j = j
        if arr[j] < min_so_far:
            min_so_far = arr[j]
            temp_i = j
    return max_diff, best_i, best_j

if __name__ == '__main__':
    arr = [2, 3, 10, 6, 4, 8, 1]
    print("Array:", arr)
    diff, i, j = find_max_difference(arr)
    print("Maximum Difference:", diff)
    print("  arr[", j, "] - arr[", i, "] =", arr[j], "-", arr[i], "=", diff)
