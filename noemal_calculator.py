import re
from tkinter import scrolledtext
from tkinter import *
import tkinter as tk

# ----------------------------------------------------< functions >-----------------------------------------------------


def insert_to_text(value):
    entry.insert(tk.END, value)


def add_operation_to_text(operation):
    value = entry.get('1.0', tk.END).strip()
    if value and value[-1] in '+-/*^%':
        value = value[:-1]

    clear_text()
    entry.insert(tk.END, value+operation)


def calculate():
    try:
        value = entry.get('1.0', tk.END).strip()
        value = value.replace('^', '**')
        value = re.sub(r'[^0-9+\-*/().%]', '', value)
        if value:
            result = eval(value)

            history_text.insert(tk.END, f'{value.replace('**', '^')} = \n {result}\n \n')
            history_text.see(tk.END)

            clear_text()
            entry.insert(tk.END, str(result))

    except Exception:
        clear_text()
        entry.insert(tk.END, 'INVALID SYNTAX')


def switch_theme():
    current_bg = root.cget('bg')
    # dark
    if current_bg == '#FFFFFF':
        root.config(background="#2B2B2B")
        entry.config(background="#3C3F41", foreground="#FFFFFF", insertbackground="#FFFFFF")
        history_text.config(background="#3C3F41", foreground="#FFFFFF")
        switch_theme_button.config(background='#555555', image=theme_icon_w)
        clear_history_button.config(background="#555555", foreground="#FFFFFF", activebackground="#424242")

        for widget in root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(background="#555555", foreground="#FFFFFF", activebackground="#424242",
                              activeforeground="#FFFFFF")

    # light
    else:
        root.config(background='#FFFFFF')
        entry.config(background='#FFFFFF', foreground='#000000', insertbackground='#000000')
        history_text.config(background='#FFFFFF', foreground='#000000')
        switch_theme_button.config(background='#F8F8FF', activebackground='#FFFAF0', image=theme_icon_b)
        clear_history_button.config(background='#F8F8FF', foreground='#000000', activebackground='#FFFAF0')

        for widget in root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(background="#FFFAFA", foreground="#000000", activebackground="#FFF0F5",
                              activeforeground="#000000")


def delete_last_char():
    content = entry.get('1.0', tk.END).strip()
    clear_text()
    entry.insert(tk.END, content[:-1])


def clear_text():
    entry.delete("1.0", END)


def clear_journal():
    history_text.delete('1.0', tk.END)


# <--------------------------------------------------< Frame.text >---------------------------------------------------->
root = tk.Tk()
root.title('calculator')
root.geometry('1200x594+350+200')
root.resizable(False, False)
root.attributes("-alpha", 0.9)

icon = PhotoImage(file='calculator.png')
root.iconphoto(False, icon)

entry = tk.Text(root, font=('Impact', 30), width=35, height=4, padx=0, pady=0, background='#FFFFFF')
entry.grid(row=0, columnspan=4)

# <---------------------------------------------------< buttons >_----------------------------------------------------->
theme_icon_b = tk.PhotoImage(file='black.png')
theme_icon_w = tk.PhotoImage(file='white.png')

buttons = [('.', 3, 0), ('^', 3, 1), ('%', 3, 2), ('<-', 3, 3),
           ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
           ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
           ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
           ('C', 7, 0), ('0', 7, 1), ('=', 7, 2), ('+', 7, 3)]

for (text, row, col) in buttons:
    if text in {'^', '%', '/', '*', '-', '+'}:
        button = tk.Button(root, text=text, font=('Impact', 18), width=14, height=2, relief='flat',
                           activebackground='#FFF0F5', background='#FFFAFA',
                           command=lambda t=text: add_operation_to_text(t))
    elif text == 'C':
        button = tk.Button(root, text='C', font=('Impact', 18), width=14, height=2, relief='flat', background='#FFFAFA',
                           activebackground='#FFF0F5', command=clear_text)
    elif text == '<-':
        button = tk.Button(root, text='<-', font=('Impact', 18), width=14, height=2, relief='flat',
                           background='#FFFAFA', activebackground='#FFF0F5', command=delete_last_char)
    elif text == '=':
        button = tk.Button(root, text='=', font=('Impact', 18), width=14, height=2, relief='flat', background='#FFFAFA',
                           activebackground='#FFF0F5', command=calculate)
    else:
        button = tk.Button(root, text=text, font=('Impact', 18), width=14, height=2, relief='flat',
                           background='#FFFAFA', activebackground='#FFF0F5', command=lambda t=text: insert_to_text(t))
        button.config(relief='flat')

    button.grid(row=row, column=col, padx=0, pady=0, sticky='nsew')


history_frame = tk.Frame(root)
history_frame.config()
history_frame.grid(row=0, column=4, rowspan=8, padx=1, pady=0.1, sticky='ns')

history_text = scrolledtext.ScrolledText(history_frame, font=('Impact', 19), width=34, height=17.5)
history_text.grid(row=1, column=4, rowspan=6, sticky='nsew')


clear_history_button = tk.Button(root, text="clear journal", font=('Impact', 18), height=2, width=29,
                                 activebackground='#FFFAF0', background='#F8F8FF', command=clear_journal)
clear_history_button.place(x=738, y=515)

switch_theme_button = tk.Button(root, image=theme_icon_b, height=74, width=84, background='#F8F8FF',
                                activebackground='#FFFAF0', command=switch_theme)
switch_theme_button.place(x=1096, y=515)


root.mainloop()
