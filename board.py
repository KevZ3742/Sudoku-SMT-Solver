import tkinter as tk

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
        inputs.append(entry.get())
    print(inputs)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku Sat Solver")

    title = tk.Label(root, text="Sudoku Sat Solver", font='TkDefaultFont 18 bold')
    lable1 = tk.Label(root, text="Enter a puzzle: ")
    title.pack()
    lable1.pack()

    entries = CreateInputGrid(root)

    solveButton = tk.Button(root, text="Solve", bg="yellow", command=lambda: GetInputs(entries))
    solveButton.pack()

    root.mainloop()
