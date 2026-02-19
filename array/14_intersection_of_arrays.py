def find_intersection(arr1, arr2):
    set1 = set(arr1)
    intersection = []
    for num in arr2:
        if num in set1 and num not in intersection:
            intersection.append(num)
    return intersection

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Intersection:", find_intersection(arr1, arr2))
