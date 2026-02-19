def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 5]
    print("Original Array:", arr)
    print("After Removing Duplicates:", remove_duplicates(arr))
