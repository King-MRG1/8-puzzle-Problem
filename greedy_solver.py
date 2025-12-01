import heapq
from puzzle_state import PuzzleState


class GreedySolver:
    def __init__(self):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.nodes_explored = 0
        self.visited_nodes = 0
    
    def calculate_manhattan_distance(self, board):
        distance = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    target_value = board[i][j]
                    target_row = (target_value - 1) // 3
                    target_col = (target_value - 1) % 3
                    distance += abs(i - target_row) + abs(j - target_col)
        return distance
    
    def get_possible_moves(self, state):
        neighbors = []
        blank_row, blank_col = state.find_blank_position()
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
        
        for dr, dc, move_name in moves:
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = [row[:] for row in state.board]
                new_board[blank_row][blank_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_row][blank_col]
                h = self.calculate_manhattan_distance(new_board)
                new_state = PuzzleState(board=new_board, g=state.g + 1, h=h, parent=state, move=move_name)
                neighbors.append(new_state)
        return neighbors
    
    def solve(self, initial_board):
        h_initial = self.calculate_manhattan_distance(initial_board)
        initial_state = PuzzleState(board=initial_board, g=0, h=h_initial)
        goal = PuzzleState(board=self.goal_state)
        
        # Priority queue: (h, counter, state) - only h (greedy)
        open_list = []
        counter = 0
        heapq.heappush(open_list, (initial_state.h, counter, initial_state))
        counter += 1
        
        visited = set()
        visited.add(hash(initial_state))
        self.nodes_explored = 0
        self.visited_nodes = 0
        
        while open_list:
            _, _, current = heapq.heappop(open_list)
            self.nodes_explored += 1
            
            if current == goal:
                self.visited_nodes = len(visited)
                print(f"Greedy Solution found! Nodes explored: {self.nodes_explored}, Visited: {self.visited_nodes}")
                return self.build_solution_path(current)
            
            for neighbor in self.get_possible_moves(current):
                neighbor_hash = hash(neighbor)
                if neighbor_hash not in visited:
                    visited.add(neighbor_hash)
                    heapq.heappush(open_list, (neighbor.h, counter, neighbor))
                    counter += 1
        
        self.visited_nodes = len(visited)
        print(f"Greedy: No solution found after exploring {self.nodes_explored} nodes.")
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
        
        print(f"\nGreedy Solution found in {len(solution) - 1} moves:\n")
        for i, state in enumerate(solution):
            if state.move:
                print(f"Move {i}: {state.move}")
            else:
                print(f"Initial State:")
            state.display_board()
            print()
