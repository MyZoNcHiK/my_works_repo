import tkinter as tk

root = tk.Tk()
root.title("Назарук, лабораторна 3.1, завдання 3")
root.geometry("400x300")
root.configure(bg="white")

icon = tk.PhotoImage(width=32, height=32)
icon.put("#ff3333", to=(4, 4, 28, 28))
root.iconphoto(True, icon)

for i in range(4):
    root.columnconfigure(i, weight=1)

button = tk.Button(
    root,
    text="Ширина 50%",
    bg="red",
    fg="white"
)

button.grid(
    row=1,
    column=1,
    columnspan=2,
    sticky="ew"
)

root.mainloop()
