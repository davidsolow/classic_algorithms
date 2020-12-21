from random import randint

v = {}
e = 0
with open('data.txt') as file:
    for index, line in enumerate(file):
        numbers = [int(number) for number in line.split()]
        v[numbers[0]] = numbers[1:]
        e += len(numbers[1:])

def random_edge(vertices, total_edges):
    random_edge = randint(0, total_edges - 1)
    for vertex, edges in vertices.items():
        if len(edges) <= random_edge:
            random_edge -= len(edges)
        else:
            from_vertex = vertex
            to_vertex = edges[random_edge]
            return from_vertex, to_vertex

def find_min_cut(vertices, total_edges):
    min_cut = 0
    while len(vertices) > 2:
        vertex_1, vertex_2 = random_edge(vertices, total_edges)
        total_edges -= len(vertices[vertex_1])
        total_edges -= len(vertices[vertex_2])
        vertices[vertex_1].extend(vertices[vertex_2])
        for vertex in vertices[vertex_2]:
            vertices[vertex].remove(vertex_2)
            vertices[vertex].append(vertex_1)
        vertices[vertex_1] = list(filter(lambda v: v != vertex_1, vertices[vertex_1]))
        total_edges += len(vertices[vertex_1])
        vertices.pop(vertex_2)
    for edges in vertices.values():
        min_cut = len(edges)
    return min_cut

results = []
iterations = len(v) * len(v)
for i in range(iterations):
    results.append(find_min_cut(v, e))

print(results)
print(min(results))
print(find_min_cut(v, e))