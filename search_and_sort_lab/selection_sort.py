def selection_sort(arr):

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


data = [int(num) for num in input().split(" ")]
print(*selection_sort(data), sep=" ")
