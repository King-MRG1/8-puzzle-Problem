"""
8-Puzzle Solver - Main Entry Point
Follows Single Responsibility Principle: Only handles program startup
"""

from design.gui_interface import PuzzleSolverGUI
import tkinter as tk


def main():
    """Main entry point for the 8-Puzzle solver application."""
    root = tk.Tk()
    app = PuzzleSolverGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
