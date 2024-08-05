import tkinter as tk

class ToDoList:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List")

        # Create task list
        self.task_list = tk.Listbox(self.window, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        # Create entry field for new tasks
        self.entry_field = tk.Entry(self.window, width=40)
        self.entry_field.pack(padx=10, pady=10)

        # Create buttons
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.edit_button = tk.Button(self.window, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.entry_field.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.entry_field.delete(0, tk.END)

    def edit_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task = self.task_list.get(selected_task)
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, task)
            self.task_list.delete(selected_task)

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()