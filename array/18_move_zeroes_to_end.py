def move_zeroes_to_end(arr):
    insert_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos] = arr[i]
            insert_pos += 1
    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1
    return arr

if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    print("Original Array:", arr)
    print("After Moving Zeroes:", move_zeroes_to_end(arr))
