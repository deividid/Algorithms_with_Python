import math
from queue import PriorityQueue


class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = int(distance)


def get_path(start, end, par, path):
    path.append(end)

    if par[end] == start:
        path.append(par[end])
        return path

    get_path(start, par[end], par, path)


number_of_roads = int(input())

graph = {}

for _ in range(number_of_roads):
    start, end, distance = input().split(' - ')
    road_1 = Road(start, end, distance)
    road_2 = Road(end, start, distance)
    if start not in graph:
        graph[start] = []

    if end not in graph:
        graph[end] = []

    graph[start].append(road_1)
    graph[end].append(road_2)


closed_roads = input().split(', ')

start_point = input()
end_point = input()


distances = {}
parent = {}

for name in graph.keys():
    distances[name] = math.inf
    parent[name] = None


pq = PriorityQueue()

pq.put((0, start_point))

while not pq.empty():
    min_dist, node = pq.get()
    if node == end_point:
        break

    for road in graph[node]:
        road_name = road.start + '-' + road.end
        if road_name in closed_roads:
            continue
        new_dist = min_dist + road.distance
        if new_dist < distances[road.end]:
            distances[road.end] = new_dist
            parent[road.end] = node
            pq.put((new_dist, road.end))


path = []
get_path(start_point, end_point, parent, path)

correct_order = []

for i in range(len(path) - 1, -1, -1):
    correct_order.append(path[i])

print(*correct_order, sep=' - ')

print(distances[end_point])
