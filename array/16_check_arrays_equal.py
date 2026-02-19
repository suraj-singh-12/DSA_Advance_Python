def arrays_are_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    sorted1 = sorted(arr1)
    sorted2 = sorted(arr2)
    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False
    return True

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 1, 4, 2]
    arr3 = [1, 2, 3, 4, 6]
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Array 1 == Array 2:", arrays_are_equal(arr1, arr2))
    print("Array 1:", arr1)
    print("Array 3:", arr3)
    print("Array 1 == Array 3:", arrays_are_equal(arr1, arr3))
