import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Назарук, ЛР №3.3, завдання №1")
root.geometry("360x750")
root.resizable(False, False)
root.configure(bg="#20242D")

icon = tk.PhotoImage(width=32, height=32)
icon.put("#20242D", to=(0, 0, 32, 32))
icon.put("#FF5555", to=(6, 5, 26, 27))
icon.put("#FFFFFF", to=(10, 9, 22, 11))
icon.put("#FFFFFF", to=(10, 14, 22, 16))
icon.put("#FFFFFF", to=(10, 19, 19, 21))
root.iconphoto(True, icon)

BG = "#20242D"
PANEL = "#2B303B"
ACCENT = "#FF5555"
FG = "#F1F1F1"
MUTED = "#B8BEC9"

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Custom.TButton",
    font=("Segoe UI", 10),
    background=PANEL,
    foreground=FG,
    padding=8,
    borderwidth=0
)

style.map(
    "Custom.TButton",
    background=[("active", ACCENT)],
    foreground=[("active", "white")]
)

style.configure(
    "Custom.TRadiobutton",
    background=BG,
    foreground=FG,
    font=("Segoe UI", 10)
)

style.map(
    "Custom.TRadiobutton",
    background=[("active", BG)],
    foreground=[("active", ACCENT)]
)

style.configure(
    "Custom.TCheckbutton",
    background=BG,
    foreground=FG,
    font=("Segoe UI", 10)
)

style.map(
    "Custom.TCheckbutton",
    background=[("active", BG)],
    foreground=[("active", ACCENT)]
)

title = tk.Label(
    root,
    text="АНКЕТА",
    font=("Segoe UI", 17, "bold"),
    bg=BG,
    fg=ACCENT,
    pady=12
)
title.pack()

tk.Label(
    root,
    text="Введіть ваше ім'я",
    font=("Segoe UI", 10),
    bg=BG,
    fg=FG
).pack(pady=(5, 3))

name_entry = tk.Entry(
    root,
    font=("Segoe UI", 11),
    bg=PANEL,
    fg=FG,
    insertbackground=FG,
    relief="flat",
    width=27
)
name_entry.pack(ipady=5)
name_entry.insert(0, "Максим")

tk.Label(
    root,
    text="Введіть ваше прізвище",
    font=("Segoe UI", 10),
    bg=BG,
    fg=FG
).pack(pady=(12, 3))

surname_entry = tk.Entry(
    root,
    font=("Segoe UI", 11),
    bg=PANEL,
    fg=FG,
    insertbackground=FG,
    relief="flat",
    width=27
)
surname_entry.pack(ipady=5)
surname_entry.insert(0, "Назарук")

number = tk.IntVar(value=10)

for i in range(1, 12):
    ttk.Radiobutton(
        root,
        text=str(i),
        variable=number,
        value=i,
        style="Custom.TRadiobutton"
    ).pack(anchor="center", pady=2)

male = tk.BooleanVar(value=True)
female = tk.BooleanVar(value=False)

ttk.Checkbutton(
    root,
    text="Чол",
    variable=male,
    style="Custom.TCheckbutton"
).pack(pady=(8, 2))

ttk.Checkbutton(
    root,
    text="Жін",
    variable=female,
    style="Custom.TCheckbutton"
).pack(pady=2)

def highlight():
    title.config(bg=ACCENT, fg="white")

def default():
    title.config(bg=BG, fg=ACCENT)

ttk.Button(
    root,
    text="Підсвітити заголовок",
    command=highlight,
    style="Custom.TButton"
).pack(pady=(12, 5))

ttk.Button(
    root,
    text="За замовчуванням",
    command=default,
    style="Custom.TButton"
).pack(pady=3)

tk.Label(
    root,
    text="ПРИМІТКА",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=ACCENT
).pack(pady=(12, 5))

note = tk.Text(
    root,
    height=5,
    width=37,
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=FG,
    insertbackground=FG,
    relief="flat",
    padx=7,
    pady=7
)
note.pack(padx=15, fill="x")

note.insert(
    "1.0",
    "Максим\n"
    "Назарук\n"
    "Хлопець\n"
    "Навчається на 2 курсі"
)

def show_data():
    messagebox.showinfo(
        "Дані анкети",
        f"Ім'я: {name_entry.get()}\n"
        f"Прізвище: {surname_entry.get()}\n"
        f"Число: {number.get()}\n"
        f"Стать: {'Чол' if male.get() else 'Жін' if female.get() else 'Не вказано'}\n\n"
        f"Примітка:\n{note.get('1.0', 'end-1c')}"
    )

ttk.Button(
    root,
    text="Дані",
    command=show_data,
    style="Custom.TButton"
).pack(pady=12)

root.mainloop()
