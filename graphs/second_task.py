def get_path(start_node, graph, visited, path):
    path.append(start_node)
    visited.append(start_node)
    next_node = ''
    curr_node_value = 1000
    if graph[start_node]:
        for i in range(len(graph[start_node])):
            if graph[start_node][i] not in visited and number_of_parents[graph[start_node][i]] < curr_node_value:
                curr_node_value = number_of_parents[graph[start_node][i]]
                next_node = graph[start_node][i]

    else:
        return

    get_path(next_node, graph, visited, path)


numb = int(input())
flag = False
graph = {}

for _ in range(numb):
    parent, child = input().split(' -')
    if len(child) >= 3:

        try:
            children = child[2:].split(', ')
        except:
            children = child[2:]
    else:
        children = []

    graph[parent] = children


number_of_parents = {}

for p, c in graph.items():
    if p in number_of_parents.keys():
        number_of_parents[p] += 1

    else:
        number_of_parents[p] = 0

    for child in c:
        if p in graph[child]:
            flag = True
        if child in number_of_parents.keys():
            number_of_parents[child] += 1

        else:
            number_of_parents[child] = 1

if flag:
    print('Invalid topological sorting')

else:
    path = []

    start_node = sorted(number_of_parents.items(), key=lambda x: x[1], reverse=False)[0][0]

    get_path(start_node, graph, [], path)

    print(f"Topological sorting: {', '.join(path)}")
