import statistics
import time

from puzzle.board import Board
from puzzle.heuristics import hamming_distance, manhattan_distance
from puzzle.solver import Solver


def main():
    """
    Starts the Jupyter Notebook server and opens the specified notebook file.
    """
    # subprocess.run(["jupyter", "notebook", "experiment/puzzle8_experiment.ipynb"])

    """
    Generates 100 random solvable boards, evaluates each heuristic for solving them,
    and calculates the memory effort and runtime metrics.
    """
    # Generate 100 random boards
    boards = [Board.generate_random() for _ in range(100)]

    # Heuristics
    heuristics = {
        "Hamming": hamming_distance,
        "Manhattan": manhattan_distance
    }

    # Store results for analysis
    results = {heuristic_name: {"memory_usage": [], "execution_time": []} for heuristic_name in heuristics}

    for index, board in enumerate(boards):
        print("---" * 20)
        print(f"Board {index + 1}:")
        print(board)

        for heuristic_name, heuristic_func in heuristics.items():
            print(f"Evaluating with {heuristic_name} heuristic...")

            # Measure memory and runtime for the current heuristic
            start_time = time.time()
            solver = Solver(board, heuristic_func)
            solution, memory_effort = solver.solve()
            end_time = time.time()

            runtime = end_time - start_time

            # Store results
            results[heuristic_name]["memory_usage"].append(memory_effort)
            results[heuristic_name]["execution_time"].append(runtime)

            print(f"Memory Effort: {memory_effort} nodes")
            print(f"Runtime: {runtime:.6f} seconds")

    # Calculate mean and standard deviation for each heuristic
    for heuristic_name in heuristics:
        memory_usages = results[heuristic_name]["memory_usage"]
        execution_times = results[heuristic_name]["execution_time"]

        memory_mean = statistics.mean(memory_usages)
        memory_std_dev = statistics.stdev(memory_usages)
        runtime_mean = statistics.mean(execution_times)
        runtime_std_dev = statistics.stdev(execution_times)

        print(f"\n{heuristic_name} Heuristic Statistics:")
        print(f"Mean Memory Usage: {memory_mean:.2f} nodes")
        print(f"Standard Deviation of Memory Usage: {memory_std_dev:.2f} nodes")
        print(f"Mean Runtime: {runtime_mean:.6f} seconds")
        print(f"Standard Deviation of Runtime: {runtime_std_dev:.6f} seconds")
        print("\n")

        input("Press Enter to exit console...")


if __name__ == "__main__":
    main()
