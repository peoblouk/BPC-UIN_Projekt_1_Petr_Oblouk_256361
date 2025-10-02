"""
* @file visualize.py
* @author [Petr Oblouk]
* @github [https://github.com/peoblouk]
* @create date 30-09-2025 - 12:24:11
* @modify date 02-10-2025 - 15:19:32
* @desc [Function for visualizing mazes and their solutions]
"""

import matplotlib.pyplot as plt
from tabulate import tabulate

import matplotlib.pyplot as plt
from tabulate import tabulate
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


def draw_solution(maze, start, goal, result, filename):
    plt.figure(figsize=(6, 6))

    colors = ["black", "#00FF00"]
    plt.imshow(maze, cmap=plt.matplotlib.colors.ListedColormap(colors))

    if result["visited"]:
        ys = [r for (r, c) in result["visited"]]
        xs = [c for (r, c) in result["visited"]]
        plt.scatter(xs, ys, c="#FFFFFF", s=6, alpha=0.5)

    if result["path"]:
        ys = [r for (r, c) in result["path"]]
        xs = [c for (r, c) in result["path"]]
        plt.plot(xs, ys, c="#FFFFFF", linewidth=2.5)

    plt.scatter([start[1]], [start[0]], c="#FFFFFF", marker="s", s=80)

    plt.scatter([goal[1]], [goal[0]], c="#FFFFFF", marker="X", s=80)

    plt.title(result["name"], fontsize=14, fontweight="bold", color="#00FF00")
    plt.axis("off")
    plt.savefig(filename, dpi=200, bbox_inches="tight", facecolor="black")
    plt.close()


def show_results_window(
    maze, start, goal, results, df, window_size=(16, 7), spacing=0.07
):
    fig, axes = plt.subplots(
        1, len(results), figsize=window_size, facecolor="black", constrained_layout=True
    )

    if len(results) == 1:
        axes = [axes]

    for ax, res in zip(axes, results):
        colors = ["black", "#00FF00"]
        ax.imshow(maze, cmap=plt.matplotlib.colors.ListedColormap(colors))
        ax.set_facecolor("black")

        if res["visited"]:
            ys = [r for (r, c) in res["visited"]]
            xs = [c for (r, c) in res["visited"]]
            ax.scatter(xs, ys, c="#FFFFFF", s=6, alpha=0.5)

        if res["path"]:
            ys = [r for (r, c) in res["path"]]
            xs = [c for (r, c) in res["path"]]
            ax.plot(xs, ys, c="#FFFFFF", linewidth=2.5)

        ax.scatter([start[1]], [start[0]], c="#FFFFFF", marker="s", s=80)
        ax.scatter([goal[1]], [goal[0]], c="#FFFFFF", marker="X", s=80)

        ax.set_title(res["name"], fontsize=14, fontweight="bold", color="#00FF00")
        ax.axis("off")

    # Hromadná legenda
    legend_elements = [
        Patch(facecolor="black", edgecolor="black", label="Cesta"),
        Patch(facecolor="#00FF00", edgecolor="#00FF00", label="Zeď"),
        Line2D([0], [0], color="#FFFFFF", lw=2, label="Nalezená cesta"),
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor="#FFFFFF",
            markersize=6,
            label="Visited Nodes",
        ),
        Line2D(
            [0],
            [0],
            marker="s",
            color="w",
            markerfacecolor="#FFFFFF",
            markersize=10,
            label="Start",
        ),
        Line2D(
            [0],
            [0],
            marker="X",
            color="w",
            markerfacecolor="#FFFFFF",
            markersize=10,
            label="Goal",
        ),
    ]
    fig.legend(
        handles=legend_elements,
        loc="upper center",
        ncol=6,
        frameon=False,
        fontsize=10,
        labelcolor="white",
    )

    try:
        manager = plt.get_current_fig_manager()
        manager.window.wm_geometry("+0+0")
    except Exception:
        try:
            manager.window.setGeometry(
                0, 0, manager.window.width(), manager.window.height()
            )
        except Exception:
            pass

    plt.show()
