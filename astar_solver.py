import heapq
from puzzle_state import PuzzleState


class AStarSolver:
    def __init__(self):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.nodes_explored = 0
    
    def calculate_manhattan_distance(self, board):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = board[i][j]
                if value != 0:
                    goal_row = (value - 1) // 3
                    goal_col = (value - 1) % 3
                    distance += abs(i - goal_row) + abs(j - goal_col)
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
                new_state = PuzzleState(board=new_board, g=state.g + 1, h=self.calculate_manhattan_distance(new_board), parent=state, move=move_name)
                neighbors.append(new_state)
        return neighbors
    
    def solve(self, initial_board):
        initial_state = PuzzleState(board=initial_board, g=0, h=self.calculate_manhattan_distance(initial_board))
        goal = PuzzleState(board=self.goal_state)
        open_set = []
        heapq.heappush(open_set, initial_state)
        closed_set = set()
        nodes_explored = 0
        
        while open_set:
            current = heapq.heappop(open_set)
            nodes_explored += 1
            
            if current == goal:
                print(f"A* Solution found! Nodes explored: {nodes_explored}")
                self.nodes_explored = nodes_explored
                return self.build_solution_path(current)
            
            closed_set.add(hash(current))
            
            for neighbor in self.get_possible_moves(current):
                if hash(neighbor) not in closed_set:
                    heapq.heappush(open_set, neighbor)
        
        print(f"A*: No solution found after exploring {nodes_explored} nodes.")
        self.nodes_explored = nodes_explored
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
        
        print(f"\nA* Solution found in {len(solution) - 1} moves:\n")
        for i, state in enumerate(solution):
            if state.move:
                print(f"Move {i}: {state.move}")
            else:
                print(f"Initial State:")
            state.display_board()
            print()
