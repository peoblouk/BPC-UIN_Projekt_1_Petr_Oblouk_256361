"""
* @file generator.py
* @author [Petr Oblouk]
* @github [https://github.com/peoblouk]
* @create date 30-09-2025 - 12:24:11
* @modify date 01-10-2025 - 08:29:31
* @desc [Functions for generating mazes]
"""

import numpy as np


def gen_maze(rows, cols, density=0.3, seed=42):
    rng = np.random.default_rng(seed)
    return (rng.random((rows, cols)) < density).astype(np.uint8)


def in_bounds(maze, r, c):
    return 0 <= r < maze.shape[0] and 0 <= c < maze.shape[1]


def is_free(maze, r, c):
    return in_bounds(maze, r, c) and maze[r, c] == 0
