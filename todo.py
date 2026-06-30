from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

title = Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title.pack(pady=10)

entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

add_btn = Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

listbox = Listbox(root, width=35, height=12, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()
