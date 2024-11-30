def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr


data = [int(num) for num in input().split(" ")]
print(*bubble_sort(data), sep=" ")