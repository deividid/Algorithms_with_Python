def dfs(node, graph, salary):
    if salary[node] is not None:
        return salary[node]

    if len(graph[node]) == 0:
        salary[node] = 1
        return 1
    sal = 0
    for child in graph[node]:
        sal += dfs(child, graph, salary)

    salary[node] = sal
    return sal


employees = int(input())

graph = []

for _ in range(employees):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)

    graph.append(children)


salary = [None] * employees
total_salary = 0
for node in range(employees):
    total_salary += dfs(node, graph, salary)

print(total_salary)



