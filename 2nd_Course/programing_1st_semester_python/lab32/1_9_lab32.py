import tkinter as tk

root = tk.Tk()
root.title("Назарук, лабораторна 3.2, завдання 1")
root.geometry("400x300")
root.configure(bg="white")

icon = tk.PhotoImage(width=32, height=32)
icon.put("#ff3333", to=(4, 4, 28, 28))
root.iconphoto(True, icon)

def change_text():
    button1.config(text="Зміна!")

def reset_text():
    button1.config(text="Зміни текст на Зміна!")

button1 = tk.Button(
    root,
    text="Зміни текст на Зміна!",
    bg="green",
    fg="white",
    command=change_text
)

button2 = tk.Button(
    root,
    text="Повернути текст",
    bg="red",
    fg="white",
    command=reset_text
)

button1.pack(pady=20)
button2.pack(pady=10)

root.mainloop()
