# Exercise 1 - **8-Puzzle Solver**

This project implements the classic **8-puzzle problem** using **A\*** search algorithm with two heuristic functions: **Hamming Distance** and **Manhattan Distance**. The program generates random initial states, verifies their solvability, and solves the puzzle while comparing the performance of the heuristics.

---

## **Table of Contents**

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [How It Works](#how-it-works)
- [Results](#results)
- [License](#license)
- [Contributors](#contributors)

---

## **Features**

- **Solvability Check**: Determines whether a random puzzle configuration can be solved.
- **Heuristic Implementation**:
  - **Hamming Distance**: Counts misplaced tiles.
  - **Manhattan Distance**: Computes the total tile movement needed to reach the goal.
- **A\* Search**: Finds the optimal solution to the puzzle.
- **Performance Comparison**:
  - Memory usage and runtime are measured for 100 random test cases using both heuristics.
  - Mean and standard deviation are calculated for detailed analysis.
- **Extensive Documentation**:
  - Includes well-commented source code and a report summarizing design decisions and results.

---

## **Project Structure**

```plaintext
intro_ai_ds_exercise1/
├── main.py               # Entry point for running the program
├── puzzle/               # Module containing core puzzle logic
│   ├── __init__.py       # Makes the folder a Python package
│   ├── board.py          # Puzzle representation and operations
│   ├── solver.py         # A* search algorithm implementation
│   ├── heuristics.py     # Heuristic functions (Hamming and Manhattan)
│   └── utils.py          # Utility functions (e.g., solvability checks)
├── tests/                # Unit tests for core modules
│   ├── __init__.py       # Makes the folder a Python package
│   ├── test_board.py     # Tests for board.py
│   ├── test_solver.py    # Tests for solver.py
│   ├── test_heuristics.py# Tests for heuristics.py
│   └── test_utils.py     # Tests for utils.py
├── experiments/          # Performance analysis and experiment scripts
│   ├── [experiment.ipynb](experiment/experiment.ipynb)  # Jupter notebook for experiments with results
├── README.md             # Project overview, setup instructions, and usage
├── requirements.txt      # Python dependencies to install with pip
├── .gitignore            # Git ignore file for excluding unnecessary files
```

---

## **Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/CSDCBB26/intro_ai-ds_exercise1.git
   cd intro_ai-ds_exercise1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
    Check if the installation was successful by running the following command:
    ```bash
    pip list
    ```

---

## **How It Works**

1. **Initialization**:
   - Generates a random solvable puzzle state.
2. **Search**:
   - Solves the puzzle using A\* with selected heuristics.
3. **Performance Logging**:
   - Logs memory usage and runtime for each heuristic.

---

## **Results**

The performance of the heuristics is summarized in terms of:
- **Memory Usage**: Number of expanded nodes.
- **Execution Time**: Time taken to solve the puzzle.

Results are averaged over 100 runs, and the report includes detailed comparisons.

---

## **License**

This project is for educational purposes. Feel free to use and adapt it.

---

## **Contributors**

- [Judy Kardouh](@judyspica)
- [Sergiu-Claudiu Iordanescu](@SergiucCl)
- [Andreas Drozd](@dro42)
