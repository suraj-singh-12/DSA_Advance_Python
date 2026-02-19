def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 3, 2, 4, 5]
    print("Array 1:", arr1)
    print("Is Sorted:", is_sorted(arr1))
    print("Array 2:", arr2)
    print("Is Sorted:", is_sorted(arr2))
