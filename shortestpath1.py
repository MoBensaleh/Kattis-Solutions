from heapq import heappush, heappop

def dijkstra(n, edges, source):
    dist = [float("inf")] * n
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        _, u = heappop(pq)

        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))

    return dist


while True:
    # Read the number of nodes, edges, queries, and the source vertex
    n, m, q, s = map(int, input().split())

    # Check if the input is terminated
    if n == 0 and m == 0 and q == 0 and s == 0:
        break

    # Create a dictionary to store the edges of the graph
    edges = {u: [] for u in range(n)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))

    # Call the Dijkstra function to find the shortest path
    # from the source vertex to every other vertex in the graph
    dist = dijkstra(n, edges, s)

    for _ in range(q):
        query = int(input())
        # If the query vertex is reachable from the source vertex,
        # print the shortest distance from the source vertex to the query vertex
        if dist[query] != float("inf"):
            print(dist[query])
        else:
            print("Impossible")
            
    print()
