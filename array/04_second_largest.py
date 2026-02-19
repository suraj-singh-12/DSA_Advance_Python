def find_second_largest(arr):
    largest = arr[0]
    second_largest = None
    for num in arr:
        if num > largest:
            largest = num
    for num in arr:
        if num == largest:
            continue
        if second_largest is None or num > second_largest:
            second_largest = num
    return second_largest

if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 1]
    print("Array:", arr)
    print("Second Largest Element:", find_second_largest(arr))
