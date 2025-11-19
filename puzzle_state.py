class PuzzleState:
    
    def __init__(self, board, g=0, h=0, parent=None, move=""):
        self.board = [row[:] for row in board]  # Deep copy of the board
        self.g = g  # Cost to reach this state
        self.h = h  # Heuristic cost to reach goal
        self.parent = parent  # Parent state
        self.move = move  # Move taken to reach this state
    
    @property
    def total_cost(self):
        return self.g + self.h
    
    def find_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (-1, -1)
    
    def __hash__(self):
        hash_value = 0
        for i in range(3):
            for j in range(3):
                hash_value = hash_value * 10 + self.board[i][j]
        return hash_value
    
    def __eq__(self, other):
        if other is None or not isinstance(other, PuzzleState):
            return False
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def display_board(self):
        """Print the puzzle board in a formatted way."""
        print("-------------")
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                if self.board[i][j] == 0:
                    print("  | ", end="")
                else:
                    print(f"{self.board[i][j]} | ", end="")
            print()
            print("-------------")
