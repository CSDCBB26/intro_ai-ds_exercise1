# Exercise 1 - **8-Puzzle Solver**

This project implements the classic **8-puzzle problem** using **A\*** search algorithm with two heuristic functions: **Hamming Distance** and **Manhattan Distance**. The program generates random initial states, verifies their solvability, and solves the puzzle while comparing the performance of the heuristics.

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
8-puzzle/
├── main.py               # Entry point for running the program
├── puzzle/
│   ├── board.py          # Puzzle representation and operations
│   ├── solver.py         # A* search implementation
│   ├── heuristics.py     # Heuristic functions
│   └── utils.py          # Helper functions
├── tests/                # Unit tests for components
├── experiments/          # Scripts and results for performance analysis
├── README.md             # Project overview (this file)
├── requirements.txt      # Python dependencies
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

3. Run the program:
   ```bash
   python main.py
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