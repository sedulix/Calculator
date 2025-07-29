import tkinter as tk
from tkinter import scrolledtext
from tkinter import *

from themes import load_themes
from logic import CalculatorLogic


# <--------------------------------------------------< GUI >----------------------------------------------------------->

root = tk.Tk()

root.title('calculator')
root.geometry('1200x594+350+200')
root.resizable(False, False)
root.attributes("-alpha", 0.9)

icon = PhotoImage(file='source/calculator.png')
root.iconphoto(False, icon)


# ENTRY ---------------------------------->

entry = tk.Text(root, font=('Impact', 30), width=35, height=4, padx=0, pady=0, background='#FFFFFF')
entry.grid(row=0, columnspan=4)


# THEMES --------------------------------->

themes = load_themes(root)
default_theme = "light"
theme_data = themes[default_theme]


# JOURNAL FRAME -------------------------->

history_frame = tk.Frame(root)
history_frame.grid(row=0, column=4, rowspan=8, padx=1, pady=0.1, sticky='ns')

history_text = scrolledtext.ScrolledText(history_frame, font=('Impact', 19), width=34, height=17.5)
history_text.grid(row=1, column=4, rowspan=6, sticky='nsew')


# CLEAR JOURNAL BUTTON ------------------->

clear_history_button = tk.Button(root, text="clear journal", font=theme_data["font"], height=2, width=29,
                                 activebackground=theme_data["clear_active_bg"], background=theme_data["clear_bg"],
)
clear_history_button.place(x=738, y=515)


# SWITCH THEME BUTTON -------------------->

switch_theme_button = tk.Button(root, image=theme_data["theme_icon"], height=74, width=84,
                                activebackground=theme_data["clear_active_bg"], background=theme_data["clear_bg"],
)
switch_theme_button.place(x=1096, y=515)


# CALCULATOR LOGIC OBJECT -------------------------------------------------------------------------------------------<<<


cal_logic = CalculatorLogic(root=root, themes=themes, entry=entry, history_text=history_text,
                            switch_theme_button=switch_theme_button, clear_history_text=clear_history_button
)


# <-----------------------------------------------< CALCULATOR KEYBOARD >---------------------------------------------->


buttons = [('.', 3, 0), ('^', 3, 1), ('%', 3, 2), ('⌫', 3, 3),
           ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
           ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
           ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
           ('C', 7, 0), ('0', 7, 1), ('=', 7, 2), ('+', 7, 3)]


for (text, row, col) in buttons:
    if text in {'^', '%', '/', '*', '-', '+'}:
        cmd = lambda t=text: cal_logic.add_operation_to_text(t)
    elif text == 'C':
        cmd = cal_logic.clear_text
    elif text == '⌫':
        cmd = cal_logic.delete_last_char
    elif text == '=':
        cmd = cal_logic.calculate
    else:
        cmd = lambda t=text: cal_logic.insert_to_text(t)

    cal_logic.create_button(text, row, col, cmd)


# CLEAR HISTORY AND SWITCH THEME BUTTONS ->

clear_history_button.config(command=cal_logic.clear_journal)
switch_theme_button.config(command=cal_logic.switch_theme)


# APPLY DEFAULT THEME -------------------->

cal_logic.apply_theme(default_theme)
root.mainloop()

