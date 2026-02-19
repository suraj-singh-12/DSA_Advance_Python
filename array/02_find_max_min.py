def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    return max_val, min_val

if __name__ == '__main__':
    arr = [3, 1, 7, 2, 9, 4]
    print("Array:", arr)
    maximum, minimum = find_max_min(arr)
    print("Maximum Element:", maximum)
    print("Minimum Element:", minimum)
