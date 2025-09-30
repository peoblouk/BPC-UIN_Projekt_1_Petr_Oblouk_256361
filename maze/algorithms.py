"""
* @file algorithms.py
* @author [Petr Oblouk]
* @github [https://github.com/peoblouk]
* @create date 30-09-2025 - 12:24:11
* @modify date 04-10-2025 - 12:42:32
* @desc [Funkce pro algoritmy pro hledání cesty v bludišti]
"""

import time, math, heapq
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return []
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path if path and path[0] == start else []


def bfs(maze, start, goal, is_free):
    t0 = time.time()
    q = deque([start])
    parent = {start: None}
    visited = {start}

    while q:
        r, c = q.popleft()
        if (r, c) == goal:
            break
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if is_free(maze, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                q.append((nr, nc))

    path = reconstruct_path(parent, start, goal)
    return {
        "name": "BFS",
        "path": path,
        "visited": visited,
        "runtime": time.time() - t0,
    }


def dfs(maze, start, goal, is_free):
    t0 = time.time()
    stack = [start]
    parent = {start: None}
    visited = {start}

    while stack:
        r, c = stack.pop()
        if (r, c) == goal:
            break
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if is_free(maze, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                stack.append((nr, nc))

    path = reconstruct_path(parent, start, goal)
    return {
        "name": "DFS",
        "path": path,
        "visited": visited,
        "runtime": time.time() - t0,
    }


def astar(maze, start, goal, is_free):
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    t0 = time.time()
    open_set = [(0, start)]
    parent = {start: None}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            break

        r, c = current
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            nb = (nr, nc)
            if not is_free(maze, nr, nc):
                continue
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(nb, math.inf):
                parent[nb] = current
                g_score[nb] = tentative_g
                f = tentative_g + manhattan(nb, goal)
                heapq.heappush(open_set, (f, nb))

    path = reconstruct_path(parent, start, goal)
    return {
        "name": "A_STAR",
        "path": path,
        "visited": visited,
        "runtime": time.time() - t0,
    }
