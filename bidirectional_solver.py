from collections import deque
from puzzle_state import PuzzleState


class BidirectionalSolver:
    def __init__(self):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.nodes_explored = 0
        self.visited_nodes = 0
    
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
        
        # Forward search from initial state
        forward_queue = deque([initial_state])
        forward_visited = {hash(initial_state): initial_state}
        
        # Backward search from goal state
        backward_queue = deque([goal])
        backward_visited = {hash(goal): goal}
        
        self.nodes_explored = 0
        self.visited_nodes = 0
        
        while forward_queue and backward_queue:
            # Expand forward
            if forward_queue:
                current_forward = forward_queue.popleft()
                self.nodes_explored += 1
                
                # Check if this state was visited from backward
                current_hash = hash(current_forward)
                if current_hash in backward_visited:
                    # Found intersection - reconstruct path
                    backward_state = backward_visited[current_hash]
                    solution = self._reconstruct_bidirectional_path(current_forward, backward_state)
                    self.visited_nodes = len(forward_visited) + len(backward_visited)
                    print(f"Bidirectional Solution found! Nodes explored: {self.nodes_explored}, Visited: {self.visited_nodes}")
                    return solution
                
                for neighbor in self.get_possible_moves(current_forward):
                    neighbor_hash = hash(neighbor)
                    if neighbor_hash not in forward_visited:
                        forward_visited[neighbor_hash] = neighbor
                        forward_queue.append(neighbor)
            
            # Expand backward
            if backward_queue:
                current_backward = backward_queue.popleft()
                self.nodes_explored += 1
                
                # Check if this state was visited from forward
                current_hash = hash(current_backward)
                if current_hash in forward_visited:
                    # Found intersection - reconstruct path
                    forward_state = forward_visited[current_hash]
                    solution = self._reconstruct_bidirectional_path(forward_state, current_backward)
                    self.visited_nodes = len(forward_visited) + len(backward_visited)
                    print(f"Bidirectional Solution found! Nodes explored: {self.nodes_explored}, Visited: {self.visited_nodes}")
                    return solution
                
                for neighbor in self.get_possible_moves(current_backward):
                    neighbor_hash = hash(neighbor)
                    if neighbor_hash not in backward_visited:
                        backward_visited[neighbor_hash] = neighbor
                        backward_queue.append(neighbor)
        
        self.visited_nodes = len(forward_visited) + len(backward_visited)
        print(f"Bidirectional: No solution found after exploring {self.nodes_explored} nodes.")
        return None
    
    def _reconstruct_bidirectional_path(self, forward_state, backward_state):
        """Reconstruct path from forward and backward meeting point."""
        # Build forward path
        forward_path = []
        current = forward_state
        while current is not None:
            forward_path.append(current)
            current = current.parent
        forward_path.reverse()
        
        # Build backward path (skip first as it's duplicate)
        backward_path = []
        current = backward_state.parent
        while current is not None:
            backward_path.append(current)
            current = current.parent
        
        return forward_path + backward_path
    
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
        
        print(f"\nBidirectional Solution found in {len(solution) - 1} moves:\n")
        for i, state in enumerate(solution):
            if state.move:
                print(f"Move {i}: {state.move}")
            else:
                print(f"Initial State:")
            state.display_board()
            print()
