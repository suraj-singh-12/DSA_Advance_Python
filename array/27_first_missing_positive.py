def first_missing_positive(arr):
    n = len(arr)
    for i in range(n):
        num = abs(arr[i])
        if 1 <= num <= n:
            index = num - 1
            if arr[index] > 0:
                arr[index] = -arr[index]
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    return n + 1

if __name__ == '__main__':
    arr = [3, 4, -1, 1]
    print("Array:", arr)
    print("First Missing Positive:", first_missing_positive(arr))
    arr2 = [1, 2, 0]
    print("Array:", arr2)
    print("First Missing Positive:", first_missing_positive(arr2))
