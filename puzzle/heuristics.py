def hamming_distance(board):
    """
    The Hamming distance heuristic counts the number of tiles that are not in their goal position.
    It is calculated by comparing each tile in the current board configuration with the corresponding tile in the goal configuration.
    If a tile is not in its correct position, the distance is incremented by one.

    :param board: 2D list representing the puzzle state.
    :return: Hamming distance.
    """
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                distance += 1
    return distance

def manhattan_distance(board):
    """
    The Manhattan distance heuristic calculates the sum of the absolute differences between the current and goal positions of each tile.
    It measures the total number of moves required to get each tile from its current position to its goal position,
    assuming that tiles can only move horizontally or vertically.

    :param board: 2D list representing the puzzle state.
    :return: Manhattan distance.
    """
    goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 0: (2, 2)}
    distance = 0
    tiles = board.get_tiles()
    for i in range(3):
        for j in range(3):
            tile = tiles[i * 3 + j]
            if tile != 0:
                goal_i, goal_j = goal_positions[tile]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance