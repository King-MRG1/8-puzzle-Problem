import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from astar_solver import AStarSolver
from bfs_solver import BFSSolver
from dfs_solver import DFSSolver
from puzzle_state import PuzzleState
from design.visualizer import PuzzleSolutionVisualizer


class PuzzleSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver - AI Search Algorithms")
        self.root.geometry("800x800")
        self.root.configure(bg='#1e1e1e')
        
        # Dark mode color scheme
        self.bg_dark = '#1e1e1e'
        self.bg_medium = '#2d2d2d'
        self.bg_light = '#3d3d3d'
        self.fg_primary = '#ffffff'
        self.fg_secondary = '#b0b0b0'
        self.accent_blue = '#0d7377'
        self.accent_green = '#14cc60'
        self.accent_red = '#ff6b6b'
        self.accent_orange = '#ffa500'
        
        # Variables
        self.algorithm_var = tk.StringVar(value="astar")
        self.board_entries = []
        
        # Create main container with padding
        main_container = tk.Frame(root, bg=self.bg_dark, padx=20, pady=20)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_container, 
                              text="8-Puzzle Solver",
                              font=('Arial', 24, 'bold'),
                              bg=self.bg_dark,
                              fg=self.fg_primary)
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(main_container,
                                 text="AI Search Algorithms Comparison",
                                 font=('Arial', 12),
                                 bg=self.bg_dark,
                                 fg=self.fg_secondary)
        subtitle_label.pack(pady=(0, 20))
        
        # Input Section
        input_frame = tk.LabelFrame(main_container,
                                   text=" Enter Puzzle Configuration ",
                                   font=('Arial', 11, 'bold'),
                                   bg=self.bg_medium,
                                   fg=self.fg_primary,
                                   padx=20,
                                   pady=20,
                                   borderwidth=2,
                                   relief=tk.GROOVE)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Instructions
        instruction_label = tk.Label(input_frame,
                                    text="Enter numbers 0-8 (0 represents the blank tile):",
                                    font=('Arial', 10),
                                    bg=self.bg_medium,
                                    fg=self.fg_secondary)
        instruction_label.pack(pady=(0, 15))
        
        # Puzzle grid
        grid_frame = tk.Frame(input_frame, bg=self.bg_medium)
        grid_frame.pack()
        
        # Create 3x3 grid of entry boxes
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(grid_frame,
                               width=5,
                               font=('Arial', 20, 'bold'),
                               justify='center',
                               relief=tk.SOLID,
                               borderwidth=2,
                               bg=self.bg_light,
                               fg=self.fg_primary,
                               insertbackground=self.fg_primary)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.board_entries.append(row_entries)
        
        # Preset buttons
        preset_frame = tk.Frame(input_frame, bg=self.bg_medium)
        preset_frame.pack(pady=(15, 0))
        
        tk.Button(preset_frame,
                 text="Load Easy Puzzle",
                 command=self.load_easy_puzzle,
                 font=('Arial', 10),
                 bg=self.accent_blue,
                 fg='white',
                 padx=10,
                 pady=5,
                 cursor='hand2',
                 relief=tk.FLAT).pack(side=tk.LEFT, padx=5)
        
        tk.Button(preset_frame,
                 text="Load Medium Puzzle",
                 command=self.load_medium_puzzle,
                 font=('Arial', 10),
                 bg=self.accent_orange,
                 fg='white',
                 padx=10,
                 pady=5,
                 cursor='hand2',
                 relief=tk.FLAT).pack(side=tk.LEFT, padx=5)
        
        tk.Button(preset_frame,
                 text="Load Hard Puzzle",
                 command=self.load_hard_puzzle,
                 font=('Arial', 10),
                 bg=self.accent_red,
                 fg='white',
                 padx=10,
                 pady=5,
                 cursor='hand2',
                 relief=tk.FLAT).pack(side=tk.LEFT, padx=5)
        
        tk.Button(preset_frame,
                 text="Clear",
                 command=self.clear_board,
                 font=('Arial', 10),
                 bg='#555555',
                 fg='white',
                 padx=10,
                 pady=5,
                 cursor='hand2',
                 relief=tk.FLAT).pack(side=tk.LEFT, padx=5)
        
        # Algorithm Selection
        algo_frame = tk.LabelFrame(main_container,
                                  text=" Choose Search Algorithm ",
                                  font=('Arial', 11, 'bold'),
                                  bg=self.bg_medium,
                                  fg=self.fg_primary,
                                  padx=25,
                                  pady=25,
                                  borderwidth=2,
                                  relief=tk.GROOVE)
        algo_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Radio buttons for algorithms
        algorithms = [
            ("A* Search (Manhattan Distance Heuristic)", "astar", "#0d7377"),
            ("BFS (Breadth-First Search)", "bfs", "#ff6b6b"),
            ("DFS (Depth-First Search)", "dfs", "#14cc60")
        ]
        
        for text, value, color in algorithms:
            rb = tk.Radiobutton(algo_frame,
                               text=text,
                               variable=self.algorithm_var,
                               value=value,
                               font=('Arial', 13, 'bold'),
                               bg=self.bg_medium,
                               fg=self.fg_primary,
                               selectcolor=self.bg_light,
                               activebackground=self.bg_medium,
                               activeforeground=color,
                               cursor='hand2',
                               padx=15,
                               pady=10,
                               indicatoron=1)
            rb.pack(anchor='w', pady=8)
        
        # Action Buttons
        button_frame = tk.Frame(main_container, bg=self.bg_dark)
        button_frame.pack(pady=(20, 10))
        
        self.solve_button = tk.Button(button_frame,
                                      text="🔍 SOLVE PUZZLE",
                                      command=self.solve_puzzle,
                                      font=('Arial', 14, 'bold'),
                                      bg=self.accent_green,
                                      fg='white',
                                      padx=30,
                                      pady=15,
                                      cursor='hand2',
                                      relief=tk.RAISED,
                                      borderwidth=3)
        self.solve_button.pack(side=tk.LEFT, padx=10)
        
        compare_button = tk.Button(button_frame,
                                  text="📊 COMPARE ALL",
                                  command=self.compare_all,
                                  font=('Arial', 14, 'bold'),
                                  bg=self.accent_blue,
                                  fg='white',
                                  padx=30,
                                  pady=15,
                                  cursor='hand2',
                                  relief=tk.RAISED,
                                  borderwidth=3)
        compare_button.pack(side=tk.LEFT, padx=10)
        
        # Status Label
        self.status_label = tk.Label(main_container,
                                     text="Ready to solve!",
                                     font=('Arial', 10),
                                     bg=self.bg_dark,
                                     fg=self.fg_secondary)
        self.status_label.pack(pady=(10, 0))
        
        # Load default puzzle
        self.load_easy_puzzle()
    
    def load_easy_puzzle(self):
        """Load an easy puzzle configuration."""
        puzzle = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        self.set_board(puzzle)
        self.status_label.config(text="Easy puzzle loaded (2 moves to solve)")
    
    def load_medium_puzzle(self):
        """Load a medium difficulty puzzle."""
        puzzle = [[0, 2, 3], [5, 6, 8], [7, 4, 1]]
        self.set_board(puzzle)
        self.status_label.config(text="Medium puzzle loaded")
    
    def load_hard_puzzle(self):
        """Load a hard puzzle configuration."""
        puzzle = [[8, 6, 7], [2, 5, 4], [3, 0, 1]]
        self.set_board(puzzle)
        self.status_label.config(text="Hard puzzle loaded (requires many moves)")
    
    def clear_board(self):
        """Clear all entries."""
        for i in range(3):
            for j in range(3):
                self.board_entries[i][j].delete(0, tk.END)
        self.status_label.config(text="Board cleared")
    
    def set_board(self, puzzle):
        """Set the board with given puzzle configuration."""
        for i in range(3):
            for j in range(3):
                self.board_entries[i][j].delete(0, tk.END)
                self.board_entries[i][j].insert(0, str(puzzle[i][j]))
    
    def get_board(self):
        """Get the current board configuration from entries."""
        try:
            board = []
            for i in range(3):
                row = []
                for j in range(3):
                    value = self.board_entries[i][j].get().strip()
                    if value == '':
                        messagebox.showerror("Error", "Please fill all cells!")
                        return None
                    num = int(value)
                    if num < 0 or num > 8:
                        messagebox.showerror("Error", "Numbers must be between 0 and 8!")
                        return None
                    row.append(num)
                board.append(row)
            
            # Check if all numbers 0-8 are present
            flat = [num for row in board for num in row]
            if sorted(flat) != list(range(9)):
                messagebox.showerror("Error", "Board must contain each number 0-8 exactly once!")
                return None
            
            return board
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return None
    
    def solve_puzzle(self):
        """Solve the puzzle with selected algorithm."""
        board = self.get_board()
        if board is None:
            return
        
        algorithm = self.algorithm_var.get()
        self.status_label.config(text=f"Solving with {algorithm.upper()}...")
        self.solve_button.config(state='disabled')
        self.root.update()
        
        try:
            # Map algorithm names to colors and max_depth
            algo_config = {
                "astar": {"name": "A* Search", "color": "#3498db", "max_depth": None},
                "bfs": {"name": "BFS", "color": "#e74c3c", "max_depth": None},
                "dfs": {"name": "DFS", "color": "#2ecc71", "max_depth": None}
            }
            
            if algorithm == "astar":
                solver = AStarSolver()
                self.status_label.config(text="Running A* Search...")
            elif algorithm == "bfs":
                solver = BFSSolver()
                self.status_label.config(text="Running BFS...")
            elif algorithm == "dfs":
                solver = DFSSolver()
                self.status_label.config(text="Running DFS...")
                algo_config["dfs"]["max_depth"] = solver.max_depth
            
            solution = solver.solve(board)
            
            if solution:
                moves = len(solution) - 1
                nodes = solver.nodes_explored
                self.status_label.config(
                    text=f"Solution found! {moves} moves, {nodes} nodes explored"
                )
                # Show visualization using shared visualizer
                config = algo_config[algorithm]
                visualizer = PuzzleSolutionVisualizer(
                    algorithm_name=config["name"],
                    algorithm_color=config["color"],
                    nodes_explored=nodes,
                    max_depth=config["max_depth"],
                    parent=self.root  # Pass parent window
                )
                visualizer.visualize(solution)
            else:
                messagebox.showwarning("No Solution", "No solution found for this puzzle!")
                self.status_label.config(text="No solution found")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error occurred")
        
        finally:
            self.solve_button.config(state='normal')
    
    def compare_all(self):
        """Compare all three algorithms."""
        board = self.get_board()
        if board is None:
            return
        
        self.status_label.config(text="Running all algorithms...")
        self.root.update()
        
        results = []
        
        try:
            # A* Search
            self.status_label.config(text="Running A* Search...")
            self.root.update()
            astar_solver = AStarSolver()
            astar_solution = astar_solver.solve(board)
            if astar_solution:
                results.append({
                    'name': 'A* Search',
                    'moves': len(astar_solution) - 1,
                    'nodes': astar_solver.nodes_explored,
                    'solver': astar_solver,
                    'solution': astar_solution
                })
            
            # BFS
            self.status_label.config(text="Running BFS...")
            self.root.update()
            bfs_solver = BFSSolver()
            bfs_solution = bfs_solver.solve(board)
            if bfs_solution:
                results.append({
                    'name': 'BFS',
                    'moves': len(bfs_solution) - 1,
                    'nodes': bfs_solver.nodes_explored,
                    'solver': bfs_solver,
                    'solution': bfs_solution
                })
            
            # DFS
            self.status_label.config(text="Running DFS...")
            self.root.update()
            dfs_solver = DFSSolver()
            dfs_solution = dfs_solver.solve(board)
            if dfs_solution:
                results.append({
                    'name': 'DFS',
                    'moves': len(dfs_solution) - 1,
                    'nodes': dfs_solver.nodes_explored,
                    'solver': dfs_solver,
                    'solution': dfs_solution
                })
            
            if results:
                self.show_comparison_window(results)
                self.status_label.config(text="Comparison complete!")
            else:
                messagebox.showwarning("No Solution", "No algorithm found a solution!")
                self.status_label.config(text="No solutions found")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error occurred")
    
    def show_comparison_window(self, results):
        """Show comparison results in a new window."""
        comp_window = tk.Toplevel(self.root)
        comp_window.title("Algorithm Comparison Results")
        comp_window.geometry("850x550")
        comp_window.configure(bg=self.bg_dark)
        
        # Title
        title = tk.Label(comp_window,
                        text="Algorithm Comparison Results",
                        font=('Arial', 18, 'bold'),
                        bg=self.bg_dark,
                        fg=self.fg_primary)
        title.pack(pady=20)
        
        # Results frame
        results_frame = tk.Frame(comp_window, bg=self.bg_dark)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=40)
        
        # Headers
        headers = ['Algorithm', 'Moves', 'Nodes Explored', 'Efficiency']
        colors = ['#0d7377', '#ff6b6b', '#14cc60']
        
        # Define fixed column widths
        col_widths = [150, 100, 150, 100]  # pixels for each column
        
        for col, header in enumerate(headers):
            label = tk.Label(results_frame,
                           text=header,
                           font=('Arial', 12, 'bold'),
                           bg=self.bg_light,
                           fg=self.fg_primary,
                           width=col_widths[col]//7,  # Convert pixels to characters approximately
                           padx=15,
                           pady=10,
                           relief=tk.FLAT,
                           borderwidth=0,
                           anchor='center')
            label.grid(row=0, column=col, sticky='ew', padx=2, pady=2)
        
        # Results data
        for idx, result in enumerate(results):
            # Algorithm name
            name_label = tk.Label(results_frame,
                                 text=result['name'],
                                 font=('Arial', 11, 'bold'),
                                 bg=self.bg_medium,
                                 fg=colors[idx],
                                 width=col_widths[0]//7,
                                 padx=15,
                                 pady=15,
                                 anchor='w')
            name_label.grid(row=idx+1, column=0, sticky='ew', padx=2, pady=2)
            
            # Moves
            moves_label = tk.Label(results_frame,
                                  text=str(result['moves']),
                                  font=('Arial', 11),
                                  bg=self.bg_medium,
                                  fg=self.fg_primary,
                                  width=col_widths[1]//7,
                                  padx=15,
                                  pady=15,
                                  anchor='center')
            moves_label.grid(row=idx+1, column=1, sticky='ew', padx=2, pady=2)
            
            # Nodes explored
            nodes_label = tk.Label(results_frame,
                                  text=str(result['nodes']),
                                  font=('Arial', 11),
                                  bg=self.bg_medium,
                                  fg=self.fg_primary,
                                  width=col_widths[2]//7,
                                  padx=15,
                                  pady=15,
                                  anchor='center')
            nodes_label.grid(row=idx+1, column=2, sticky='ew', padx=2, pady=2)
            
            # Efficiency (nodes per move)
            efficiency = result['nodes'] / max(result['moves'], 1)
            eff_label = tk.Label(results_frame,
                                text=f"{efficiency:.2f}",
                                font=('Arial', 11),
                                bg=self.bg_medium,
                                fg=self.fg_primary,
                                width=col_widths[3]//7,
                                padx=15,
                                pady=15,
                                anchor='center')
            eff_label.grid(row=idx+1, column=3, sticky='ew', padx=2, pady=2)
        
        # Configure grid weights
        for col in range(4):
            results_frame.grid_columnconfigure(col, weight=1)
        
        # Visualization buttons
        viz_frame = tk.Frame(comp_window, bg=self.bg_dark)
        viz_frame.pack(pady=20)
        
        tk.Label(viz_frame,
                text="View Visualization:",
                font=('Arial', 11, 'bold'),
                bg=self.bg_dark,
                fg=self.fg_primary).pack(pady=(0, 10))
        
        button_container = tk.Frame(viz_frame, bg=self.bg_dark)
        button_container.pack()
        
        # Create visualization function with proper parameters
        def show_visualization(result, color):
            max_depth = result['solver'].max_depth if hasattr(result['solver'], 'max_depth') else None
            visualizer = PuzzleSolutionVisualizer(
                algorithm_name=result['name'],
                algorithm_color=color,
                nodes_explored=result['nodes'],
                max_depth=max_depth,
                parent=self.root  # Pass parent window
            )
            visualizer.visualize(result['solution'])
        
        for idx, result in enumerate(results):
            btn = tk.Button(button_container,
                          text=result['name'],
                          command=lambda r=result, c=colors[idx]: show_visualization(r, c),
                          font=('Arial', 10, 'bold'),
                          bg=colors[idx],
                          fg='white',
                          padx=20,
                          pady=10,
                          cursor='hand2',
                          relief=tk.FLAT)
            btn.pack(side=tk.LEFT, padx=10)
        
        # Close button
        close_btn = tk.Button(comp_window,
                             text="Close",
                             command=comp_window.destroy,
                             font=('Arial', 11),
                             bg='#555555',
                             fg='white',
                             padx=30,
                             pady=10,
                             cursor='hand2',
                             relief=tk.FLAT)
        close_btn.pack(pady=10)


def main():
    root = tk.Tk()
    app = PuzzleSolverGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
