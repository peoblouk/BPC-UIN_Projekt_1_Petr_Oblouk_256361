"""
* @file main.py
* @author Petr Oblouk
* @github https://github.com/peoblouk
* @create date 30-09-2025 - 12:24:11
* @modify date 02-10-2025 - 11:07:10
* @desc [Hlavní soubor pro generování bludiště, spuštění algoritmů a zobrazení výsledků]
"""

import os
import pandas as pd
import maze
from tabulate import tabulate

if __name__ == "__main__":
    rows, cols = 30, 30
    start, goal = (0, 0), (29, 29)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # ------------------------
    # PARAMETERS FROM USER
    # ------------------------
    try:
        density = float(input("Density of walls (0–1) [default 0.3]:") or 0.3)
        seed = int(input("Choose seed [0]: ") or 0)
    except ValueError:
        print("⚠️ Invalid input – using default values.")
        density, seed = 0.3, 0

    # ------------------------
    # GENERATION OF MAZE WITH GUARANTEED PATH
    # ------------------------
    valid = False
    seed = 0
    while not valid and seed < 50:
        maze_map = maze.gen_maze(rows, cols, density=density, seed=seed)
        maze_map[start] = 0
        maze_map[goal] = 0
        if maze.bfs(maze_map, start, goal, maze.is_free)["path"]:
            valid = True
        else:
            seed += 1

    if not valid:
        print("⚠️ Could not generate a valid maze. Try different parameters.")
        exit()

    # ------------------------
    # SOLVING THE MAZE
    # ------------------------
    results = []
    for algo in [maze.dfs, maze.bfs, maze.astar]:
        res = algo(maze_map, start, goal, maze.is_free)
        results.append(res)
        maze.draw_solution(
            maze_map,
            start,
            goal,
            res,
            os.path.join(output_dir, f"{res['name']}.png"),
        )

    # ------------------------
    # TABLE OF RESULTS
    # ------------------------
    data = []
    for r in results:
        path_len = max(0, len(r["path"]) - 1)
        data.append([r["name"], path_len, len(r["visited"]), round(r["runtime"], 6)])

    df = pd.DataFrame(
        data, columns=["Algorithm", "Path Length", "Explored Nodes", "Time (s)"]
    )
    print("\n=== Algorithm Results ===\n")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))

    df.to_csv(os.path.join(output_dir, "results.csv"), index=False)
    print(f"\nResults and images have been saved to the '{output_dir}' folder.")
    maze.show_results_window(maze_map, start, goal, results, df)
