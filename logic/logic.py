import tkinter as tk
import re


# CALCULATOR LOGIC CLASS -------------------------------------------------------------------------------------------[CL]


class CalculatorLogic:
    def __init__(self, root, themes, entry, history_text, switch_theme_button, clear_history_text):
        self.root = root
        self.themes = themes
        self.entry = entry
        self.history_text = history_text
        self.switch_theme_button = switch_theme_button
        self.clear_history_text = clear_history_text
        self.current_theme = "light"


    # INSERT TEXT INTO ENTRY ------------------------------------------------------------------------------------------<


    def insert_to_text(self, value):
        self.entry.insert(tk.END, value)


    # ADD OPERATIONS COMMAND ------------------------------------------------------------------------------------------<


    def add_operation_to_text(self, operation):
        value = self.entry.get("1.0", tk.END).strip()
        if value and value[-1] in '+-/*^%':
            value = value[:-1]

        self.clear_text()
        self.entry.insert("1.0", value + operation)


    # CALCULATE THE EXPRESSION ---------------------------------------------------------------------------------------->


    def calculate(self):
        try:
            value = self.entry.get('1.0', tk.END).strip()
            value = value.replace('^', '**')
            value = re.sub(r'[^0-9+\-*/().%]', '', value)

            if value:
                result = eval(value)

                self.history_text.insert(tk.END, f'{value.replace("**", "^")} = \n {result}\n \n')
                self.history_text.see(tk.END)

                self.clear_text()
                self.entry.insert(tk.END, str(result))

        except Exception as e:
            self.clear_text()
            self.entry.insert(tk.END, f'INVALID SYNTAX: {e}')


    # APPLY THEME NAME ------------------------------------------------------------------------------------------------<


    def apply_theme(self, theme_name):
        theme = self.themes[theme_name]
        self.root.config(bg=theme["root_bg"])
        self.entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"], insertbackground=theme["entry_insert"])
        self.history_text.config(bg=theme["text_bg"], fg=theme["text_fg"])
        self.switch_theme_button.config(bg=theme["switch_bg"], activebackground=theme["switch_active_bg"],
                                        image=theme["theme_icon"])
        self.clear_history_text.config(bg=theme["switch_bg"], fg=theme["button_fg"],
                                         activebackground=theme["button_active_bg"])

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=theme["button_bg"], fg=theme["button_fg"],
                              activebackground=theme["button_active_bg"],
                              activeforeground=theme["button_fg"])

        self.current_theme = theme_name


    # CREATE KEYBOARD BUTTONS -----------------------------------------------------------------------------------------<


    def create_button(self, text, row, col, cmd):
        theme = self.themes[self.current_theme]
        btn = tk.Button(self.root, text=text, font=theme["font"], width=14, height=2, relief="flat",
                            background=theme["button_bg"], activebackground=theme["button_active_bg"], command=cmd)
        btn.grid(row=row, column=col, sticky="nsew")
        return btn


    # CLEAR ENTRY COMMAND --------------------------------------------------------------------------------------------->


    def clear_text(self):
        self.entry.delete('1.0', tk.END)


    # SWITCH THEME COMMAND -------------------------------------------------------------------------------------------->


    def switch_theme(self):
        new_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme(new_theme)


    # DELETE LAST CHAR COMMAND ---------------------------------------------------------------------------------------->


    def delete_last_char(self):
        content = self.entry.get('1.0', "end-1c")
        self.clear_text()
        self.entry.insert("1.0", content[:-1])


    # CLEAR JOURNAL TEXT ---------------------------------------------------------------------------------------------->


    def clear_journal(self):
        self.history_text.delete('1.0', tk.END)

