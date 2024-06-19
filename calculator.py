import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.expression = ""
        self.text_input = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Entry box
        entry = tk.Entry(self.root, textvariable=self.text_input, font=('arial', 20, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.text_input.set(self.expression)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero is not allowed")
                self.expression = ""
                self.text_input.set("")
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
                self.text_input.set("")
        elif char == '√':
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.text_input.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
                self.text_input.set("")
        elif char == '^':
            self.expression += '**'
            self.text_input.set(self.expression)
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
