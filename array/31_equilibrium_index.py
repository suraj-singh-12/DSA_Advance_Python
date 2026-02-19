def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1

if __name__ == '__main__':
    arr = [1, 7, 3, 6, 5, 6]
    print("Array:", arr)
    index = find_equilibrium_index(arr)
    if index != -1:
        print("Equilibrium Index:", index, "(element =", arr[index], ")")
    else:
        print("No equilibrium index found")
