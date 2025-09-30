"""
* @file main.py
* @author Petr Oblouk
* @github https://github.com/peoblouk
* @create date 30-09-2025 - 12:24:11
* @modify date 05-10-2025 - 12:00:00
* @desc [Hlavní soubor pro generování bludiště, spuštění algoritmů a zobrazení výsledků]
"""

import os
import pandas as pd
import maze

if __name__ == "__main__":
    rows, cols = 30, 30
    start, goal = (0, 0), (29, 29)

    # složka na výsledky
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # ------------------------
    # GENEROVÁNÍ S KONTROLOU
    # ------------------------
    valid = False
    seed = 0
    while not valid and seed < 50:
        maze_map = maze.gen_maze(rows, cols, density=0.3, seed=seed)
        maze_map[start] = 0
        maze_map[goal] = 0
        if maze.bfs(maze_map, start, goal, maze.is_free)["path"]:
            valid = True
        else:
            seed += 1

    if not valid:
        print("Nepodařilo se vygenerovat průchozí bludiště.")
        exit()

    # ------------------------
    # SPUŠTĚNÍ ALGORITMŮ
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
    # TABULKA VÝSLEDKŮ
    # ------------------------
    data = []
    for r in results:
        path_len = max(0, len(r["path"]) - 1)
        data.append([r["name"], path_len, len(r["visited"]), round(r["runtime"], 6)])

    df = pd.DataFrame(
        data, columns=["Algoritmus", "Délka cesty", "Prozkoumané uzly", "Čas (s)"]
    )
    print(df)
    df.to_csv(os.path.join(output_dir, "vysledky.csv"), index=False)
