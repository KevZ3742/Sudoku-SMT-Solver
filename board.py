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

def CreateOutputGrid(root, entries, solution):
    board = tk.Frame(root, highlightbackground="black", highlightthickness=2)
    board.pack()

    inputs = []
    for entry in entries:
        value = entry.get()
        if not value:
            inputs.append(0)
        else:
            inputs.append(int(value))

    outputGrid = []
    for i in range(0, len(inputs), 9):
        outputGrid.append(inputs[i:i+9])
        
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(board, highlightbackground="black", highlightthickness=2)
            frame.grid(row=i, column=j)
            
            for k in range(3):
                for l in range(3):
                    label = tk.Label(frame, text=solution[i*3+k][j*3+l], width=4)
                    label.grid(row=k, column=l)

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
    root.title("Sudoku SMT Solver")

    title = tk.Label(root, text="Sudoku SMT Solver", font='TkDefaultFont 18 bold')
    label1 = tk.Label(root, text="Enter a puzzle: ")
    title.pack()
    label1.pack()

    entries = CreateInputGrid(root)

    def Solve():
        # Destroy all widgets under the solution label
        for widget in root.winfo_children():
            if widget.winfo_y() > solutionLabel.winfo_y():
                widget.destroy()

        sudokuGrid = GetInputs(entries)
        solution = solver.SudokuSolver(sudokuGrid)

        if solution == "unsat":
            returnLabel = tk.Label(root, text="unsat")
            returnLabel.pack()
        else:
            CreateOutputGrid(root, entries, solution)

    solveButton = tk.Button(root, text="Solve", bg="yellow", command=Solve)
    solutionLabel = tk.Label(root, text="Solution:")
    solveButton.pack()
    solutionLabel.pack()

    root.mainloop()
