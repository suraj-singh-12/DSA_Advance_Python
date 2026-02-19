def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print("Array:", arr)
    print("Sum of Elements:", sum_of_elements(arr))
