def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


data = [int(num) for num in input().split(" ")]
print(*insertion_sort(data), sep=" ")