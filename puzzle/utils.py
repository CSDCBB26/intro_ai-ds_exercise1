from puzzle.board import Board

def generate_multiple_boards(count):
    """
    Generates multiple random solvable boards.
    :param count: Number of boards to generate.
    :return: List of Board instances.
    """
    boards = []
    for _ in range(count):
        boards.append(Board.generate_random())
    return boards
