def reverse(array):
    if len(array) == 1:
        return array[0]

    result = array.pop() + " " + reverse(array)
    return result


array = input().split(" ")
print(reverse(array))
