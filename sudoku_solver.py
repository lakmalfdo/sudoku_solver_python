# MIT License
# Copyright (c) Lakmal Fernando

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF,
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import random

class SudokuSolver:
    # Generates a new Sudoku puzzle with a unique solution.
    def generate_sudoku(self):
        # Initialize an empty 9x9 grid
        self.sudoku = [[0 for _ in range(9)] for _ in range(9)]
        
        # Start with a solved puzzle
        self.solve()
        
        # Remove random numbers to create a puzzle
        # Adjust the difficulty by controlling the number of removed elements
        # Adjust the range for the desired difficulty
        for _ in range(random.randint(35, 55)):  
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.sudoku[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.sudoku[row][col] = 0

    # Prints the Sudoku grid in a readable format.
    def print_sudoku(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.sudoku[i][j], end=" ")
            print()

    # Checks if placing number at a given position is valid.
    def is_valid_move(self, row, col, num):
        for i in range(9):
            if self.sudoku[row][i] == num or self.sudoku[i][col] == num:
                return False

        subgrid_row = 3 * (row // 3)
        subgrid_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.sudoku[subgrid_row + i][subgrid_col + j] == num:
                    return False

        return True

    # Recursively solves the Sudoku puzzle using a backtracking algorithm.
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.sudoku[row][col] = num
                            if self.solve():
                                return True
                            self.sudoku[row][col] = 0
                    return False
        return True

if __name__ == "__main__":
    # Create a SudokuSolver instance
    solver = SudokuSolver()

    # Generates a new unsolved Sudoku puzzle
    solver.generate_sudoku()

    print("Unsolved Sudoku:")
    # Show Unsolved Sudoku puzzle
    solver.print_sudoku()

    # Prompt the user to press any key to continue
    input("\nPress any key to solve the Sudoku...")

    # Solved the puzzle
    solver.solve()

    print("\nSolved Sudoku:")
    # Show Solved Sudoku puzzle
    solver.print_sudoku()
