# python program to create a simple calculator
# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:

        equation.set(" error ")
        expression = ""

# Function to clear the entry


def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    window = Tk()

    # set the background colour of GUI window
    window.configure(background="maroon")

    # set the title of GUI window
    window.title("Simple Calculator")

    # set the configuration of GUI window
    window.geometry("265x125")

    # create an instance of variable class
    equation = StringVar()

    # create an entry box
    expression_field = Entry(window, textvariable=equation)

    # display it at a particular position in table
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('Enter the expression')

    # create Buttons and place them at a particular position which when clicked, function affiliated to them is executed
    button1 = Button(window, text=' 1 ', fg='black', bg='pink', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(window, text=' 2 ', fg='black', bg='pink', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(window, text=' 3 ', fg='black', bg='pink', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(window, text=' 4 ', fg='black', bg='pink', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(window, text=' 5 ', fg='black', bg='pink', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(window, text=' 6 ', fg='black', bg='pink', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(window, text=' 7 ', fg='black', bg='pink', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(window, text=' 8 ', fg='black', bg='pink', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(window, text=' 9 ', fg='black', bg='pink', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(window, text=' 0 ', fg='black', bg='pink', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(window, text=' + ', fg='black', bg='pink', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(window, text=' - ', fg='black', bg='pink', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(window, text=' * ', fg='black', bg='pink', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(window, text=' / ', fg='black', bg='pink', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(window, text=' = ', fg='black', bg='pink', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(window, text='Clear', fg='black', bg='pink', command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    # display the window
    window.mainloop()