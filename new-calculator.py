from tkinter import Tk, Entry, Button, StringVar

class NewCalculator:
    def __init__(self, master):
        # Configure the root window
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        # Create a StringVar to hold the equation
        self.equation = StringVar()
        self.entry_value = ''
        
        # Create an Entry widget to display the equation
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Create buttons for each digit and operation
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show('(')).place(x=0 ,y=50)
        # Other buttons omitted for brevity...

    def show(self, value):
        # Update the entry_value and equation with the pressed button
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        # Clear the entry_value and equation
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        # Evaluate the expression and update the equation with the result
        result = eval(self.entry_value)
        self.equation.set(result)

# Create the root window and NewCalculator instance
root = Tk()
NewCalculator = NewCalculator(root)
root.mainloop()
