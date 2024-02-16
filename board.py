import tkinter as tk
import solver

def CreateInputGrid(root):
    entries = []
    board = tk.Frame(root, highlightbackground="black", highlightthickness=2)
    board.pack()
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(board, highlightbackground="black", highlightthickness=2)
            frame.grid(row=i, column=j)
            
            for k in range(3):
                for l in range(3):
                    entry = tk.Entry(frame, width=5)
                    entry.grid(row=k, column=l)
                    entries.append(entry)
    return entries

def GetInputs(entries):
    inputs = []
    for entry in entries:
        value = entry.get()
        if not value:
            inputs.append(0)
        else:
            inputs.append(int(value))

    sudokuGrid = []
    i = 0
    while i < 81:
        sudokuGrid.append(inputs[i:i+3] + inputs[i+9:i+9+3] + inputs[i+18:i+18+3])
        i += 3
        if i % 9 == 0:
            i += 18
    
    return sudokuGrid

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku Sat Solver")

    title = tk.Label(root, text="Sudoku Sat Solver", font='TkDefaultFont 18 bold')
    lable1 = tk.Label(root, text="Enter a puzzle: ")
    title.pack()
    lable1.pack()

    entries = CreateInputGrid(root)

    def Solve():
        sudokuGrid = GetInputs(entries)
        solver.SudokuSolver(sudokuGrid)

    solveButton = tk.Button(root, text="Solve", bg="yellow", command=Solve)
    solveButton.pack()

    root.mainloop()
