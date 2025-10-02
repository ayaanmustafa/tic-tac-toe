import tkinter as tk
from tkinter import messagebox
import sys

def show_popup(char):
    return messagebox.askyesno("Congrats",f"Congrats {char}!! You won. Wanna replay?")

def is_board_full():
    for row in grid:
        for cell in row:
            if cell == "":  
                return False
    return True

grid = [["","",""],
        ["","",""],
        ["","",""]]

def reset():
    global grid, turn
    grid = [["","",""], ["","",""], ["","",""]]
    turn = True
    for i in range(3):
        for j in range(3):
            cells[i][j].config(text=" ", bg="SystemButtonFace") 

def check_win():
    for i in range(2):
        if grid[i][0] == grid[i][1] == grid[i][2] == "X" or grid[0][i] == grid[1][i] == grid[2][i] == "X":
            reset() if show_popup("X") else sys.exit()
        elif grid[i][0] == grid[i][1] == grid[i][2] == "O" or grid[0][i] == grid[1][i] == grid[2][i] == "O":
            reset() if show_popup("O") else sys.exit()
    
    if grid[0][0] == grid[1][1] == grid[2][2] == "X" or grid[0][2] == grid[1][1] == grid[2][0] == "X":
        reset() if show_popup("X") else sys.exit()
    elif grid[0][0] == grid[1][1] == grid[2][2] == "O" or grid[0][2] == grid[1][1] == grid[2][0] == "O":
        reset() if show_popup("O") else sys.exit()

    if is_board_full():
        if messagebox.askyesno("Tie", "It's a tie! Replay?"):
            reset()
        else:
            sys.exit()

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x450")
root.configure(bg='light slate gray') 
root.resizable(0,0)

turn = True
cells = []
def main():
    global cells
    l = tk.Label(root,text="TIC-TAC-TOE",font=("Chiller",25, "bold")).pack(anchor="n",pady=20)
    frame = tk.Frame(root, bg="black", bd=0)
    frame.pack(anchor="center")

    
    def on_click(x,y):
        global turn
        if grid[x][y] != "":
            return 
        if turn:
            cells[x][y].config(text="X",fg="white",bg="firebrick2")
            grid[x][y] = "X"
        else:
            cells[x][y].config(text="O",fg="light gray",bg="Deep sky blue")
            grid[x][y] = "O"
        turn = not turn
        check_win()


    for i in range(3):
        row = []
        for j in range(3):
            b = tk.Button(frame, text=" ", font=("Arial", 18, "bold"),
                        width=6, height=3, relief="raised",
                        command=lambda i=i, j=j: on_click(i,j))
            row.append(b)
            b.grid(row=i,column=j,padx=2,pady=2)
        cells.append(row)

main()
root.mainloop()


