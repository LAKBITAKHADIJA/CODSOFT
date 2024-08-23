from tkinter import *
from tkinter import ttk

class TodoApp:
    def __init__(self,root):
        self.root = root
        self.root.title( "TodoApp Manager")
        self.root.geometry("600x400")

        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        stats_menu = Menu (menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Statistics", menu=stats_menu)

        stats_menu.add_command(label="Total tasks",command=self.show_total_tasks)
        stats_menu.add_command(label="Completed tasks",command=self.show_completed_tasks)
        stats_menu.add_command(label="Pending tasks",command=self.show_pending_tasks)
        self.title_label = Label(self.root,text="ToDoApp",font=("Courier",20, "bold italic"))
        self.title_label.pack(pady=10)


        main_frame = Frame(self.root)
        main_frame.pack(pady=10, fill=BOTH, expand=True)

        left_frame = Frame(main_frame)
        left_frame.pack(side=LEFT, fill=Y, padx=10)

        self.prompt_label = Label(left_frame, text="Entry your task:", font=("Times New Roman",14,"bold"))
        self.prompt_label.pack(pady=(10,5), anchor= 'w')

        self.task_entry = Entry(left_frame, width=20, font=("Times New Roman",14, "bold"))
        self.task_entry.pack(pady=5, fill=X)

        button_frame = Frame(left_frame)
        button_frame.pack(side=BOTTOM, fill=Y, pady=10)

        button_width = 20

        self.add_button =Button(button_frame, text= "Add task", command=self.add_task, bg="lightgreen", font=("Times New Roman ", 14), width=button_width)
        self.add_button.pack(pady=5,fill=X)

        self.edit_button = Button(button_frame, text="Edit task", command=self.edit_task, bg="lightblue",font=("Times New Roman", 14), width=button_width)
        self.edit_button.pack(pady=5, fill=X)

        self.remove_button =Button(button_frame, text= "Delete task", command=self.remove_task, bg="salmon", font=("Times New Roman", 14), width=button_width)
        self.remove_button.pack(pady=5,fill=X)

        self.delete_all_button =Button(button_frame, text= "Delete all tasks", command=self.delete_all_tasks, bg="lightcoral", font=("Times New Roman", 14), width=button_width)
        self.delete_all_button.pack(pady=5,fill=X)

        self.exit_button =Button(button_frame, text= "Exit", command=self.exit_app, bg="lightgray", font=("Times New Roman ", 14), width=button_width)
        self.exit_button.pack(pady=5,fill=X)

        self.task_frame = Frame(main_frame, bg="beige")
        self.task_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
    

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'complete' : False})
            self.update_task_list()
            self.task_entry.delete(0,END)

    def edit_task(self):
        selected_task = None
        for task in self.tasks:
            if task['complete']: 
                selected_task = task
                break
        if selected_task:
            self.edit_windows = Toplevel(self.root)
            self.edit_windows.title("Edit Task")

            Label(self.edit_windows, Text="Edit your task:", font= ("Times New Roman",14,"bold")).pack(pady=10)

            self.edit_entry = Entry(self.edit_windows, width=30, font=("Times New Roman", 14))
            self.edit_entry.pack(pady=5)
            self.edit_entry.insert(0, selected_task['task'])

            Button(self.edit_windows, text="Save", command=lambda: self.save_task(selected_task)).pack(pady=10)






    def remove_task(self):
        self.tasks = [task for task in self.tasks if not task ['complete']]
        self.update_task_list()

    def delete_all_tasks(self):
        self.tasks = []
        self.update_task_list()

    def exit_app(self):
        self.root.quit()
        
    def update_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        
        for task in self.tasks:
            task_frame = Frame(self.task_frame,bg="beige")
            task_frame.pack(fill=X, pady=0)

            var=BooleanVar(value=task['complete'])
            font_style = ("Helvetica",18,"overstrike" if task['complete'] else "normal")

            check= Checkbutton(task_frame, variable=var , onvalue=True, offvalue=False, command=lambda v=var, t=task: self.update_task_status(v,t), bg="beige", activebackground="beige", highlightbackground="white", highlightcolor="white", selectcolor="white", width=6)
            check.pack(side=LEFT, padx=0)

            task_label= Label(task_frame, text=task['task'],font=font_style, bg="beige")
            task_label.pack(side=LEFT,padx=0, fill=X,expand=True)

    def update_task_status(self, var, task):

        task['complete'] = var.get()
        self.update_task_list()

    def show_total_tasks(self):
        total_tasks = len(self.tasks)
        self.show_message(f"Total tasks : {total_tasks}")


    def show_completed_tasks(self): 
        completed_tasks = len([task for task in self.tasks if task['complete']])
        self.show_message(f" Completed tasks: {completed_tasks}")


    def show_pending_tasks(self):
        pending_tasks = len([task for task in self.tasks if task['complete']])
        self.show_message(f" Pending tasks: {pending_tasks}")


    def show_message(self, message):
        top = Toplevel(self.root)
        top.title("Statistics")
        Label(top, text=message, font=("Halvetica",20)).pack(pady=20)
        Button(top, text="OK",command=top.destroy, font=("Arial,20")).pack(pady=10)

def main():
        root = Tk()
        app = TodoApp(root)
        root.mainloop()

if __name__ == "__main__":
    main()




    

        








        
    



