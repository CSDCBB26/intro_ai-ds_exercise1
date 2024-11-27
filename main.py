from puzzle.utils import generate_multiple_boards
from puzzle.board import Board

def main():
    # Generate 100 random solvable boards
    boards = generate_multiple_boards(100)

    # Display each board and solvability status in the console
    for i, board in enumerate(boards):
        flattened_board = sum(board.board, [])  # Flatten the board for solvability check
        solvable = Board.is_solvable(flattened_board)
        print(f"Board {i + 1}:\n{board}\nSolvable: {'Yes' if solvable else 'No'}\n")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
