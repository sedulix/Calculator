import tkinter as tk


def load_themes(root):
    return {
        # LIGHT THEME ----------------------->
        "light": {
            "root_bg": "#FFFFFF",
            "entry_bg": "#FFFFFF",
            "entry_fg": "#000000",
            "entry_insert": "#000000",
            "text_bg": "#FFFFFF",
            "text_fg": "#000000",
            "button_bg": "#FFFAFA",
            "button_fg": "#000000",
            "button_active_bg": "#FFF0F5",
            "switch_bg": "#F8F8FF",
            "switch_active_bg": "#FFFAF0",
            "clear_bg": "#F8F8FF",
            "clear_active_bg": "#FFFAF0",
            "font": ('Impact', 18),
            "theme_icon": tk.PhotoImage(master=root, file="source/night_mode.png")
        },

        # DARK THEME ------------------------>
        "dark": {
            "root_bg": "#2B2B2B",
            "entry_bg": "#3C3F41",
            "entry_fg": "#FFFFFF",
            "entry_insert": "#FFFFFF",
            "text_bg": "#3C3F41",
            "text_fg": "#FFFFFF",
            "button_bg": "#555555",
            "button_fg": "#FFFFFF",
            "button_active_bg": "#424242",
            "switch_bg": "#555555",
            "switch_active_bg": "#424242",
            "clear_bg": "#555555",
            "clear_active_bg": "#424242",
            "font": ('Impact', 18),
            "theme_icon": tk.PhotoImage(master=root, file="source/light_mode.png")
        }

        # You can also add your own colors
        # "theme name": {
        
        # }
    }


