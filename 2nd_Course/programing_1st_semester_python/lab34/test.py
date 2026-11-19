import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Назарук, ЛР 3.4, завдання 1")
root.geometry("600x850")
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
    "Custom.TRadiobutton",
    background=PANEL,
    foreground=FG,
    font=("Segoe UI", 10)
)

style.map(
    "Custom.TRadiobutton",
    background=[("active", PANEL)],
    foreground=[("active", ACCENT)]
)

style.configure(
    "Custom.TCheckbutton",
    background=PANEL,
    foreground=FG,
    font=("Segoe UI", 10)
)

style.map(
    "Custom.TCheckbutton",
    background=[("active", PANEL)],
    foreground=[("active", ACCENT)]
)

style.configure(
    "Custom.TButton",
    font=("Segoe UI", 10, "bold"),
    background=PANEL,
    foreground=FG,
    padding=9,
    borderwidth=0
)

style.map(
    "Custom.TButton",
    background=[("active", ACCENT)],
    foreground=[("active", "white")]
)

style.configure(
    "Vertical.TScrollbar",
    background=PANEL,
    troughcolor=BG,
    borderwidth=0,
    arrowcolor=FG
)

header = tk.Label(
    root,
    text="ТЕСТ З ОСНОВ PYTHON",
    font=("Segoe UI", 19, "bold"),
    bg=BG,
    fg=ACCENT,
    pady=15
)
header.pack()

subtitle = tk.Label(
    root,
    text="Перевір свої знання програмування",
    font=("Segoe UI", 10),
    bg=BG,
    fg=MUTED
)
subtitle.pack(pady=(0, 12))

container = tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True, padx=12, pady=(0, 12))

canvas = tk.Canvas(
    container,
    bg=BG,
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    container,
    orient="vertical",
    command=canvas.yview,
    style="Vertical.TScrollbar"
)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

content = tk.Frame(canvas, bg=BG)

window_id = canvas.create_window(
    (0, 0),
    window=content,
    anchor="nw"
)

def update_scroll(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

def resize_content(event):
    canvas.itemconfigure(window_id, width=event.width)

content.bind("<Configure>", update_scroll)
canvas.bind("<Configure>", resize_content)

def mouse_scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)

def create_section(title):
    frame = tk.Frame(
        content,
        bg=PANEL,
        padx=15,
        pady=12
    )
    frame.pack(fill="x", pady=6)

    tk.Label(
        frame,
        text=title,
        font=("Segoe UI", 11, "bold"),
        bg=PANEL,
        fg=ACCENT,
        anchor="w",
        wraplength=480,
        justify="left"
    ).pack(fill="x", pady=(0, 8))

    return frame

identity = create_section("ІНФОРМАЦІЯ ПРО КОРИСТУВАЧА")

tk.Label(
    identity,
    text="Прізвище:",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=FG
).pack(anchor="w")

surname_entry = tk.Entry(
    identity,
    font=("Segoe UI", 11),
    bg=BG,
    fg=FG,
    insertbackground=FG,
    relief="flat"
)
surname_entry.pack(fill="x", ipady=6, pady=(3, 10))

tk.Label(
    identity,
    text="Група:",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=FG
).pack(anchor="w")

group_entry = tk.Entry(
    identity,
    font=("Segoe UI", 11),
    bg=BG,
    fg=FG,
    insertbackground=FG,
    relief="flat"
)
group_entry.pack(fill="x", ipady=6, pady=(3, 5))

warning = tk.Label(
    identity,
    text="",
    font=("Segoe UI", 9, "bold"),
    bg=PANEL,
    fg=ACCENT
)
warning.pack(anchor="w", pady=(5, 0))

q1 = tk.IntVar(value=0)
q2 = tk.IntVar(value=0)
q3 = [tk.BooleanVar(value=False) for _ in range(4)]
q4 = tk.StringVar()
q5 = tk.IntVar(value=0)
q6 = [tk.BooleanVar(value=False) for _ in range(4)]
q7 = tk.StringVar()
q8 = tk.IntVar(value=0)
q9 = [tk.BooleanVar(value=False) for _ in range(4)]
q10 = tk.StringVar()

frame = create_section("1. Яке розширення мають файли Python?")

for value, text in [
    (1, ".py"),
    (2, ".html"),
    (3, ".exe"),
    (4, ".css")
]:
    ttk.Radiobutton(
        frame,
        text=text,
        variable=q1,
        value=value,
        style="Custom.TRadiobutton"
    ).pack(anchor="w", pady=2)

frame = create_section("2. Яка функція використовується для визначення довжини рядка?")

for value, text in [
    (1, "size()"),
    (2, "len()"),
    (3, "count()"),
    (4, "length()")
]:
    ttk.Radiobutton(
        frame,
        text=text,
        variable=q2,
        value=value,
        style="Custom.TRadiobutton"
    ).pack(anchor="w", pady=2)

frame = create_section("3. Які з наведених типів даних існують у Python? (Декілька правильних)")

options = ["int", "str", "float", "number"]

for i, text in enumerate(options):
    ttk.Checkbutton(
        frame,
        text=text,
        variable=q3[i],
        style="Custom.TCheckbutton"
    ).pack(anchor="w", pady=2)

frame = create_section("4. Яким ключовим словом оголошується функція в Python?")

tk.Label(
    frame,
    text="Введіть відповідь:",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=FG
).pack(anchor="w")

entry4 = tk.Entry(
    frame,
    textvariable=q4,
    font=("Segoe UI", 11),
    bg=BG,
    fg=FG,
    insertbackground=FG,
    relief="flat"
)
entry4.pack(fill="x", ipady=5, pady=5)

frame = create_section("5. Який тип даних є змінюваним (mutable)?")

for value, text in [
    (1, "Кортеж (tuple)"),
    (2, "Рядок (str)"),
    (3, "Список (list)"),
    (4, "Ціле число (int)")
]:
    ttk.Radiobutton(
        frame,
        text=text,
        variable=q5,
        value=value,
        style="Custom.TRadiobutton"
    ).pack(anchor="w", pady=2)

frame = create_section("6. Які конструкції використовуються для створення циклів? (Декілька правильних)")

options = ["for", "while", "if", "def"]

for i, text in enumerate(options):
    ttk.Checkbutton(
        frame,
        text=text,
        variable=q6[i],
        style="Custom.TCheckbutton"
    ).pack(anchor="w", pady=2)

frame = create_section("7. Який оператор використовується для порівняння на рівність?")

tk.Label(
    frame,
    text="Введіть оператор:",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=FG
).pack(anchor="w")

entry7 = tk.Entry(
    frame,
    textvariable=q7,
    font=("Segoe UI", 11),
    bg=BG,
    fg=FG,
    insertbackground=FG,
    relief="flat"
)
entry7.pack(fill="x", ipady=5, pady=5)

frame = create_section("8. Яка структура даних зберігає інформацію у форматі ключ-значення?")

for value, text in [
    (1, "list"),
    (2, "tuple"),
    (3, "dict"),
    (4, "set")
]:
    ttk.Radiobutton(
        frame,
        text=text,
        variable=q8,
        value=value,
        style="Custom.TRadiobutton"
    ).pack(anchor="w", pady=2)

frame = create_section("9. Які з наведених модулів належать до стандартної бібліотеки Python? (Декілька правильних)")

options = ["math", "random", "Tkinter", "pygame"]

for i, text in enumerate(options):
    ttk.Checkbutton(
        frame,
        text=text,
        variable=q9[i],
        style="Custom.TCheckbutton"
    ).pack(anchor="w", pady=2)

frame = create_section('10. Який результат поверне вираз len("Python")?')

tk.Label(
    frame,
    text="Введіть число:",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=FG
).pack(anchor="w")

entry10 = tk.Entry(
    frame,
    textvariable=q10,
    font=("Segoe UI", 11),
    bg=BG,
    fg=FG,
    insertbackground=FG,
    relief="flat"
)
entry10.pack(fill="x", ipady=5, pady=5)

def calculate():
    surname = surname_entry.get().strip()
    group = group_entry.get().strip()

    if not surname or not group:
        warning.config(
            text="Заповніть прізвище та групу!"
        )
        canvas.yview_moveto(0)
        return

    warning.config(text="")

    score = 0

    if q1.get() == 1:
        score += 1

    if q2.get() == 2:
        score += 1

    if [v.get() for v in q3] == [True, True, True, False]:
        score += 1

    if q4.get().strip().lower() == "def":
        score += 1

    if q5.get() == 3:
        score += 1

    if [v.get() for v in q6] == [True, True, False, False]:
        score += 1

    if q7.get().strip() == "==":
        score += 1

    if q8.get() == 3:
        score += 1

    if [v.get() for v in q9] == [True, True, True, False]:
        score += 1

    if q10.get().strip() == "6":
        score += 1

    messagebox.showinfo(
        "Результат тесту",
        f"Користувач: {surname}\n"
        f"Група: {group}\n\n"
        f"Ваш результат: {score} / 10 балів\n"
        f"Правильних відповідей: {score}"
    )

def clear_answers():
    q1.set(0)
    q2.set(0)

    for variable in q3:
        variable.set(False)

    q4.set("")
    q5.set(0)

    for variable in q6:
        variable.set(False)

    q7.set("")
    q8.set(0)

    for variable in q9:
        variable.set(False)

    q10.set("")
    warning.config(text="")
    canvas.yview_moveto(0)

buttons = tk.Frame(content, bg=BG)
buttons.pack(fill="x", pady=15)

ttk.Button(
    buttons,
    text="Відправити результат",
    command=calculate,
    style="Custom.TButton"
).pack(fill="x", pady=5)

ttk.Button(
    buttons,
    text="Очистити відповіді",
    command=clear_answers,
    style="Custom.TButton"
).pack(fill="x", pady=5)

tk.Label(
    content,
    text="НАЗАРУК МАКСИМ | ЛАБОРАТОРНА 3.4",
    font=("Segoe UI", 9),
    bg=BG,
    fg=MUTED,
    pady=10
).pack()

root.mainloop()

