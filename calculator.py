import tkinter as tk
from tkinter import messagebox
import streamlit as st

# =====================================
# Calculator Functions
# =====================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# =====================================
# Main Window
# =====================================

root = tk.Tk()
root.title("Modern Aesthetic Calculator")
root.geometry("430x700")
root.resizable(False, False)

# =====================================
# Themes
# =====================================

DARK_BG = "#1E1E2E"
DARK_BUTTON = "#313244"
DARK_TEXT = "white"

LIGHT_BG = "#F5F5F5"
LIGHT_BUTTON = "#D6D6D6"
LIGHT_TEXT = "black"

current_theme = "dark"

all_buttons = []

# =====================================
# Entry Box
# =====================================

entry = tk.Entry(
    root,
    font=("Poppins", 28, "bold"),
    bd=0,
    justify="right"
)

entry.pack(pady=20, padx=20, fill="both", ipady=20)

# =====================================
# History Section
# =====================================

history_label = tk.Label(
    root,
    text="Calculation History",
    font=("Poppins", 14, "bold")
)

history_label.pack()

history_box = tk.Text(
    root,
    height=7,
    font=("Consolas", 12),
    bd=0
)

history_box.pack(padx=20, pady=10, fill="both")

# =====================================
# Apply Theme
# =====================================

def apply_theme():

    if current_theme == "dark":

        root.configure(bg=DARK_BG)

        entry.configure(
            bg="#45475A",
            fg="white",
            insertbackground="white"
        )

        history_box.configure(
            bg="#313244",
            fg="white"
        )

        history_label.configure(
            bg=DARK_BG,
            fg="white"
        )

        for button in all_buttons:
            button.configure(
                bg=DARK_BUTTON,
                fg="white",
                activebackground="#89B4FA"
            )

    else:

        root.configure(bg=LIGHT_BG)

        entry.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        history_box.configure(
            bg="#EAEAEA",
            fg="black"
        )

        history_label.configure(
            bg=LIGHT_BG,
            fg="black"
        )

        for button in all_buttons:
            button.configure(
                bg=LIGHT_BUTTON,
                fg="black",
                activebackground="#B4BEFE"
            )

# =====================================
# Toggle Theme
# =====================================

def toggle_theme():
    global current_theme

    if current_theme == "dark":
        current_theme = "light"
    else:
        current_theme = "dark"

    apply_theme()

# =====================================
# Click Function
# =====================================

def click(value):

    current = entry.get()

    entry.delete(0, tk.END)

    entry.insert(0, current + str(value))

# =====================================
# Clear Screen
# =====================================

def clear_screen():
    entry.delete(0, tk.END)

# =====================================
# Animation Effect
# =====================================

def animate(button):

    button.config(font=("Poppins", 20, "bold"))

    root.after(
        100,
        lambda: button.config(font=("Poppins", 18, "bold"))
    )

# =====================================
# Calculate Function
# =====================================

def calculate():

    try:

        expression = entry.get()

        if not expression:
            messagebox.showerror(
                "Error",
                "Please enter a calculation"
            )
            return

        if '+' in expression:
            a, b = expression.split('+')
            result = add(float(a), float(b))

        elif '-' in expression:
            a, b = expression.split('-')
            result = subtract(float(a), float(b))

        elif '*' in expression:
            a, b = expression.split('*')
            result = multiply(float(a), float(b))

        elif '/' in expression:
            a, b = expression.split('/')
            result = divide(float(a), float(b))

        else:
            messagebox.showerror(
                "Error",
                "Invalid operator"
            )
            return

        # Add to history
        history_box.insert(
            tk.END,
            f"{expression} = {result}\n"
        )

        # Show result
        entry.delete(0, tk.END)

        entry.insert(0, str(result))

    except ZeroDivisionError:

        messagebox.showerror(
            "Math Error",
            "Cannot divide by zero"
        )

    except Exception:

        messagebox.showerror(
            "Error",
            "Invalid input"
        )

# =====================================
# Keyboard Support
# =====================================

def key_event(event):

    key = event.char

    allowed = "1234567890+-*/."

    if key in allowed:
        click(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":

        current = entry.get()

        entry.delete(0, tk.END)

        entry.insert(0, current[:-1])

root.bind("<Key>", key_event)

# =====================================
# Buttons Frame
# =====================================

frame = tk.Frame(root)

frame.pack(pady=10)

# =====================================
# Buttons Layout
# =====================================

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# =====================================
# Create Buttons
# =====================================

for row in buttons:

    row_frame = tk.Frame(frame)

    row_frame.pack()

    for btn in row:

        if btn == "=":
            action = calculate

        elif btn == "C":
            action = clear_screen

        else:
            action = lambda x=btn: click(x)

        button = tk.Button(
            row_frame,
            text=btn,
            font=("Poppins", 18, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            width=5,
            height=2,
            command=lambda a=action: a()
        )

        button.pack(
            side="left",
            padx=10,
            pady=10
        )

        all_buttons.append(button)

# =====================================
# Theme Toggle Button
# =====================================

mode_button = tk.Button(
    root,
    text="Toggle Dark/Light Mode",
    font=("Poppins", 12, "bold"),
    command=toggle_theme,
    relief="flat",
    bd=0,
    cursor="hand2"
)

mode_button.pack(pady=10)

all_buttons.append(mode_button)

# =====================================
# Apply Initial Theme
# =====================================

apply_theme()

# =====================================
# Run App
# =====================================

root.mainloop()