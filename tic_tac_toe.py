from tkinter import *
from functools import partial
from itertools import product
import random
from time import time, sleep


root = Tk()
root.title("Tic-Tac")
isWork = True
matrix = []
x_text = "X"
o_text = "O"
isCross = False
button_id = []
d_list = []
isValue = False
rows_number = IntVar()
columns_number = IntVar()

rows = rows_number.get()
columns = columns_number.get()



def change(i, j):
    global isValue
    global isCross
    rows = rows_number.get()
    columns = columns_number.get()
    bname = button_id[i][j]
    if isCross:
        if matrix[i][j] == None or matrix[i][j] == "X":
            matrix[i][j] = "X"
            bname.config(text="X")
            isCross = False
        elif matrix[i][j] == None or matrix[i][j] == "0":
            matrix[i][j] = "0"
            bname.config(text="0")
            isCross = True
    else:
        if matrix[i][j] == None or matrix[i][j] == "0":
            matrix[i][j] = "0"
            bname.config(text="0")
            isCross = True
        elif matrix[i][j] == None or matrix[i][j] == "X":
            matrix[i][j] = "X"
            bname.config(text="X")
            isCross = False

    game_result = validate_game_state()
    print(game_result)

def validate_game_state():
    '''
    returs: one of 4 game states: 1 - nobody wins, 2 - tie, 3 - x wins, 4 - y wins
    '''

    for i in range(0, len(matrix)):
        is_row_assembled = False
        current_row_winner = matrix[i][0]

        if current_row_winner == None:
            break

        for j in range(1, len(matrix[0])):
            if matrix[i][j] != current_row_winner:
                is_row_assembled = False
                break
            else: 
                is_row_assembled = True
        
        if is_row_assembled and current_row_winner == "X":
            return 3
        elif is_row_assembled and current_row_winner == "0":
            return 4

    return None


rows_number = IntVar()
columns_number = IntVar()

def get_buttons():
    ok_button.destroy()
    rows_label.destroy()
    columns_label.destroy()
    which_rows.destroy()
    which_columns.destroy()
    rows = rows_number.get()
    columns = columns_number.get()
    for i in range(0, rows):
        button_id.append([])
        matrix.append([])
        for j in range(0, columns):
            matrix[i].append(None)
            btn_press = Button(root, text=" ", width=4, height=2, command=partial(change, i, j))
            btn_press.grid(row=i, column=j, sticky="n,e,s,w", ipadx=10, ipady=6, padx=10, pady=10)
            button_id[i].append(btn_press)

    btn_restart = Button(root, text="Restart", width=4, height=2)
    btn_restart.grid(row=rows + 1, column=columns//2, ipadx=10, ipady=6, padx=10, pady=10)

rows_label = Label(root, text="Enter number of rows")
columns_label = Label(root, text="Enter numbers of columns")

which_rows = Entry(root, textvariable=rows_number)
which_columns = Entry(root, textvariable=columns_number)

rows_label.grid(row=0, column=0, sticky="w")
columns_label.grid(row=1, column=0, sticky="w")
which_rows.grid(row=0,column=2, padx=5, pady=5)
which_columns.grid(row=1,column=2, padx=5, pady=5)
ok_button = Button(text="Ok", command=partial(get_buttons))
ok_button.grid(row=2, column=2, padx=5, pady=5, sticky="e")




root.mainloop()


def smth(numb):
    print()
    print(numb**2)
    print()

    print_sqrt_smth(numb)

def print_sqrt_smth(numb):
    print(numb**(1/2))