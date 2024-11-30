def nested(idx, value):
    if idx >= len(value):
        print(*value, sep=" ")
        return

    for i in range(1, len(value) + 1):
        value[idx] = i
        nested(idx + 1, value)


n = int(input())

value = [1] * n
nested(0, value)
