from puzzle_state import PuzzleState


class IDDFSSolver:
    def __init__(self):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.nodes_explored = 0
        self.visited_nodes = 0
        self.max_depth = 50
    
    def get_possible_moves(self, state):
        neighbors = []
        blank_row, blank_col = state.find_blank_position()
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
        
        for dr, dc, move_name in moves:
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = [row[:] for row in state.board]
                new_board[blank_row][blank_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_row][blank_col]
                new_state = PuzzleState(board=new_board, g=state.g + 1, h=0, parent=state, move=move_name)
                neighbors.append(new_state)
        return neighbors
    
    def solve(self, initial_board):
        initial_state = PuzzleState(board=initial_board, g=0, h=0)
        goal = PuzzleState(board=self.goal_state)
        
        self.nodes_explored = 0
        self.visited_nodes = 0
        
        # Iteratively increase depth limit
        for depth in range(self.max_depth):
            visited_at_depth = set()
            result = self._depth_limited_search(initial_state, goal, depth, visited_at_depth)
            self.visited_nodes += len(visited_at_depth)
            
            if result is not None:
                print(f"IDDFS Solution found at depth {depth}! Nodes explored: {self.nodes_explored}, Visited: {self.visited_nodes}")
                return result
        
        print(f"IDDFS: No solution found within depth limit {self.max_depth}. Nodes explored: {self.nodes_explored}")
        return None
    
    def _depth_limited_search(self, current, goal, depth_limit, visited):
        """Perform depth-limited DFS."""
        self.nodes_explored += 1
        visited.add(hash(current))
        
        if current == goal:
            return self.build_solution_path(current)
        
        if depth_limit == 0:
            return None
        
        for neighbor in self.get_possible_moves(current):
            neighbor_hash = hash(neighbor)
            if neighbor_hash not in visited:
                result = self._depth_limited_search(neighbor, goal, depth_limit - 1, visited)
                if result is not None:
                    return result
        
        return None
    
    def build_solution_path(self, state):
        path = []
        current = state
        while current is not None:
            path.append(current)
            current = current.parent
        return path[::-1]
    
    def display_solution(self, solution):
        if solution is None:
            print("No solution to print.")
            return
        
        print(f"\nIDDFS Solution found in {len(solution) - 1} moves:\n")
        for i, state in enumerate(solution):
            if state.move:
                print(f"Move {i}: {state.move}")
            else:
                print(f"Initial State:")
            state.display_board()
            print()
