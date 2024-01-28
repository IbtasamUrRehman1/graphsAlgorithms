import heapq
from collections import defaultdict

def generate_graph():
    graph = defaultdict(dict)
    graph['A'] = {'B': 3, 'C': 2}
    graph['B'] = {'A': 1, 'C': 4, 'D': 2}
    graph['C'] = {'D': 5}
    graph['D'] = {'B': 1}
    return graph

def bellman_ford(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Generate a weighted graph
graph = generate_graph()

# Apply Bellman-Ford algorithm
start_node = 'A'
bellman_ford_distances = bellman_ford(graph, start_node)
print(f"Bellman-Ford distances from node {start_node}: {bellman_ford_distances}")

# Apply Dijkstra's algorithm
dijkstra_distances = dijkstra(graph, start_node)
print(f"Dijkstra's distances from node {start_node}: {dijkstra_distances}")
