n, m = map(int, input().split())
connected = [[] for _ in range(n)]
visited = set()
toVisit = [0]

for _ in range(m):
    a, b = map(int, input().split())
    connected[a - 1].append(b - 1)
    connected[b - 1].append(a - 1)

while toVisit:
    house = toVisit.pop()
    if house not in visited:
        visited.add(house)
        for neighbor in connected[house]:
            toVisit.append(neighbor)

if len(visited) == n:
    print("Connected")
else:
    for i in range(n):
        if i not in visited:
            print(i + 1)

