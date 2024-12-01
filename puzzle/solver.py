import heapq
from puzzle.board import Board
from puzzle.utils import reconstruct_path, get_neighbors


class Solver:
    def __init__(self, board, heuristic):
        """
        Initializes the Solver with a board and heuristic function.
        :param board: Instance of Board representing the puzzle state.
        :param heuristic: Heuristic function to evaluate board states.
        """
        if not board or board.get_dimensions() != (3, 3):
            raise ValueError("Invalid board format. Board must be a 3x3 grid!")
        if not Board.is_solvable(board.get_tiles()):
            raise ValueError("The board is not solvable!")
        self.board = board  # Initial puzzle state
        self.heuristic = heuristic  # Heuristic function (e.g., hamming_distance or manhattan_distance)
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal configuration
        self.expanded_nodes = 0

    class Node:
        def __init__(self, board, parent=None, g=0, h=0):
            """
            Represents a node in the A* search tree.
            :param board: Current puzzle state (2D list).
            :param parent: Parent Node instance (used to reconstruct solution path).
            :param g: Cost from start to current node (path cost).
            :param h: Estimated cost to the goal (heuristic cost).
            """
            self.board = board
            self.parent = parent
            self.g = g
            self.h = h
            self.f = g + h

        def __lt__(self, other):
            """
            Comparison operator for priority queue based on f-value.
            """
            return self.f < other.f

    def is_goal(self, board):
        """
        Checks if the board is in the goal state.
        :param board: Current board state (2D list).
        :return: True if board matches goal state, otherwise False.
        """
        return board == self.goal_state

    def solve(self):
        """
        Executes the A* search algorithm to solve the puzzle.
        :return: Solution path and number of expanded nodes.
        """
        start_node = self.Node(self.board, h=self.heuristic(self.board))
        open_list = []
        heapq.heappush(open_list, start_node)
        closed_set = set()

        while open_list:
            current_node = heapq.heappop(open_list)
            self.expanded_nodes += 1

            if self.is_goal(current_node.board.get_state()):
                return reconstruct_path(current_node), self.expanded_nodes

            closed_set.add(tuple(map(tuple, current_node.board.get_state())))

            for neighbor in get_neighbors(current_node.board):
                if tuple(map(tuple, neighbor.get_state())) in closed_set:
                    continue

                g = current_node.g + 1
                h = self.heuristic(neighbor)
                neighbor_node = self.Node(neighbor, current_node, g, h)

                heapq.heappush(open_list, neighbor_node)

        return None, self.expanded_nodes  # If no solution is found
