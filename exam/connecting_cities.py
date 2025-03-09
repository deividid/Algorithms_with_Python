class Road:
    def __init__(self, start, end, weight, is_critical):
        self.start = start
        self.end = end
        self.weight = weight
        self.is_critical = is_critical


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    return node


number_of_cities = int(input())
roads = []

for _ in range(number_of_cities):
    city_input = input().split(' ')
    start_city, end_city, distance = city_input[0], city_input[1], int(city_input[2])
    if len(city_input) > 3:
        new_road = Road(start_city, end_city, distance, True)

    else:
        new_road = Road(start_city, end_city, distance, False)

    roads.append(new_road)

parent = {}
forest = []
for road in roads:
    parent[road.start] = road.start
    parent[road.end] = road.end

critical_roads = [r for r in roads if r.is_critical]

for road in sorted(critical_roads, key=lambda e: e.weight):
    start_root = find_root(parent, road.start)
    end_root = find_root(parent, road.end)
    if start_root != end_root:
        parent[start_root] = end_root
        forest.append(road)

for road in sorted(roads, key=lambda e: e.weight):
    start_root = find_root(parent, road.start)
    end_root = find_root(parent, road.end)
    if start_root != end_root:
        parent[start_root] = end_root
        forest.append(road)

total_distance = 0

for road in forest:
    total_distance += road.weight

print(total_distance)