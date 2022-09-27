#ask user what items to place on their to-do list
#append items to list
#dispay items
#if done, mark them as done and display remaining items on list

import tkinter
from tkinter import Label, StringVar, filedialog
from tkinter.font import Font
import pickle
from datetime import datetime


""" def time_now():
    string = time.strftime(f'%H:%M:%S %p')
    display_time.config(text=string)
    display_time.after(1000, time_now) """

root = tkinter.Tk()
root.title("To-Do List")
root.geometry("500x500")

my_menu = tkinter.Menu(root)
root.config(menu=my_menu)

def save_list():
    items = task_list.get(0, tkinter.END)
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Udacity/python/data",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"),
                    ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

    output_file = open(file_name, 'wb')
    pickle.dump(items, output_file)



def open_list():
    file_name = filedialog.askopenfilename(
            initialdir="C:/Udacity/python/data",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"),
                    ("All Files", "*.*"))
    )

    if file_name:
        task_list.delete(0, tkinter.END)
        input_file = open(file_name, 'rb')
        tasks = pickle.load(input_file)
        for item in tasks:
            task_list.insert(tkinter.END, item)

    

def delete_crossed():
    count = 0
    while count < task_list.size():
        if task_list.itemcget(count, "fg") == "#dedede":
            task_list.delete(task_list.index(count))
        else:
            count += 1
        

def clear_list():
    task_list.delete(0, tkinter.END)

def change_color():
    task_list.config(bg=radio.get())
    

file_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Delete Crossed Items", command=delete_crossed)
file_menu.add_command(label="Clear List", command=clear_list)
file_menu.add_command(label="Exit", command=root.quit)

radio = StringVar()
radio.set("#FEFFCC")

color_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_radiobutton(label="white", background="white", variable=radio, value="white", command=change_color)
color_menu.add_radiobutton(label="yellow", state="active", background="#FEFFCC", variable=radio, value="#FEFFCC", command=change_color)
color_menu.add_radiobutton(label="pink", background="#FFE5F0",variable=radio, value="#FFE5F0", command=change_color)
color_menu.add_radiobutton(label="mint", background="#EBFFF6", variable=radio, value="#EBFFF6", command=change_color)
color_menu.add_radiobutton(label="purple", background="#E9D3FF", variable=radio, value="#E9D3FF", command=change_color)

my_font = Font(
    family="Lucida Calligraphy italic",
    size=28,
    weight="bold"
)

date_frame = tkinter.Frame(root)
date_frame.pack()

today = datetime.now()
date = Label(date_frame, text=f'{today:%A, %B %d, %Y}', font="Arial, 11", fg="#A9A9A9")
date.pack()
    

my_frame = tkinter.Frame(root)
my_frame.pack()

task_list = tkinter.Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="#FEFFCC",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#C2E5D3",
    activestyle="none"
)
task_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

my_scrollbar = tkinter.Scrollbar(my_frame)
my_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

task_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=task_list.yview)

def add_task():
    task = my_entry.get()
    if len(task) > 0:
        task_list.insert(tkinter.END, task)
    my_entry.delete(0, tkinter.END)

def task_done():
    task_list.itemconfig(task_list.curselection(), fg="#dedede")
    task_list.selection_clear(0, tkinter.END)

def delete_task():
    task_list.delete(tkinter.ANCHOR)

def uncross():
    task_list.itemconfig(task_list.curselection(), fg="#464646")
    task_list.selection_clear(0, tkinter.END)

my_entry = tkinter.Entry(root, font="Helvetica, 20", width=26)
my_entry.pack(pady=20)

button_frame = tkinter.Frame(root)
button_frame.pack(pady=20)

add = tkinter.Button(button_frame, text="Add", padx=20, pady=5, command=add_task).grid(row=0, column=0)
cross_off = tkinter.Button(button_frame, text="Cross Off Item", padx=20, pady=5, command=task_done).grid(row=0, column=2)
uncross_off = tkinter.Button(button_frame, text="Uncross Item", padx=20, pady=5, command=uncross).grid(row=0, column=3, pady=10)
delete = tkinter.Button(button_frame, text="Delete", padx=20, pady=5, command=delete_task).grid(row=0, column=1, pady=10)

#today = tkinter.Label(root, text=f"{date:%A, %B %d, %Y}", font="Calibri, 15", justify='center')
#today.grid(row=0, pady=10, columnspan=2)

root.mainloop()
