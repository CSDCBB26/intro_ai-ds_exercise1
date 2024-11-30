import unittest

from puzzle.board import Board
from puzzle.utils import generate_multiple_boards


class TestGenerateMultipleBoards(unittest.TestCase):

    def test_generate_multiple_boards_normal(self):
        count = 5
        boards = generate_multiple_boards(count)
        self.assertEqual(len(boards), count)
        for board in boards:
            self.assertIsInstance(board, Board)

    def test_generate_multiple_boards_zero(self):
        count = 0
        boards = generate_multiple_boards(count)
        self.assertEqual(len(boards), 0)

    def test_generate_multiple_boards_negative(self):
        count = -5
        boards = generate_multiple_boards(count)
        self.assertEqual(len(boards), 0)

    def test_generate_multiple_boards_large_number(self):
        count = 1000
        boards = generate_multiple_boards(count)
        self.assertEqual(len(boards), count)
        for board in boards:
            self.assertIsInstance(board, Board)


if __name__ == '__main__':
    unittest.main()
