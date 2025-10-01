<!-- @format -->

# Hledání cest v bludišti

## `algorithms.py`

Obsahuje implementace tří algoritmů pro hledání cest v bludišti.

- **`MOVES`** – definice možných kroků (nahoru, dolů, vlevo, vpravo).
- **`reconstruct_path`** – funkce, která z rodičů (`parent`) poskládá výslednou cestu od cíle ke startu.

### Funkce:

- **`bfs(maze, start, goal, is_free)`**

  - Implementace **Breadth-First Search** (prohledávání do šířky).
  - Používá frontu (`deque`).
  - Najde vždy nejkratší cestu.
  - Prozkoumává hodně uzlů, proto může být pomalejší.

- **`dfs(maze, start, goal, is_free)`**

  - Implementace **Depth-First Search** (prohledávání do hloubky).
  - Používá zásobník (`list` jako stack).
  - Najde nějakou cestu, ale nemusí být optimální.
  - Může být rychlejší u malých bludišť.

- **`astar(maze, start, goal, is_free)`**
  - Implementace **A\*** algoritmu.
  - Používá prioritní frontu (`heapq`).
  - Využívá heuristiku – **Manhattanovu vzdálenost**.
  - Najde optimální cestu efektivněji než BFS, protože prozkoumá méně uzlů.

Každá funkce vrací slovník se strukturou:

```python
{
  "name": "BFS / DFS / A_STAR",
  "path": [...],       # nalezená cesta
  "visited": {...},    # množina navštívených uzlů
  "runtime": 0.00123   # doba běhu v sekundách
}
```

---

## `generator.py`

Starà se o generování a validaci bludiště.

### Funkce:

- **`gen_maze(rows, cols, density=0.3, seed=42)`**

  - Vygeneruje náhodné bludiště s daným počtem řádků a sloupců.
  - `density` určuje hustotu zdí (0 = žádné, 1 = plné).
  - `seed` umožní opakovatelné generování.

- **`in_bounds(maze, r, c)`**

  - Kontrola, zda souřadnice leží uvnitř bludiště.

- **`is_free(maze, r, c)`**
  - Vrací `True`, pokud je na souřadnici volné pole (`0`).

---

## `visualize.py`

Slouží k vizualizaci výsledků algoritmů.

### Funkce:

- **`draw_solution(maze, start, goal, result, filename)`**
  - Vykreslí bludiště:
    - zdi = černé (`1`),
    - volné pole = bílé (`0`),
    - navštívené uzly = modré,
    - výsledná cesta = zelená čára,
    - start = červený čtverec,
    - cíl = modrý křížek.
  - Uloží obrázek do souboru (`filename`).

---

## `__init__.py`

Zajišťuje, aby šel balíček `maze` jednoduše používat.

### Obsah:

```python
from .algorithms import bfs, dfs, astar
from .generator  import gen_maze, is_free
from .visualize  import draw_solution

__all__ = ["bfs", "dfs", "astar", "gen_maze", "is_free", "draw_solution"]
```

Díky tomu jde psát jednoduše:

```python
import maze

maze.bfs(...)
maze.gen_maze(...)
maze.draw_solution(...)
```

---

## `main.py`

Hlavní spouštěcí soubor projektu.

### Postup:

1. Nastaví parametry (`rows`, `cols`, start a cíl).
2. Vytvoří složku `outputs/` pro výsledky.
3. Generuje náhodné bludiště s kontrolou průchodnosti (pomocí BFS).
4. Spustí algoritmy `DFS`, `BFS`, `A*`.
5. Uloží vizualizace do `outputs/`.
6. Vypíše tabulku výsledků do konzole (pomocí `tabulate`) a uloží ji do `outputs/vysledky.csv`.

### Ukázka výsledku v konzoli:

```
=== Výsledky algoritmů ===

+------------+--------------+------------------+---------+
| Algoritmus | Délka cesty  | Prozkoumané uzly | Čas (s) |
+------------+--------------+------------------+---------+
| DFS        |     58       |        312       | 0.0003  |
| BFS        |     42       |        198       | 0.0004  |
| A*         |     42       |        156       | 0.0002  |
+------------+--------------+------------------+---------+

Tabulka byla uložena do: outputs/vysledky.csv
```

---
