# 8-Puzzle Solver

An intelligent solution to the classic 8-puzzle problem using three different search algorithms: A\* Search, Breadth-First Search (BFS), and Depth-First Search (DFS).

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

## 🆚 Algorithm Comparison

| Criterion          | A\* Search      | BFS                 | DFS                 |
| ------------------ | --------------- | ------------------- | ------------------- |
| **Optimality**     | ✅ Optimal      | ✅ Optimal          | ❌ Not Optimal      |
| **Completeness**   | ✅ Complete     | ✅ Complete         | ⚠️ Limited by depth |
| **Memory Usage**   | 🟡 Medium       | 🔴 High             | 🟢 Low              |
| **Speed**          | 🟢 Fast         | 🔴 Slow             | 🟡 Variable         |
| **Nodes Explored** | 🟢 Low-Medium   | 🔴 High             | 🟡 Variable         |
| **Best For**       | General purpose | Guaranteed shortest | Memory constrained  |

### Example Performance (12-move solution):

**A\* Search:**

- Moves: 12 (optimal)
- Nodes Explored: ~80
- Execution Time: <0.1s

**BFS:**

- Moves: 12 (optimal)
- Nodes Explored: ~1,200
- Execution Time: ~0.3s

**DFS:**

- Moves: 35-45 (non-optimal)
- Nodes Explored: ~400
- Execution Time: Variable

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

   - Select A\*, BFS, or DFS using radio buttons

3. **Solve:**

   - Click "🔍 SOLVE PUZZLE" to find solution with selected algorithm
   - Click "📊 COMPARE ALL" to run all three algorithms and compare results

4. **View Results:**
   - See step-by-step visualization of the solution path
   - Review performance metrics: moves, nodes explored, efficiency

---

## 📊 Features

- **Interactive GUI:** Modern dark-themed interface for easy interaction
- **Multiple Algorithms:** Compare three different search strategies
- **Step-by-Step Visualization:** Watch how each algorithm solves the puzzle
- **Performance Metrics:** Analyze nodes explored, moves, and efficiency
- **Preset Puzzles:** Test with easy, medium, and hard difficulty levels
- **Algorithm Comparison:** Side-by-side performance comparison tool

---

## 🏗️ Project Structure

```
8-puzzle/
├── design/              # GUI and visualization components
├── reports/             # Project documentation and reports
├── astar_solver.py      # A* search implementation
├── bfs_solver.py        # BFS implementation
├── dfs_solver.py        # DFS implementation
├── puzzle_state.py      # State representation
└── main.py              # Application entry point
```

---

## 👥 Team

- **Mohamed Ahmed Ramadan** - 23015430
- **Mohamed Mahmoud Ibrahim** - 23015446
- **Mazen Hussein Mostafa** - 23017827

---

## 🎓 Educational Context

This project was developed as part of an Artificial Intelligence course to demonstrate:

- Search algorithm implementation and comparison
- State space representation
- Heuristic design and evaluation
- Trade-offs between optimality, completeness, and efficiency
- SOLID principles in software design

---

## 📝 License

Educational Project © 2025
