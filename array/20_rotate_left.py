def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    arr.reverse()
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 2
    print("Original Array:", arr)
    print("After Rotating Left by", k, "positions:", rotate_left(arr, k))
