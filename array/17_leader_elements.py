def find_leaders(arr):
    leaders = []
    n = len(arr)
    max_from_right = arr[n - 1]
    leaders.append(arr[n - 1])
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    leaders.reverse()
    return leaders

if __name__ == '__main__':
    arr = [16, 17, 4, 3, 5, 2]
    print("Array:", arr)
    print("Leader Elements:", find_leaders(arr))
