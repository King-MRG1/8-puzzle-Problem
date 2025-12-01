import tkinter as tk


class PuzzleSolutionVisualizer:
    """
    Single Responsibility: Handles visualization of puzzle solutions.
    Works with any solver that provides a solution path.
    """
    
    def __init__(self, algorithm_name, algorithm_color, nodes_explored, visited_nodes=None, max_depth=None, parent=None):
        """
        Initialize the visualizer.
        
        Args:
            algorithm_name: Name of the algorithm (e.g., "A* Search", "BFS", "DFS")
            algorithm_color: Color theme for the algorithm (e.g., "#3498db")
            nodes_explored: Number of nodes explored during search
            visited_nodes: Number of unique nodes visited (stored in memory)
            max_depth: Optional max depth limit (for DFS)
            parent: Parent window (if None, creates new window)
        """
        self.algorithm_name = algorithm_name
        self.algorithm_color = algorithm_color
        self.nodes_explored = nodes_explored
        self.visited_nodes = visited_nodes if visited_nodes is not None else nodes_explored
        self.max_depth = max_depth
        self.parent = parent
    
    def visualize(self, solution):
        """
        Visualize the solution using a fullscreen Tkinter window with scrollable canvas.
        
        Args:
            solution: List of PuzzleState objects representing the solution path
        """
        if solution is None:
            print("No solution to visualize.")
            return

        # Create a new top-level window (doesn't block parent)
        if self.parent:
            viz_window = tk.Toplevel(self.parent)
        else:
            viz_window = tk.Tk()
        
        viz_window.title(f"{self.algorithm_name} - 8-Puzzle Solution ({len(solution)-1} moves)")
        viz_window.state('zoomed')  # Fullscreen on Windows
        
        # Dark mode colors
        bg_dark = '#1e1e1e'
        bg_medium = '#2d2d2d'
        bg_light = '#3d3d3d'
        fg_primary = '#ffffff'
        fg_secondary = '#b0b0b0'
        
        viz_window.configure(bg=bg_dark)
        
        # Create main frame
        main_frame = tk.Frame(viz_window, bg=bg_dark)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(main_frame, bg=bg_dark)
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview, 
                                bg=bg_medium, troughcolor=bg_dark, activebackground=bg_light)
        scrollable_frame = tk.Frame(canvas, bg=bg_dark)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        # Update canvas window position to center after frame is configured
        def center_content(event=None):
            canvas.update_idletasks()
            canvas_width = canvas.winfo_width()
            frame_width = scrollable_frame.winfo_reqwidth()
            x_position = max(0, (canvas_width - frame_width) // 2)
            canvas.coords(canvas.find_withtag("content_window")[0], x_position, 0)
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="content_window")
        canvas.bind("<Configure>", center_content)
        viz_window.after(100, center_content)
        
        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Layout parameters
        boards_per_row = 3
        cell_size = 50
        cell_padding = 5
        board_margin_x = 60
        board_margin_y = 80
        
        # Title
        title_label = tk.Label(scrollable_frame, 
                              text=f"{self.algorithm_name} Solution Path",
                              font=('Arial', 18, 'bold'), bg=bg_dark, fg=fg_primary)
        title_label.grid(row=0, column=0, columnspan=boards_per_row, pady=(20, 5))
        
        # Metrics info
        nodes_text = f"Visited Nodes: {self.visited_nodes} | Number of Steps: {len(solution)-1}"
        if self.max_depth:
            nodes_text += f" | Max Depth: {self.max_depth}"
        
        nodes_label = tk.Label(scrollable_frame,
                              text=nodes_text,
                              font=('Arial', 12), bg=bg_dark, fg=fg_secondary)
        nodes_label.grid(row=1, column=0, columnspan=boards_per_row, pady=(0, 15))
        
        # Draw each board in grid layout
        for idx, state in enumerate(solution):
            row_num = (idx // boards_per_row) + 2  # +2 for title and nodes row
            col_num = idx % boards_per_row
            
            # Create frame for this board
            board_frame = tk.Frame(scrollable_frame, bg=bg_dark)
            board_frame.grid(row=row_num, column=col_num, padx=board_margin_x, pady=board_margin_y)
            
            self._draw_board_step(board_frame, state, idx, bg_dark, bg_medium, fg_primary, fg_secondary)
        
        # Close button at bottom
        close_btn = tk.Button(scrollable_frame, text='Close Window', 
                            command=viz_window.destroy, font=('Arial', 12),
                            bg=self.algorithm_color, fg='white', padx=20, pady=10, relief=tk.FLAT)
        close_btn.grid(row=(len(solution)//boards_per_row)+3, column=0, 
                      columnspan=3, pady=30)
        
        # Don't call mainloop if we have a parent (it's already running)
        if not self.parent:
            viz_window.mainloop()
    
    def _draw_board_step(self, parent_frame, state, step_index, bg_dark, bg_medium, fg_primary, fg_secondary):
        """
        Draw a single board step.
        
        Args:
            parent_frame: Parent frame to draw in
            state: PuzzleState object
            step_index: Index of this step in the solution
            bg_dark: Dark background color
            bg_medium: Medium background color
            fg_primary: Primary foreground color
            fg_secondary: Secondary foreground color
        """
        cell_size = 50
        cell_padding = 5
        
        # Step label
        if step_index == 0:
            step_text = "Initial State"
        else:
            step_text = f"Step {step_index}: {state.move}"
        step_label = tk.Label(parent_frame, text=step_text, 
                             font=('Arial', 12, 'bold'), bg=bg_dark, fg=fg_primary)
        step_label.pack(pady=(0, 10))
        
        # Canvas for the puzzle board
        board_canvas = tk.Canvas(parent_frame, 
                                width=3*(cell_size+cell_padding)+10,
                                height=3*(cell_size+cell_padding)+10,
                                bg=bg_dark, highlightthickness=0)
        board_canvas.pack()
        
        # Get lighter version of algorithm color for tiles
        tile_color = self._get_lighter_color(self.algorithm_color)
        
        # Draw the 3x3 puzzle
        for i in range(3):
            for j in range(3):
                x = 5 + j * (cell_size + cell_padding)
                y = 5 + i * (cell_size + cell_padding)
                val = state.board[i][j]
                
                if val == 0:
                    fill = bg_medium
                    outline = '#555'
                    text_color = fg_secondary
                else:
                    fill = tile_color
                    outline = self.algorithm_color
                    text_color = fg_primary
                
                board_canvas.create_rectangle(x, y, x+cell_size, y+cell_size,
                                             fill=fill, outline=outline, width=2)
                if val != 0:
                    board_canvas.create_text(x+cell_size/2, y+cell_size/2,
                                           text=str(val), 
                                           font=('Arial', 20, 'bold'),
                                           fill=text_color)
        
        # Cost/depth information under the board
        self._draw_cost_info(parent_frame, state, bg_dark, fg_secondary)
    
    def _draw_cost_info(self, parent_frame, state, bg_dark, fg_secondary):
        """
        Draw cost/depth information based on algorithm type.
        
        Args:
            parent_frame: Parent frame to draw in
            state: PuzzleState object
            bg_dark: Dark background color
            fg_secondary: Secondary foreground color
        """
        cost_frame = tk.Frame(parent_frame, bg=bg_dark)
        cost_frame.pack(pady=(10, 0))
        
        if self.algorithm_name == "A* Search":
            # A* shows g, h, and f
            g_label = tk.Label(cost_frame, text=f"g = {state.g}", 
                             font=('Arial', 11), bg=bg_dark, fg='#ff6b6b')
            g_label.pack()
            
            h_label = tk.Label(cost_frame, text=f"h = {state.h}", 
                             font=('Arial', 11), bg=bg_dark, fg='#14cc60')
            h_label.pack()
            
            f_label = tk.Label(cost_frame, text=f"f = {state.total_cost}", 
                             font=('Arial', 11, 'bold'), bg=bg_dark, fg=self.algorithm_color)
            f_label.pack()
        elif self.algorithm_name == "Greedy Best-First":
            # GBFS shows f(n) = h only
            f_label = tk.Label(cost_frame, text=f"f(n) = {state.h}", 
                             font=('Arial', 11, 'bold'), bg=bg_dark, fg=self.algorithm_color)
            f_label.pack()
            
            h_label = tk.Label(cost_frame, text=f"h = {state.h}", 
                             font=('Arial', 11), bg=bg_dark, fg='#14cc60')
            h_label.pack()
        else:
            # BFS, DFS, Bidirectional, IDDFS show depth only
            depth_label = tk.Label(cost_frame, text=f"Depth = {state.g}", 
                             font=('Arial', 11, 'bold'), bg=bg_dark, fg=self.algorithm_color)
            depth_label.pack()
    
    def _get_lighter_color(self, hex_color):
        """
        Get a lighter version of the given hex color.
        
        Args:
            hex_color: Hex color string (e.g., "#3498db")
            
        Returns:
            Lighter hex color string
        """
        # Remove '#' and convert to RGB
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Make lighter by moving towards white
        factor = 0.7
        r = int(r + (255 - r) * factor)
        g = int(g + (255 - g) * factor)
        b = int(b + (255 - b) * factor)
        
        return f'#{r:02x}{g:02x}{b:02x}'
