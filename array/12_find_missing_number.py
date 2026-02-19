def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

if __name__ == '__main__':
    arr = [1, 2, 4, 5, 6]
    print("Array:", arr)
    print("Missing Number:", find_missing_number(arr))
