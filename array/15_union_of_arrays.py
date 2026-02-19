def find_union(arr1, arr2):
    seen = set()
    union = []
    for num in arr1:
        if num not in seen:
            union.append(num)
            seen.add(num)
    for num in arr2:
        if num not in seen:
            union.append(num)
            seen.add(num)
    return union

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Union:", find_union(arr1, arr2))
