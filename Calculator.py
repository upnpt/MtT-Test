import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("500x750")
root.configure(bg="#202124")
root.resizable(False, False)

expression = ""

# ======================
# Display
# ======================
display = tk.Entry(
    root,
    font=("Segoe UI", 30),
    bg="#202124",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", padx=15, pady=20, ipady=20)

# ======================
# Functions
# ======================
def press(value):
    global expression
    expression += str(value)
    update_display()

def update_display():
    display.delete(0, tk.END)
    display.insert(0, expression)

def clear():
    global expression
    expression = ""
    update_display()

def backspace():
    global expression
    expression = expression[:-1]
    update_display()

def plus_minus():
    global expression
    if expression:
        try:
            expression = str(float(expression) * -1)
            if expression.endswith(".0"):
                expression = expression[:-2]
            update_display()
        except:
            pass

def percent():
    global expression
    try:
        expression = str(eval(expression) / 100)
        update_display()
    except:
        pass

def calculate():
    global expression
    try:
        result = str(eval(expression))
        expression = result
        update_display()
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        expression = ""

# ======================
# Button Style
# ======================
btn_font = ("Segoe UI", 18)

def make_button(text, row, col, cmd,
                bg="#3c4043",
                fg="white"):

    button = tk.Button(
        frame,
        text=text,
        font=btn_font,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        bd=0,
        command=cmd
    )

    button.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=4,
        pady=4
    )

# ======================
# Buttons Frame
# ======================
frame = tk.Frame(root, bg="#202124")
frame.pack(fill="both", expand=True, padx=10, pady=10)

for i in range(6):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

# Row 1
make_button("C", 0, 0, clear, "#5f6368")
make_button("⌫", 0, 1, backspace, "#5f6368")
make_button("%", 0, 2, percent, "#5f6368")
make_button("÷", 0, 3, lambda: press("/"), "#ff9500")

# Row 2
make_button("7", 1, 0, lambda: press("7"))
make_button("8", 1, 1, lambda: press("8"))
make_button("9", 1, 2, lambda: press("9"))
make_button("×", 1, 3, lambda: press("*"), "#ff9500")

# Row 3
make_button("4", 2, 0, lambda: press("4"))
make_button("5", 2, 1, lambda: press("5"))
make_button("6", 2, 2, lambda: press("6"))
make_button("-", 2, 3, lambda: press("-"), "#ff9500")

# Row 4
make_button("1", 3, 0, lambda: press("1"))
make_button("2", 3, 1, lambda: press("2"))
make_button("3", 3, 2, lambda: press("3"))
make_button("+", 3, 3, lambda: press("+"), "#ff9500")

# Row 5
make_button("±", 4, 0, plus_minus)
make_button("0", 4, 1, lambda: press("0"))
make_button(".", 4, 2, lambda: press("."))
make_button("=", 4, 3, calculate, "#00a67e")

# ======================
# Keyboard Support
# ======================
def key_press(event):
    key = event.char

    if key in "0123456789+-*/.":
        press(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        backspace()

    elif event.keysym == "Escape":
        clear()

root.bind("<Key>", key_press)

root.mainloop()