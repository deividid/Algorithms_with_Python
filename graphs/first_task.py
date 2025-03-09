
numb = int(input())
graph = []

for _ in range(numb):

    graph.append([int(i) for i in input().split()])


def dfs(node, graph, visited, component):
    if node in visited:
        return

    visited.append(node)

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


all_paths = []
visited = []

for i in range(len(graph)):
    if i not in visited:
        component = []
        dfs(i, graph, visited, component)
        all_paths.append(component)


for component in all_paths:
    print('Connected component:', *component)
