import unittest

from puzzle.board import Board
from puzzle.utils import reconstruct_path, get_neighbors


class TestUtils(unittest.TestCase):

    def test_get_neighbors(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 0, 8]])  # One move away
        neighbors = get_neighbors(board)
        self.assertEqual(len(neighbors), 3)
        expected_states = [
            [[1, 2, 3], [4, 0, 6], [7, 5, 8]],  # Move 0 up
            [[1, 2, 3], [4, 5, 6], [0, 7, 8]],  # Move 0 left
            [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Move 0 right
        ]
        actual_states = [neighbor.get_state() for neighbor in neighbors]
        self.assertTrue(all(state in expected_states for state in actual_states))

    def test_reconstruct_path(self):
        class Node:
            def __init__(self, board, parent=None):
                self.board = board
                self.parent = parent

        start_board = Board([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        goal_board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        node1 = Node(start_board)
        node2 = Node(Board([[1, 2, 3], [4, 5, 6], [7, 0, 8]]), node1)
        node3 = Node(goal_board, node2)

        path = reconstruct_path(node3)
        expected_path = [start_board, Board([[1, 2, 3], [4, 5, 6], [7, 0, 8]]), goal_board]
        actual_path = [board.get_state() for board in path]
        expected_path_states = [board.get_state() for board in expected_path]

        self.assertEqual(actual_path, expected_path_states)


if __name__ == '__main__':
    unittest.main()
