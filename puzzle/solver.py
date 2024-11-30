from heapq import heappop, heappush

class AStarSearch:
    def __init__(self, graph: dict, heuristic_values: dict):
        """
        Initialize the A* Search class.

        @param graph: The graph to search as a dictionary of adjacency lists.
                      Each key is a node, and the value is a list of tuples (neighbor, edge_cost).
        @param heuristic_values: Admissible heuristic values for each node.
        """
        self.graph = graph  # Graph representation as adjacency lists.
        self.heuristic_values = heuristic_values  # Admissible heuristic values for nodes.

    def search(self, start: str, goal: str):
        """
        Perform A* search from the start node to the goal node.

        @param start: The starting node.
        @param goal: The goal node.
        @return: A tuple containing the total cost and the path from start to goal.
        """
        # Priority queue (open list) initialized with the start node.
        # Each entry is a tuple: (f_score, g_score, node)
        # f_score = g_score + heuristic value
        open_list = [(self.heuristic_values[start], 0, start)]

        # Dictionary to store the minimum cost to reach each node from the start.
        g_scores = {start: 0}

        # Dictionary to track the parent of each node for path reconstruction.
        came_from = {}

        # Main loop: Process nodes until the open list is empty or the goal is reached.
        while open_list:
            # Step 1: Remove the node with the smallest f_score from the priority queue.
            f_score, g_score, current = heappop(open_list)

            # Step 2: If the goal node is reached, reconstruct and return the path.
            if current == goal:
                return self._reconstruct_path(came_from, current, g_score)

            # Step 3: Explore all neighbors of the current node.
            for neighbor, edge_cost in self.graph.get(current, []):
                # Calculate the tentative g_score for the neighbor.
                # g_score represents the path cost from the start node to this neighbor.
                tentative_g_score = g_score + edge_cost

                # Step 4: Check if this path to the neighbor is better than any known path.
                if tentative_g_score < g_scores.get(neighbor, float('inf')):
                    # Update the g_score for this neighbor.
                    g_scores[neighbor] = tentative_g_score

                    # Calculate the total cost (f_score) for this neighbor.
                    # f_score = g_score + heuristic value
                    f_score = tentative_g_score + self.heuristic_values[neighbor]

                    # Add the neighbor to the open list for further exploration.
                    heappush(open_list, (f_score, tentative_g_score, neighbor))

                    # Update the 'came_from' dictionary to track the parent node.
                    # This is used later to reconstruct the path.
                    came_from[neighbor] = current

        # Step 5: If the open list is empty and the goal was not reached, return failure.
        return -1, []  # No path found.

    def _reconstruct_path(self, came_from: dict, current: str, g_score: int):
        """
        Reconstruct the path from the start node to the goal node.

        @param came_from: Dictionary tracking the parent of each node.
        @param current: The current (goal) node.
        @param g_score: The total cost to reach the goal node.
        @return: A tuple containing the total cost and the reconstructed path.
        """
        # Initialize the path list and backtrack from the goal to the start.
        path = []
        while current:
            path.append(current)  # Add the current node to the path.
            current = came_from.get(current)  # Move to the parent node.

        # Reverse the path to get the order from start to goal.
        path.reverse()
        return g_score, path


"""
EXAMPLE_GRAPH = {
    'S': [('A', 4), ('B', 10), ('C', 11)],
    'A': [('B', 8), ('D', 5)],
    'B': [('D', 15)],
    'C': [('D', 8), ('E', 20), ('F', 2)],
    'D': [('F', 1), ('I', 20), ('H', 16)],
    'E': [('G', 19)],
    'F': [('G', 13)],
    'H': [('J', 2), ('I', 1)],
    'I': [('K', 13), ('G', 5), ('J', 5)],
    'J': [('K', 7)],
    'K': [('G', 16)]
}

EXAMPLE_HEURISTIC_VALUES = {
    'S': 7,
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 5,
    'E': 3,
    'F': 3,
    'G': 0,  # Goal node has a heuristic value of 0.
    'H': 7,
    'I': 4,
    'J': 5,
    'K': 3
}

# Instantiate the AStarSearch class.
astar = AStarSearch(EXAMPLE_GRAPH, EXAMPLE_HEURISTIC_VALUES)

# Perform the search.
result_cost, result_path = astar.search('S', 'G')
print(f"Cost: {result_cost}, Path: {result_path}")

"""