import tkinter as tk
from tkinter import messagebox

# Initialize the game
current_player = "X"
game_over = False

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create the buttons for the cells
buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]


# Function to handle button click
def on_click(row, col):
    global current_player, game_over

    # If the cell is already occupied or the game is over, do nothing
    if buttons[row][col]["text"] or game_over:
        return

    # Set the text of the button to the current player
    buttons[row][col]["text"] = current_player

    # Check for a win or a tie
    if check_win(current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        game_over = True
    elif check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        game_over = True
    else:
        # Switch to the next player
        current_player = "O" if current_player == "X" else "X"


# Function to check for a win
def check_win(player):
    # Check rows
    for row in range(3):
        if (buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] == player):
            return True

    # Check columns
    for col in range(3):
        if (buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] == player):
            return True

    # Check diagonals
    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player) or \
            (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player):
        return True

    return False


# Function to check for a tie
def check_tie():
    for row in range(3):
        for col in range(3):
            if not buttons[row][col]["text"]:
                return False
    return True


# Create the buttons and attach the click event
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(window, text="", font=("Arial", 20), width=6, height=3,
                                     command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Run the main event loop
window.mainloop()
