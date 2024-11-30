lookup_table = {}
def get_fibonacci(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n in lookup_table.keys():
        return lookup_table[n]

    result = get_fibonacci(n - 1) + get_fibonacci(n - 2)
    lookup_table[n] = result
    return result


index = int(input())
print(get_fibonacci(index))

