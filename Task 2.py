from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.config(bg="#2C3E50")

        self.expression = ""

        self.entry = Entry(self.root, font= ("Arial",20), borderwidth=5, relief=SUNKEN, justify=RIGHT, bg="#1C1C1C", fg="#FFFFFF")

        self.entry.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('(',1,0),(')',1,1),('%',1,2),('AC',1,3),
            ('1',2,0),('2',2,1),('3',2,2),('+',2,3),
            ('4',3,0),('5',3,1),('6',3,2),('-',3,3),
            ('7',4,0),('8',4,1),('9',4,2),('/',4,3),
            ('0',5,0),('.',5,1),('x',5,2),('=',5,3)
        ]
        button_color = "#2E86C1"
        button_text_color = "#FFFFFF"
        button_active_color = "#21618C"
        button_ac_color = "#E74C3C"

        for (text, row, col) in buttons:
            if text== 'AC':
                button = Button(self.root, text=text, font=("Arial",18),bg=button_ac_color, fg=button_text_color, activebackground=button_active_color, relief=RAISED, bd=2, command=lambda t=text: self.on_button_click(t))
            else :
                button = Button(self.root, text=text, font=("Arial",18),bg=button_color, fg=button_text_color, activebackground=button_active_color, relief=RAISED, bd=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'AC':
            self.expression = ""

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
            
        else:

            self.expression += str(char)
            
        self.entry.delete(0, END)
        self.entry.insert(END, self.expression)



def main():
    root = Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

