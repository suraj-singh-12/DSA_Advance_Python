def rearrange_alternately(arr):
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 1
    take_largest = True
    while left <= right:
        if take_largest:
            result.append(arr[right])
            right -= 1
        else:
            result.append(arr[left])
            left += 1
        take_largest = not take_largest
    return result

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Original Array:", arr)
    print("Rearranged Array:", rearrange_alternately(arr))
