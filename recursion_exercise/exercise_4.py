def connected_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] == '*':
        return 0

    if matrix[row][col] == 'v':
        return 0

    matrix[row][col] = 'v'
    result = 1

    result += connected_area(row + 1, col, matrix)
    result += connected_area(row - 1, col, matrix)
    result += connected_area(row, col + 1, matrix)
    result += connected_area(row, col - 1, matrix)

    return result


rows = int(input())
columns = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

result = {}
for row in range(rows):
    for col in range(columns):
        size = connected_area(row, col, matrix)
        if size > 0:
            result[(row, col)] = size

print(f"Total areas found: {len(result)}")

result = sorted(result.items(), key=lambda x: x[1], reverse=True)

for i in range(len(result)):
    print(f"Area #{i + 1} at {result[i][0]}, size: {result[i][1]}")