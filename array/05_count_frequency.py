def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

if __name__ == '__main__':
    arr = [1, 2, 2, 3, 3, 3, 4]
    print("Array:", arr)
    freq = count_frequency(arr)
    print("Frequency of each element:")
    for element, count in freq.items():
        print(" ", element, "->", count, "times")
