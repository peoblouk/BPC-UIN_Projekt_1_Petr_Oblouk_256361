"""
* @file visualize.py
* @author [Petr Oblouk]
* @github [https://github.com/peoblouk]
* @create date 30-09-2025 - 12:24:11
* @modify date 03-10-2025 - 15:19:32
* @desc [Funkce pro vizualizaci bludiště a řešení]
"""

import matplotlib.pyplot as plt
from tabulate import tabulate


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


def show_results_window(maze, start, goal, results, df):
    """
    Zobrazí výsledky všech algoritmů vedle sebe v jednom okně
    + tabulku výsledků pod obrázky.
    """
    fig, axes = plt.subplots(1, len(results), figsize=(5 * len(results), 5))

    if len(results) == 1:
        axes = [axes]  # zajistí iterovatelnost i pro 1 graf

    for ax, res in zip(axes, results):
        ax.imshow(maze, cmap="gray_r")

        if res["visited"]:
            ys = [r for (r, c) in res["visited"]]
            xs = [c for (r, c) in res["visited"]]
            ax.scatter(xs, ys, c="lightblue", s=10)

        if res["path"]:
            ys = [r for (r, c) in res["path"]]
            xs = [c for (r, c) in res["path"]]
            ax.plot(xs, ys, c="green", linewidth=2)

        ax.scatter([start[1]], [start[0]], c="red", marker="s")
        ax.scatter([goal[1]], [goal[0]], c="blue", marker="X")

        ax.set_title(res["name"])
        ax.axis("off")

    # pod grafy tabulka
    plt.figtext(
        0.5,
        -0.05,
        tabulate(df, headers="keys", tablefmt="grid", showindex=False),
        ha="center",
        va="top",
        fontsize=10,
        family="monospace",
    )

    plt.tight_layout()
    plt.show()

