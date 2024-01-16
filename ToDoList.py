import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class ToDoList:
    def __init__(self, app):
        self.app = app
        app.title("To-Do List")
        app.geometry("550x500") 
        app.configure(bg='#6820B0')

        # Adding the header for the GUI
        self.header = tk.Label(app, text="Alex's Weekly To-Do List", bg='skyblue', fg='white', font=("Times New Roman", 16))
        self.header.pack(pady=10)

        # Adding the frames for the input, date entry, and add button
        self.frame_add = tk.Frame(app, bg='black')
        self.frame_add.pack(pady=10)

        # Entry for adding new tasks
        self.task_entry = tk.Entry(self.frame_add, width=25, font=("Times New Roman", 12))  # Adjusted width for task entry
        self.task_entry.pack(side=tk.LEFT, padx=5)

        # Date entry for selecting due dates
        self.due_date_entry = DateEntry(self.frame_add, width=12, background='sky blue', foreground='white', borderwidth=2, date_pattern='mm-dd-yy')
        self.due_date_entry.pack(side=tk.LEFT, padx=5)

        # Button for adding task
        self.add_button = tk.Button(self.frame_add, text="Add Task", command=self.addTask, bg='grey', fg='#FFFDD0', font=("Times New Roman", 12))
        self.add_button.pack(side=tk.LEFT)

        # Displaying the list of tasks
        self.listbox = tk.Listbox(app, width=65, height=10, bg='white', fg='black', font=("Times New Roman", 12))  # Adjusted width for listbox
        self.listbox.pack(pady=10)

        # Done and delete button frames
        self.frame_actions = tk.Frame(app, bg='#6820B0')
        self.frame_actions.pack(pady=10)

        # Button to mark task as complete
        self.done_button = tk.Button(self.frame_actions, text="Mark as Done", command=self.mark, bg='grey', fg='#FFFDD0', font=("Times New Roman", 12))
        self.done_button.pack(side=tk.LEFT, padx=5)

        # Button to delete task
        self.delete_button = tk.Button(self.frame_actions, text="Delete Task", command=self.delete_task, bg='grey', fg='#FFFDD0', font=("Times New Roman", 12))
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Button to exit
        self.exit_button = tk.Button(app, text="Exit List", command=app.quit, bg='grey', fg='#FFFDD0', font=("Times New Roman", 12))
        self.exit_button.pack(pady=5)

        # Storing the task
        self.tasks = []

    def addTask(self):
        task = self.task_entry.get()
        due_date = self.due_date_entry.get()
        if task != "":
            self.tasks.append({'task': task, 'due_date': due_date})
            display_text = f"{task} - Due: {due_date}"
            self.listbox.insert(tk.END, display_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def mark(self):
        try:
            task_index = self.listbox.curselection()[0]
            task = self.tasks[task_index]['task']
            due_date = self.tasks[task_index]['due_date']
            # Updating the task in the listbox and tasks list
            self.listbox.delete(task_index)
            self.listbox.insert(task_index, f"{task} - Due: {due_date} (Done)")
            self.tasks[task_index]['task'] = task + " (Done)"
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        # Function to delete a task
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

app = tk.Tk()
application = ToDoList(app)

app.mainloop()