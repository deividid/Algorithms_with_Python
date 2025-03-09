from collections import deque
def bfs(par_row, par_col, row, col, maze, visited, parent, d):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
        return

    if maze[row][col] == '#':
        return

    if visited[row][col]:
        return


    visited[row][col] = True

    parent[row][col] = (par_row, par_col)

    bfs(row, col, row + 1, col, maze, visited, parent, d)
    bfs(row, col, row - 1, col, maze, visited, parent, d)
    bfs(row, col, row, col + 1, maze, visited, parent, d)
    bfs(row, col, row, col - 1, maze, visited, parent,

rows = int(input())

grid = []

for _ in range(rows):
    grid.append(list(input()))

start_pos = []
end_pos = []
for row in range(rows):
    for col in range(rows):
        if grid[row][col] == 'E':

            end_pos.append(row)
            end_pos.append(col)

        if grid[row][col] == 'S':
            start_pos.append(row)
            start_pos.append(col)

visited = []
parent = []

for i in range(rows):
    col_vis = [False] * rows
    col_par = [None] * rows
    visited.append(col_vis)
    parent.append(col_par)


bfs(start_pos[0], start_pos[1], start_pos[0], start_pos[1], grid, visited, parent)

node = parent[end_pos[0]][end_pos[1]]
path = []
while True:
    path.append(node)
    if node[0] == start_pos[0] and node[1] == start_pos[1]:
        break
    node = parent[node[0]][node[1]]

print(len(path))
