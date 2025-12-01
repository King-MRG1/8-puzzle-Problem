# 8-Puzzle Solver

An intelligent solution to the classic 8-puzzle problem using six different search algorithms: A\* Search, Breadth-First Search (BFS), Depth-First Search (DFS), Bidirectional Search, Iterative Deepening DFS (IDDFS), and Greedy Best-First Search (GBFS).

## 📋 Problem Description

The 8-puzzle is a sliding puzzle that consists of a 3×3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles from a given initial configuration to reach the goal state by sliding tiles into the blank space.

**Goal State:**

```
1 2 3
4 5 6
7 8 0
```

where `0` represents the blank space.

### Problem Characteristics

- **State Space:** Each state is a unique arrangement of the tiles (9! / 2 = 181,440 reachable states)
- **Actions:** Move the blank space Up, Down, Left, or Right (2-4 possible moves per state)
- **Path Cost:** Each move has a uniform cost of 1
- **Challenge:** Finding the optimal solution efficiently among thousands of possible states

## 🔍 Search Algorithms

### 1. A\* Search (A-Star)

**Type:** Informed Search Algorithm

**How it Works:**

- Uses a heuristic function to guide the search toward the goal
- Evaluates states using: `f(n) = g(n) + h(n)`
  - `g(n)`: Cost from start to current state (number of moves)
  - `h(n)`: Manhattan distance heuristic (estimated cost to goal)
  - `f(n)`: Total estimated cost

**Manhattan Distance Heuristic:**
Calculates the sum of horizontal and vertical distances each tile must travel to reach its goal position.

**Characteristics:**

- ✅ **Optimal:** Guarantees shortest solution path
- ✅ **Efficient:** Explores fewer nodes than uninformed search
- ✅ **Complete:** Always finds a solution if one exists
- 📊 **Performance:** Typically explores 50-200 nodes for moderate puzzles

**Best Used When:** You need the optimal solution with reasonable computational efficiency.

---

### 2. Breadth-First Search (BFS)

**Type:** Uninformed Search Algorithm

**How it Works:**

- Explores all nodes at depth `d` before exploring nodes at depth `d+1`
- Uses a FIFO (First-In-First-Out) queue
- Systematically expands the search frontier level by level

**Characteristics:**

- ✅ **Optimal:** Guarantees shortest solution path (for uniform cost)
- ✅ **Complete:** Always finds a solution if one exists
- ⚠️ **Memory Intensive:** Stores all nodes at current depth level
- 📊 **Performance:** May explore 500-2000+ nodes for moderate puzzles

**Best Used When:** You need guaranteed optimal solution and have sufficient memory resources.

---

### 3. Depth-First Search (DFS)

**Type:** Uninformed Search Algorithm

**How it Works:**

- Explores as far as possible along each branch before backtracking
- Uses a LIFO (Last-In-First-Out) stack
- Implements depth limiting (max depth = 50) to prevent infinite loops

**Characteristics:**

- ❌ **Not Optimal:** May find longer paths to the goal
- ✅ **Memory Efficient:** Only stores nodes along current path
- ⚠️ **Incomplete:** May fail on difficult puzzles due to depth limit
- 📊 **Performance:** Variable; may explore 100-1000+ nodes

**Best Used When:** Memory is severely constrained and suboptimal solutions are acceptable.

---

### 4. Bidirectional Search

**Type:** Informed Search Algorithm

**How it Works:**

- Runs two simultaneous BFS searches from both start and goal states
- Searches meet in the middle, significantly reducing search space
- Terminates when the two frontiers intersect

**Characteristics:**

- ✅ **Optimal:** Guarantees shortest solution path
- ✅ **Efficient:** Much faster than single-direction BFS
- ✅ **Complete:** Always finds a solution if one exists
- 📊 **Performance:** Typically explores 200-500 nodes for moderate puzzles

**Best Used When:** You need optimal solutions faster than standard BFS.

---

### 5. Iterative Deepening DFS (IDDFS)

**Type:** Uninformed Search Algorithm

**How it Works:**

- Combines DFS's space efficiency with BFS's optimality
- Repeatedly performs depth-limited DFS with increasing depth limits (0 to 50)
- Finds optimal solution with minimal memory usage

**Characteristics:**

- ✅ **Optimal:** Guarantees shortest solution path
- ✅ **Memory Efficient:** Only stores nodes along current path
- ✅ **Complete:** Always finds a solution within depth limit
- 📊 **Performance:** Typically explores 300-800 nodes for moderate puzzles

**Best Used When:** You need optimal solutions with limited memory.

---

### 6. Greedy Best-First Search (GBFS)

**Type:** Informed Search Algorithm

**How it Works:**

- Uses only the heuristic function to guide search: `f(n) = h(n)`
- Selects nodes that appear closest to the goal (Manhattan distance)
- Does not consider actual path cost `g(n)`

**Characteristics:**

- ❌ **Not Optimal:** May find longer paths to the goal
- ✅ **Very Fast:** Often finds solutions quickly
- ⚠️ **Incomplete:** May fail without cycle detection
- 📊 **Performance:** Typically explores 30-80 nodes for moderate puzzles

**Best Used When:** Speed is critical and suboptimal solutions are acceptable.

---

## 🆚 Algorithm Comparison

| Criterion         | A\*         | BFS         | DFS            | Bidirectional | IDDFS         | GBFS             |
| ----------------- | ----------- | ----------- | -------------- | ------------- | ------------- | ---------------- |
| **Optimality**    | ✅ Optimal  | ✅ Optimal  | ❌ Not Optimal | ✅ Optimal    | ✅ Optimal    | ❌ Not Optimal   |
| **Completeness**  | ✅ Complete | ✅ Complete | ⚠️ Limited     | ✅ Complete   | ✅ Complete   | ⚠️ Limited       |
| **Memory Usage**  | 🟡 Medium   | 🔴 High     | 🟢 Low         | 🟡 Medium     | 🟢 Low        | 🟢 Low-Medium    |
| **Speed**         | 🟢 Fast     | 🔴 Slow     | 🟡 Variable    | 🟢 Very Fast  | 🟢 Good       | 🟢 Very Fast     |
| **Visited Nodes** | 🟢 Low-Med  | 🔴 High     | 🟡 Variable    | 🟢 Low        | 🟡 Medium     | 🟢 Low           |
| **Best For**      | General use | Guaranteed  | Memory limited | Fast optimal  | Space-limited | Fast non-optimal |

### Example Performance (12-move solution):

**A\* Search:**

- Moves: 12 (optimal)
- Visited Nodes: ~80
- Execution Time: <0.1s

**BFS:**

- Moves: 12 (optimal)
- Visited Nodes: ~1,200
- Execution Time: ~0.3s

**DFS:**

- Moves: 35-45 (non-optimal)
- Visited Nodes: ~400
- Execution Time: Variable

**Bidirectional Search:**

- Moves: 12 (optimal)
- Visited Nodes: ~300
- Execution Time: ~0.15s

**IDDFS:**

- Moves: 12 (optimal)
- Visited Nodes: ~500
- Execution Time: ~0.2s

**GBFS:**

- Moves: 12-18 (often non-optimal)
- Visited Nodes: ~50
- Execution Time: <0.1s

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- Tkinter (included with Python)

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd 8-puzzle
   ```
3. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```

### Running the Application

```bash
python main.py
```

---

## 🎮 How to Use

1. **Enter Puzzle Configuration:**

   - Input numbers 0-8 in the 3×3 grid (0 = blank)
   - Or use preset buttons: Easy, Medium, Hard

2. **Choose Search Algorithm:**

   - Select from 6 algorithms: A\*, BFS, DFS, Bidirectional, IDDFS, or GBFS
   - Algorithms are organized in a two-column layout for easy selection

3. **Solve:**

   - Click "🔍 SOLVE PUZZLE" to find solution with selected algorithm
   - Click "📊 COMPARE ALL" to run all six algorithms and compare results

4. **View Results:**
   - See step-by-step visualization of the solution path
   - Review performance metrics: visited nodes, number of steps
   - Compare algorithm-specific information: f(n), g(n), h(n) values

---

## 📊 Features

- **Interactive GUI:** Modern dark-themed interface with two-column algorithm layout
- **Six Search Algorithms:** Compare different search strategies (informed & uninformed)
- **Step-by-Step Visualization:** Watch how each algorithm solves the puzzle
- **Enhanced Metrics:** Visited nodes and number of steps tracking
- **Algorithm-Specific Display:** Shows f(n), g(n), h(n) for informed algorithms
- **Performance Comparison:** Side-by-side comparison of all six algorithms
- **Preset Puzzles:** Test with easy, medium, and hard difficulty levels

---

## 🏗️ Project Structure

```
8-puzzle/
├── design/                  # GUI and visualization components
│   ├── gui_interface.py     # Main GUI with dark mode
│   └── visualizer.py        # Solution visualization
├── reports/                 # Project documentation and reports
│   ├── generate_report.py   # PDF report generator
│   └── 8-Puzzle_Solver_Report.pdf
├── astar_solver.py          # A* search implementation
├── bfs_solver.py            # BFS implementation
├── dfs_solver.py            # DFS implementation
├── bidirectional_solver.py  # Bidirectional search implementation
├── iddfs_solver.py          # IDDFS implementation
├── greedy_solver.py         # GBFS implementation
├── puzzle_state.py          # State representation
├── main.py                  # Application entry point
└── README.md                # This file
```
