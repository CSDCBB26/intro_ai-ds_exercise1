# Puzzle Module Documentation

## Overview
The `puzzle` module provides functionality for creating and solving puzzle boards. It includes classes and functions for board manipulation, heuristic calculations, and utility operations.

## Modules

### `board.py`
Contains the `Board` class which represents the puzzle board and provides methods for board manipulation and validation.

#### `Board` Class
- **Attributes**:
  - `board`: A 2D list representing the puzzle board.
  
- **Methods**:
  - `__init__(self, board=None)`: Initializes the board. If no board is provided, it initializes with the default solved board.
  - `is_solvable(board)`: Static method to check if a given board configuration is solvable.
  - `generate_random()`: Static method to generate a random solvable board.
  - `__str__(self)`: Returns the string representation of the board.

### `heuristics.py`
Contains heuristic functions used for solving the puzzle.

#### Functions
- `manhattan_distance(board)`: Calculates the Manhattan distance heuristic for the given board.
- `misplaced_tiles(board)`: Calculates the number of misplaced tiles heuristic for the given board.

### `solver.py`
Contains the `Solver` class which implements algorithms to solve the puzzle.

#### `Solver` Class
- **Attributes**:
  - `initial_board`: The initial state of the puzzle board.
  
- **Methods**:
  - `__init__(self, initial_board)`: Initializes the solver with the initial board.
  - `solve(self)`: Solves the puzzle using a specified algorithm (e.g., A* search).

### `utils.py`
Contains utility functions for the puzzle module.

#### Functions
- `generate_multiple_boards(count)`: Generates multiple random solvable boards.

## Usage Examples

### Creating a Board
```python
from puzzle.board import Board

# Create a default board
board = Board()
print(board)

# Create a custom board
custom_board = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]
board = Board(custom_board)
print(board)
```

### Solving a Puzzle
```python
from puzzle.board import Board
from puzzle.solver import Solver

# Create a board
board = Board()

# Initialize the solver
solver = Solver(board)

# Solve the puzzle
solution = solver.solve()
print(solution)
```

### Generating Multiple Boards
```python
from puzzle.utils import generate_multiple_boards

# Generate 5 random solvable boards
boards = generate_multiple_boards(5)
for board in boards:
    print(board)
```