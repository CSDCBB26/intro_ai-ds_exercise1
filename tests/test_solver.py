import unittest

from puzzle.board import Board
from puzzle.heuristics import hamming_distance, manhattan_distance
from puzzle.solver import Solver


class TestSolver(unittest.TestCase):

    def test_solver_with_manhattan_distance(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Already solved
        solver = Solver(board, manhattan_distance)
        solution, expanded_nodes = solver.solve()

        self.assertEqual(len(solution), 1)
        self.assertEqual(solution[0].get_state(), [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def test_solver_with_hamming_distance(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 0, 8]])  # One move away
        solver = Solver(board, hamming_distance)
        solution, expanded_nodes = solver.solve()

        self.assertEqual(len(solution), 2)

    def test_solver_on_unsolvable_board(self):
        board = Board([[1, 2, 3], [4, 5, 6], [8, 7, 0]])  # Unsolvable
        with self.assertRaises(ValueError):
            solver = Solver(board, manhattan_distance)

    def test_solver_with_random_solvable_board(self):
        board = Board.generate_random()
        solver = Solver(board, manhattan_distance)
        solution, expanded_nodes = solver.solve()

        self.assertIsNotNone(solution)
        self.assertEqual(solution[-1].get_state(), [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def test_solver_solution_length(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 0, 8]])  # One move away
        solver = Solver(board, manhattan_distance)
        solution, expanded_nodes = solver.solve()

        self.assertEqual(len(solution), 2)

    def test_solver_with_empty_board(self):
        with self.assertRaises(ValueError):
            solver = Solver([], manhattan_distance)

    def test_solver_with_null_board(self):
        with self.assertRaises(ValueError):
            solver = Solver(None, manhattan_distance)


if __name__ == '__main__':
    unittest.main()
