"""
* @file main.py
* @author Petr Oblouk
* @github https://github.com/peoblouk
* @create date 30-09-2025 - 12:24:11
* @modify date 06-10-2025 - 14:28:02
* @desc [Hlavní soubor pro generování bludiště, spuštění algoritmů a zobrazení výsledků]
"""

import os
import pandas as pd
import maze
from tabulate import tabulate


def benchmark_algorithms(heuristic: str):
    print(
        f"\n=== Benchmarking algorithms on 10 random mazes (heuristic = {heuristic}) ===\n"
    )

    results = []
    for seed in range(10):
        maze_map = maze.gen_maze(30, 30, density=0.3, seed=seed)
        for algo in [
            maze.dfs,
            maze.bfs,
            lambda m, s, g, f: maze.astar(m, s, g, f, heuristic),
        ]:
            res = algo(maze_map, (0, 0), (29, 29), maze.is_free)
            if res["path"]:
                results.append(
                    [res["name"], len(res["path"]), len(res["visited"]), res["runtime"]]
                )

    if not results:
        print("⚠️ No valid results found.")
        return

    df = pd.DataFrame(
        results, columns=["Algorithm", "Path length", "Explored nodes", "Time (s)"]
    )

    # průměry podle algoritmu
    avg = df.groupby("Algorithm").mean().reset_index()
    avg["Path length"] = avg["Path length"].astype(int)
    avg["Explored nodes"] = avg["Explored nodes"].astype(int)
    avg["Time (s)"] = avg["Time (s)"].round(5)

    print(tabulate(avg, headers="keys", tablefmt="pretty", showindex=False))

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/benchmark.csv", index=False)
    print("\nBenchmark saved as: outputs/benchmark.csv\n")


if __name__ == "__main__":
    rows, cols = 30, 30
    start, goal = (0, 0), (29, 29)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # ------------------------
    # USER PARAMETERS
    # ------------------------
    try:
        heuristic = (
            input(
                "Choose A* heuristic [manhattan / euclidean / diagonal] [default: manhattan]: "
            )
            .strip()
            .lower()
            or "manhattan"
        )
        density = float(input("Density of walls (0–1) [default 0.3]: ") or 0.3)
        seed = int(input("Choose seed [default: 0]: ") or 0)
    except ValueError:
        print("⚠️ Invalid input – using default values.")
        generator_type, density, seed, heuristic = "random", 0.3, 0, "manhattan"

    # ------------------------
    # MAZE GENERATION (WITH VALID PATH)
    # ------------------------
    valid = False
    attempts = 0

    while not valid and attempts < 50:
        maze_map = maze.gen_maze(rows, cols, density=density, seed=seed)
        maze_map[start] = 0
        maze_map[goal] = 0

        if maze.bfs(maze_map, start, goal, maze.is_free)["path"]:
            valid = True
        else:
            seed += 1
            attempts += 1

    if not valid:
        print("⚠️ Could not generate a valid maze. Try different parameters.")
        exit()

    # ------------------------
    # SOLVING THE MAZE
    # ------------------------
    results = []
    for algo in [
        maze.dfs,
        maze.bfs,
        lambda m, s, g, f: maze.astar(m, s, g, f, heuristic),
    ]:
        res = algo(maze_map, start, goal, maze.is_free)
        results.append(res)

        safe_name = (
            res["name"]
            .replace("*", "Astar")
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
        )

        maze.draw_solution(
            maze_map,
            start,
            goal,
            res,
            os.path.join(output_dir, f"{safe_name}.png"),
        )

    # ------------------------
    # RESULTS TABLE
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
    print(f"\nResults and images have been saved to the '{output_dir}' folder.\n")

    # ------------------------
    # BENCHMARK AND VISUALIZATION
    # ------------------------
    benchmark_algorithms(heuristic)
    maze.show_results_window(maze_map, start, goal, results, df)
