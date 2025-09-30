"""
* @file visualize.py
* @author [Petr Oblouk]
* @github [https://github.com/peoblouk]
* @create date 30-09-2025 - 12:24:11
* @modify date 03-10-2025 - 15:19:32
* @desc [Funkce pro vizualizaci bludiště a řešení]
"""

import matplotlib.pyplot as plt


def draw_solution(maze, start, goal, result, filename):
    plt.figure(figsize=(6, 6))
    plt.imshow(maze, cmap="gray_r")

    if result["visited"]:
        ys = [r for (r, c) in result["visited"]]
        xs = [c for (r, c) in result["visited"]]
        plt.scatter(xs, ys, c="lightblue", s=10, label="Visited")

    if result["path"]:
        ys = [r for (r, c) in result["path"]]
        xs = [c for (r, c) in result["path"]]
        plt.plot(xs, ys, c="green", linewidth=2, label="Path")

    plt.scatter([start[1]], [start[0]], c="red", marker="s", label="Start")
    plt.scatter([goal[1]], [goal[0]], c="blue", marker="X", label="Goal")
    plt.legend()
    plt.title(result["name"])
    plt.axis("off")
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()
