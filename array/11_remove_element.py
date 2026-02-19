def remove_element(arr, target):
    result = []
    for num in arr:
        if num != target:
            result.append(num)
    return result

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3, 5, 3]
    target = 3
    print("Original Array:", arr)
    print("After Removing", target, ":", remove_element(arr, target))
