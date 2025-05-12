import tkinter as tk
from tkinter import messagebox

# Main window setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

# Game state variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for row in buttons:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            return True

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn['text'] == "":
                return False
    return True

def on_click(row, col):
    global current_player

    btn = buttons[row][col]
    if btn["text"] == "":
        btn["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

# Create buttons in a grid
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", width=10, height=4,
                        font=("Helvetica", 16),
                        command=lambda row=i, col=j: on_click(row, col))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# Reset button
tk.Button(root, text="Reset Game", command=reset_game).grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
