from puzzle.board import Board


def get_neighbors(board):
    """
    Generates valid neighbors by sliding tiles.
    :param board: Instance of Board representing the puzzle state.
    :return: List of new board states after valid moves.
    """
    neighbors = []
    tiles = board.get_tiles()
    zero_pos = next((i, j) for i in range(3) for j in range(3) if tiles[i * 3 + j] == 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for d in directions:
        new_i, new_j = zero_pos[0] + d[0], zero_pos[1] + d[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_tiles = tiles[:]
            new_tiles[zero_pos[0] * 3 + zero_pos[1]], new_tiles[new_i * 3 + new_j] = (
                new_tiles[new_i * 3 + new_j],
                new_tiles[zero_pos[0] * 3 + zero_pos[1]],
            )
            new_board = Board.from_tiles(new_tiles)
            neighbors.append(new_board)
    return neighbors


def reconstruct_path(node):
    """
    Reconstructs the solution path from goal to start.
    :param node: Goal node.
    :return: List of boards from start to goal.
    """
    path = []
    while node:
        path.append(node.board)
        node = node.parent
    return path[::-1]  # Reverse the path to get start-to-goal order
