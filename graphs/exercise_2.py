
def dfs(node, graph, visited, cycle):
    if node in cycle:
        raise Exception

    if node in visited:
        return

    cycle.add(node)
    visited.add(node)

    for c in graph[node]:
        dfs(c, graph, visited, cycle)

    cycle.remove(node)

graph = {}

while True:
    con = input()
    if con == 'End':
        break

    first_node, second_node = con.split('-')
    if first_node not in graph:
        graph[first_node] = []

    if second_node not in graph:
        graph[second_node] = []
    graph[first_node].append(second_node)


visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())

    print('Acyclic: Yes')

except Exception:
    print('Acyclic: No')
