import tkinter as tk

root = tk.Tk()
root.title("Назарук, лабораторна 3.1, завдання 1")
root.geometry("400x300")
root.configure(bg="white")

icon = tk.PhotoImage(width=32, height=32)
icon.put("#ff3333", to=(4, 4, 28, 28))
root.iconphoto(True, icon)

button = tk.Button(
    root,
    text="Центр",
    bg="green",
    fg="white"
)

button.pack(
    expand=True,
    padx=10,
    pady=10
)

root.mainloop()
