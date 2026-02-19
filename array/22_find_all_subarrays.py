def find_all_subarrays(arr):
    subarrays = []
    n = len(arr)
    for start in range(n):
        for end in range(start + 1, n + 1):
            subarrays.append(arr[start:end])
    return subarrays

if __name__ == '__main__':
    arr = [1, 2, 3]
    print("Array:", arr)
    all_subarrays = find_all_subarrays(arr)
    print("Total Subarrays:", len(all_subarrays))
    print("All Subarrays:")
    for sub in all_subarrays:
        print(" ", sub)
