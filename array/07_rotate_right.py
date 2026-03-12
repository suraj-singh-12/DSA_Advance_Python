def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    arr.reverse()
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 3
    print("Original Array:", arr)
    print("After Rotating Right by", k, "positions:", rotate_right(arr, k))
