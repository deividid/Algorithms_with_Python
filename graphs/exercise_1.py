def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if visited[row][col]:
        return

    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)


rows = int(input())
columns = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(input())
    visited.append([False] * columns)

result = {}
for i in range(rows):
    for j in range(columns):
        if visited[i][j]:
            continue

        if matrix[i][j] in result:
            result[matrix[i][j]] += 1

        else:
            result[matrix[i][j]] = 1

        dfs(matrix[i][j], i, j, matrix, visited)


print(f"Areas: {sum(result.values())}")

for key, value in sorted(result.items(), key=lambda x: x[0]):
    print(f"Letter '{key}' -> {value}")
