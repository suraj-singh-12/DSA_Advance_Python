def find_duplicates(arr):
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

if __name__ == '__main__':
    arr = [1, 2, 3, 2, 4, 5, 3, 6]
    print("Array:", arr)
    print("Duplicate Elements:", find_duplicates(arr))
