def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.
    """

    # If start == goal:
    # Only return [start] if the room actually exists.
    if start == goal:
        if start in rooms:
            return [start]
        else:
            return []

    # Build adjacency list
    graph = {r: [] for r in rooms}
    for a, b in doors:
        if a in graph:
            graph[a].append(b)
        if b in graph:
            graph[b].append(a)

    from collections import deque
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # BFS
    while queue:
        node = queue.popleft()

        if node == goal:
            break

        if node not in graph:
            continue  # Node is not a valid room

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                parent[nei] = node
                queue.append(nei)

    # If goal was never visited → no path
    if goal not in parent:
        return []

    # Reconstruct path
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path


if __name__ == "__main__":
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
