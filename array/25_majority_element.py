def find_majority_element(arr):
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    actual_count = arr.count(candidate)
    if actual_count > len(arr) // 2:
        return candidate
    else:
        return None

if __name__ == '__main__':
    arr = [3, 3, 4, 2, 3, 3, 3]
    print("Array:", arr)
    result = find_majority_element(arr)
    if result is not None:
        print("Majority Element:", result)
    else:
        print("No majority element found")
