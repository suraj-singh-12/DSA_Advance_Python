def find_kth_smallest(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

if __name__ == '__main__':
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print("Array:", arr)
    print(str(k) + "rd Smallest Element:", find_kth_smallest(arr, k))
