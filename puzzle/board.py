import random

class Board:
    def __init__(self, board=None):
        """
        Initializes the board. If no board is provided, creates a default goal state.
        :param board: 2D list representing the puzzle state (optional).
        """
        if board:
            self.board = board
        else:
            self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Default goal state

    @staticmethod
    def is_solvable(numbers):
        """
        Determines if a given puzzle configuration is solvable based on inversion count.
        :param numbers: Flattened list of puzzle tiles.
        :return: True if the puzzle is solvable, False otherwise.
        """
        inv_count = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[j] and numbers[i] and numbers[i] > numbers[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    @classmethod
    def generate_random(cls):
        """
        Generates a random solvable board.
        :return: An instance of the Board class with a solvable random configuration.
        """
        while True:
            numbers = list(range(9))  # Numbers 0 through 8
            random.shuffle(numbers)
            if cls.is_solvable(numbers):
                # Convert to a 2D board representation
                board = [numbers[i * 3:(i + 1) * 3] for i in range(3)]
                return cls(board)


def get_dimensions(self):
    """
    Returns the dimensions of the board.

    :return: A tuple (rows, columns) representing the dimensions of the board.
    """
    return len(self.board), len(self.board[0])

def get_tiles(self):
    """
    Returns a flattened list of all tiles in the board.

    :return: A list of integers representing the tiles in the board.
    """
    return [tile for row in self.board for tile in row]

def __str__(self):
        """
        Returns a string representation of the board.
        """
        return '\n'.join(' '.join(map(str, row)) for row in self.board)
