import tkinter as tk

root = tk.Tk()
root.title("Налаштування")
root.geometry("300x300")
root.configure(bg="orange")

icon = tk.PhotoImage(width=32, height=32)
icon.put("#ff3333", to=(4, 4, 28, 28))
root.iconphoto(True, icon)


def help(event):
    root.configure(bg="purple")
    root.title("Допомога")
    print("Допомога відкрито!")


def mouse_move(event):
    root.configure(bg="red")
    root.title("Видалено")
    root.geometry("300x280")


root.bind("<F1>", help)
root.bind("<Motion>", mouse_move)

root.mainloop()
