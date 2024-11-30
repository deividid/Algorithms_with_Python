def binary_search(arr, num):
    begin = 0
    end = len(arr)-1

    while begin <= end:
        middle = (end + begin) // 2
        if arr[middle] == num:
            return middle

        elif arr[middle] < num:
            begin = middle + 1

        else:
            end = middle - 1

    return -1


data = [int(num) for num in input().split(" ")]
n = int(input())

print(binary_search(data, n))
