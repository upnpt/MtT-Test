import tkinter as tk
from tkinter import messagebox
import random

# สุ่มเลข 1-100
secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts, secret_number

    guess = entry.get()

    if not guess.isdigit():
        messagebox.showwarning("ผิดพลาด", "กรุณาใส่ตัวเลข")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        result.config(text="📉 น้อยเกินไป", fg="blue")
    elif guess > secret_number:
        result.config(text="📈 มากเกินไป", fg="orange")
    else:
        messagebox.showinfo(
            "ยินดีด้วย!",
            f"คุณทายถูก!\nใช้ไป {attempts} ครั้ง"
        )
        secret_number = random.randint(1, 100)
        attempts = 0
        result.config(text="เริ่มเกมใหม่แล้ว!", fg="green")

    entry.delete(0, tk.END)


# สร้างหน้าต่าง
root = tk.Tk()
root.title("เกมทายตัวเลข")
root.geometry("350x250")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🎮 เกมทายตัวเลข",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

label = tk.Label(root, text="ทายเลขระหว่าง 1 - 100")
label.pack()

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

btn = tk.Button(
    root,
    text="ทาย",
    font=("Arial", 12),
    command=check_guess
)
btn.pack()

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

root.mainloop()