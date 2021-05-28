import tkinter
from random import randrange
from tkinter import messagebox

root = tkinter.Tk()
root.title('Minesweeper')
root.geometry('1000x800')

board = [[None for i in range(10)] for j in range(10)]
is_game_over = False


def on_box_click(event):
    global is_game_over
    if not is_game_over:
        if event.widget.cget('text') == 'X':
            messagebox.showwarning(title='Alert', message='You Lose...!')
            is_game_over = True


def create_game():
    for _ in range(10):
        row = randrange(10)
        col = randrange(10)
        button = tkinter.Button(root, text='X', fg='red', borderwidth=1, width=9, height=3)
        button.grid(row=row, column=col)
        button.bind('<Button-1>', on_box_click)
        board[row][col] = button
    for i in range(10):
        for j in range(10):
            if board[i][j] is None:
                button = tkinter.Button(root, text=' ', borderwidth=1, width=9, height=3)
                button.grid(row=i, column=j)
                button.bind('<Button-1>', on_box_click)


def new_game():
    global board
    board = [[None for _ in range(10)] for _ in range(10)]
    create_game()


def main():
    create_game()
    root.mainloop()


main()
