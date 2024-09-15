 #task number 1

"""A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing

users to create, update, and track their to-do lists"""


import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aryan Yadav's To-Do List 😊")
        self.root.geometry("600x600")
        self.root.config(bg='yellow')

        # Greeting label
        self.greeting_label = tk.Label(self.root, text="Aryan Yadav's To-Do List 😊", font=("Helvetica", 16, 'bold'), bg='yellow', fg='black')
        self.greeting_label.pack(pady=10)

        # Frame for the To-Do list
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, height=10, width=50, font=('Helvetica', 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry box for new tasks
        self.task_entry = tk.Entry(self.root, font=('Helvetica', 12), width=40)
        self.task_entry.pack(pady=10)

        # Priority dropdown menu
        self.priority_var = tk.StringVar(value="Low")
        self.priority_menu = tk.OptionMenu(self.root, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.config(width=15)
        self.priority_menu.pack(pady=5)

        # Date picker for due date
        self.due_date = DateEntry(self.root, width=15, background='darkblue', foreground='white', borderwidth=2)
        self.due_date.pack(pady=5)

        # Buttons with different colors and 3D effect
        self.add_task_button = tk.Button(self.root, text="Add Task", width=15, bg='yellow', relief=tk.RAISED, command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", width=15, bg='blue', relief=tk.RAISED, command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", width=15, bg='purple', relief=tk.RAISED, command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.mark_complete_button = tk.Button(self.root, text="Mark as Complete", width=15, bg='green', relief=tk.RAISED, command=self.mark_complete)
        self.mark_complete_button.pack(pady=5)

        self.sort_task_button = tk.Button(self.root, text="Sort by Priority", width=15, bg='pink', relief=tk.RAISED, command=self.sort_tasks)
        self.sort_task_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Task", width=15, bg='red', relief=tk.RAISED, command=self.search_task)
        self.search_button.pack(pady=5)

        # Search bar for finding tasks
        self.search_entry = tk.Entry(self.root, font=('Helvetica', 12), width=40)
        self.search_entry.pack(pady=10)

        # To store tasks with additional details
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date.get()
        if task != "":
            task_detail = f"{task} | Priority: {priority} | Due: {due_date}"
            self.tasks.append((task, priority, due_date, "Incomplete"))
            self.task_listbox.insert(tk.END, task_detail)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            updated_priority = self.priority_var.get()
            updated_due_date = self.due_date.get()
            if updated_task != "":
                task_detail = f"{updated_task} | Priority: {updated_priority} | Due: {updated_due_date}"
                self.tasks[selected_task_index] = (updated_task, updated_priority, updated_due_date, "Incomplete")
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, task_detail)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty!")
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected!")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected!")

    def mark_complete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task, priority, due_date, _ = self.tasks[selected_task_index]
            completed_task = f"{task} | Priority: {priority} | Due: {due_date} - Completed"
            self.tasks[selected_task_index] = (task, priority, due_date, "Completed")
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected!")

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: {"Low": 3, "Medium": 2, "High": 1}[x[1]])
        self.task_listbox.delete(0, tk.END)
        for task, priority, due_date, status in self.tasks:
            task_detail = f"{task} | Priority: {priority} | Due: {due_date} - {status}"
            self.task_listbox.insert(tk.END, task_detail)

    def search_task(self):
        search_query = self.search_entry.get().lower()
        matching_tasks = [f"{task} | Priority: {priority} | Due: {due_date} - {status}" 
                          for task, priority, due_date, status in self.tasks if search_query in task.lower()]
        self.task_listbox.delete(0, tk.END)
        for task_detail in matching_tasks:
            self.task_listbox.insert(tk.END, task_detail)

# Main loop to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


