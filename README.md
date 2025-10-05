# Projekt: Řešení bludiště (DFS, BFS, A*)

Tento projekt demonstruje a porovnává chování algoritmů **DFS**, **BFS** a **A\*** na procedurálně generovaných bludištích.  
Bludiště mohou být generována náhodně pomocí PRNG generátoru nebo strukturovaně pomocí **Primova algoritmu**.  
Součástí projektu je vizualizace, volba heuristiky, benchmark a export výsledků.

---

<p align="center">
  <img src="gui.png" alt="Ukázka GUI projektu" width="800"/>
</p>

---

## 🔧 Funkce projektu

- **Generování bludišť:**
  - Náhodný generátor (PRNG) s nastavitelnou hustotou (`density`) a seedem (`seed`)
  - Strukturovaný generátor založený na **Primově algoritmu**
- **Implementované algoritmy:**
  - *DFS (Depth-First Search)* – prohledávání do hloubky  
  - *BFS (Breadth-First Search)* – prohledávání do šířky  
  - *A* Search* – heuristické vyhledávání s podporou více heuristik:
    - Manhattanova vzdálenost  
    - Euklidovská vzdálenost  
    - Diagonální vzdálenost  
- **Vizualizace:**
  - Styl „hacker terminálu“ – černé pozadí, zelené zdi, bílé cesty  
  - Společná legenda pro všechny grafy  
  - Výsledky všech algoritmů vykreslené vedle sebe v jednom okně  
- **Benchmark mód** – měří výkon algoritmů na deseti náhodně vygenerovaných bludištích  
- **Export výsledků:**
  - Výpis tabulky v konzoli  
  - Obrázky (`.png`) ve složce `outputs/`  
  - Výsledky (`results.csv`, `benchmark.csv`) uložené do `outputs/`

---

## ▶️ Použití

Program spusť z příkazové řádky:

```
python main.py
Po spuštění program vyzve k zadání parametrů:
```

Choose generator [random / prim] [default: random]: prim
Choose A* heuristic [manhattan / euclidean / diagonal] [default: manhattan]: euclidean
Density of walls (0–1) [default 0.3]: 0.25
Choose seed [default: 0]: 42

## 🧭 Ukázka výstupu v konzoli
✅ Maze successfully generated using: PRIM generator (seed=42)

=== Algorithm Results ===
```
+-----------------+--------------+-----------------+---------+
|   Algorithm     | Path Length  | Explored Nodes  | Time(s) |
+-----------------+--------------+-----------------+---------+
| DFS             |     106      |       518       | 0.0007  |
| BFS             |      60      |       613       | 0.0007  |
| A* (euclidean)  |      60      |       297       | 0.0005  |
+-----------------+--------------+-----------------+---------+
```

Results and images have been saved to the 'outputs' folder.
## 🧠 Benchmark algoritmů
Pro spuštění benchmarku zvlášť (např. v interaktivním prostředí):
```
from main import benchmark_algorithms
benchmark_algorithms("manhattan")
```

Výsledky se uloží do outputs/benchmark.csv a v konzoli se zobrazí průměrné hodnoty:
```
=== Benchmarking algorithms on 10 random mazes (heuristic = manhattan) ===

+-----------------+--------------+-----------------+---------+
|   Algorithm     | Path length  | Explored nodes  | Time(s) |
+-----------------+--------------+-----------------+---------+
| DFS             |     402      |      1320       | 0.0039  |
| BFS             |     105      |      1815       | 0.0125  |
| A* (manhattan)  |     105      |       940       | 0.0084  |
+-----------------+--------------+-----------------+---------+
```

## 📦 Knihovny
```
numpy, matplotlib, pandas, tabulate
```
```
pip install -r requirements.txt
```

## 🗂 Struktura projektu
```
├── maze/
│   ├── __init__.py
│   ├── algorithms.py
│   ├── generator.py
│   ├── visualize.py
├── outputs/
│   ├── DFS.png
│   ├── BFS.png
│   ├── Astar_euclidean.png
│   ├── results.csv
│   ├── benchmark.csv
├── main.py
├── requirements.txt
├── README.md
└── gui.png
```
##📚 Teoretické pozadí
DFS (Depth-First Search)
→ Prohledává do hloubky, rychlý a nenáročný na paměť, ale nemusí najít nejkratší cestu.

BFS (Breadth-First Search)
→ Prohledává do šířky, vždy najde nejkratší cestu, ale je paměťově náročnější.

A*
→ Kombinuje výhody BFS a heuristického odhadu vzdálenosti.
Při vhodně zvolené heuristice (např. Manhattan) je A* optimální a zároveň efektivní.
Jeho výkon a rychlost závisí na použité heuristice.
