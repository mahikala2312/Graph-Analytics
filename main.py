def journeyToMoon(n, astronaut):
    graph = [[] for _ in range(n)]

    # Create the graph
    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    country_sizes = []

    # Find the size of each country
    for i in range(n):
        if not visited[i]:
            count = 0
            stack = [i]
            visited[i] = True

            while stack:
                person = stack.pop()
                count += 1

                for next_person in graph[person]:
                    if not visited[next_person]:
                        visited[next_person] = True
                        stack.append(next_person)

            country_sizes.append(count)

    # Count pairs from different countries
    answer = 0
    previous = 0

    for size in country_sizes:
        answer += previous * size
        previous += size

    return answer


# Input
n, p = map(int, input().split())

astronaut = []

for i in range(p):
    a, b = map(int, input().split())
    astronaut.append([a, b])

print(journeyToMoon(n, astronaut))