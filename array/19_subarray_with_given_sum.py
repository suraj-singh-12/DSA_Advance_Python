def find_subarray_with_sum(arr, target):
    start = 0
    current_sum = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target and start < end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return arr[start:end + 1]
    return []

if __name__ == '__main__':
    arr = [1, 4, 20, 3, 10, 5]
    target = 33
    print("Array:", arr)
    print("Target Sum:", target)
    result = find_subarray_with_sum(arr, target)
    if result:
        print("Subarray with given sum:", result)
    else:
        print("No subarray found")
