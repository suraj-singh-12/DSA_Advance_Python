def find_peak_element(arr):
    n = len(arr)
    if n == 1 or arr[0] >= arr[1]:
        return arr[0]
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    return -1

if __name__ == '__main__':
    arr = [1, 3, 20, 4, 1, 0]
    print("Array:", arr)
    print("Peak Element:", find_peak_element(arr))
