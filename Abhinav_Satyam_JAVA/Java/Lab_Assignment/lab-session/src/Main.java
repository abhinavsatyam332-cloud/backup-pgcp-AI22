//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.*;

public class Main {
    // Function to print the chessboard configuration
    private static void printBoard(int[][] board, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    System.out.print(" Q "); // Q represents a Queen
                } else {
                    System.out.print(" . "); // . represents an empty space
                }
            }
            System.out.println();
        }
        System.out.println();
    }

    // Check if it's safe to place a queen at board[row][col]
    private static boolean isSafe(int[][] board, int row, int col, int n) {
        int i, j;

        // 1. Check this row on the left side
        for (i = 0; i < col; i++) {
            if (board[row][i] == 1) {
                return false;
            }
        }

        // 2. Check upper-left diagonal
        for (i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        // 3. Check lower-left diagonal
        for (i = row, j = col; j >= 0 && i < n; i++, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        return true; // Safe to place
    }

    // Core recursive backtracking function to solve N-Queens
    private static boolean solveNQueensUtil(int[][] board, int col, int n) {
        // Base Case: If all queens are placed successfully
        if (col >= n) {
            return true;
        }

        // Consider this column and try placing a queen in all rows one by one
        for (int i = 0; i < n; i++) {
            // Check if the queen can be placed safely
            if (isSafe(board, i, col, n)) {
                // Place the queen
                board[i][col] = 1;

                // Recur to place the rest of the queens
                if (solveNQueensUtil(board, col + 1, n)) {
                    return true;
                }

                // If placing queen here doesn't lead to a solution, backtrack
                board[i][col] = 0;
            }
        }

        // If the queen cannot be placed in any row of this column, return false
        return false;
    }

    // Wrapper function to set up and trigger the solver
    public static void solveNQueens(int n) {
        int[][] board = new int[n][n]; // Initialized to 0 by default

        if (!solveNQueensUtil(board, 0, n)) {
            System.out.println("Solution does not exist for a board of size " + n);
            return;
        }

        System.out.println("A valid solution for " + n + "-Queens:");
        printBoard(board, n);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // FIXED HERE
        System.out.print("Enter the value of N (Chessboard size): ");
        int n = scanner.nextInt();

        if (n <= 0) {
            System.out.println("Please enter a valid board size greater than 0.");
        } else {
            solveNQueens(n);
        }
        scanner.close();
    }
}