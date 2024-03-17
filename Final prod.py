import tkinter as tk
from tkinter import ttk

# Define a Task class to represent a task in the task manager
class Task:
    def __init__(self, title, theme=None):
        self.title = title
        self.theme = theme
        self.done = False

# Define a TaskManager class to manage tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, theme=None):
        self.tasks.append(Task(title, theme))

    def delete_task(self, index):
        del self.tasks[index]

    def filter_tasks(self, selected_theme):
        if selected_theme == "All":
            return self.tasks
        else:
            filtered_tasks = []
            for task in self.tasks:
                if task.theme == selected_theme:
                    filtered_tasks.append(task)
            return filtered_tasks

    def toggle_task_done(self, index):
        self.tasks[index].done = not self.tasks[index].done

# Function to add a task to the task manager
def add_task():
    task = entry_task.get()
    selected_theme_value = selected_theme.get()
    if task:
        task_manager.add_task(task, selected_theme_value)
        update_listbox()
        entry_task.delete(0, tk.END)

# Function to delete a task from the task manager
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task_manager.delete_task(task_index)
        update_listbox()
    except IndexError:
        pass

# Function to toggle the completion status of a task
def toggle_task_done(event):
    try:
        task_index = listbox_tasks.nearest(event.y)
        task_manager.toggle_task_done(task_index)
        update_listbox()
    except IndexError:
        pass

# Function to update the listbox with tasks
def update_listbox(tasks=None):
    listbox_tasks.delete(0, tk.END)
    tasks = tasks if tasks else task_manager.tasks
    for task in tasks:
        checkbox = "\u2611" if task.done else "\u2610"
        listbox_tasks.insert(tk.END, f"{checkbox} {task.title} - Theme: {task.theme}")

# Function to filter tasks based on selected theme
def filter_theme_tasks():
    selected_theme_value = selected_theme.get()
    filtered_tasks = task_manager.filter_tasks(selected_theme_value)
    update_listbox(filtered_tasks)

# Create the main Tkinter application window and icon
root = tk.Tk()
root.title("Optimize Your Day: The Ultimate Daily Task Manager")
root.configure(background="white")
root.option_add("*TButton*foreground", "black")
icon = tk.PhotoImage(file='imges/icon.png')
root.iconphoto(True, icon)

# Create an instance of TaskManager to manage tasks
task_manager = TaskManager()

# Create entry field for adding tasks
entry_task = tk.Entry(root, width=50, bg="white", fg="black", insertbackground="#0ADD08")
entry_task.grid(row=0, column=0, padx=(20, 5), pady=(20, 5), sticky="ew")

# Create listbox to display tasks
listbox_tasks = tk.Listbox(root, height=20, width=50, bg="white", fg="#0ADD08", selectbackground="#0ADD08", selectforeground="black")
listbox_tasks.grid(row=1, column=0, padx=(20, 5), pady=(0, 20), rowspan=2, sticky="nsew")

# Create scrollbar for the listbox
scrollbar_tasks = tk.Scrollbar(root, orient="vertical", command=listbox_tasks.yview)
scrollbar_tasks.grid(row=1, column=1, pady=(0, 20), sticky="ns")
listbox_tasks.configure(yscrollcommand=scrollbar_tasks.set)

# Define themes and set default theme
themes = ["All", "Personal", "Work", "Study", "Fitness"]
selected_theme = tk.StringVar(root)
selected_theme.set(themes[0])

# Create theme selection dropdown menu
theme_menu = ttk.OptionMenu(root, selected_theme, themes[0], *themes)
theme_menu.grid(row=0, column=1, padx=(0, 20), pady=(20, 5))

# Define style for buttons
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", foreground="black", background="#0ADD08", font=("Helvetica", 12), padding=10)

# Create buttons for adding, deleting, and filtering tasks
add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=(0, 20), pady=(20, 5), sticky="ew")

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=2, padx=(0, 20), pady=(0, 5), sticky="ew")

filter_button = ttk.Button(root, text="Filter Tasks", command=filter_theme_tasks)
filter_button.grid(row=2, column=2, padx=(0, 20), pady=(0, 20), sticky="ew")

# Bind task completion
listbox_tasks.bind("<Button-1>", toggle_task_done)

# Configure row and column weights
root.rowconfigure(1, weight=1)
root.columnconfigure((0, 1, 2), weight=1)

# Start the Tkinter event loop
root.mainloop()