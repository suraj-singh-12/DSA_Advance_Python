def find_max_product_pair(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    product_from_end = arr_sorted[n - 1] * arr_sorted[n - 2]
    product_from_start = arr_sorted[0] * arr_sorted[1]
    if product_from_end >= product_from_start:
        return (arr_sorted[n - 2], arr_sorted[n - 1], product_from_end)
    else:
        return (arr_sorted[0], arr_sorted[1], product_from_start)

if __name__ == '__main__':
    arr = [1, 4, 3, 6, 7, 0]
    print("Array:", arr)
    a, b, product = find_max_product_pair(arr)
    print("Maximum Product Pair:", a, "x", b, "=", product)
    arr2 = [-10, -3, 5, 6, -2]
    print("\nArray:", arr2)
    a, b, product = find_max_product_pair(arr2)
    print("Maximum Product Pair:", a, "x", b, "=", product)
