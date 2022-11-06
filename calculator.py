import tkinter
from tkinter import *

root = Tk()
root.configure(bg='#EFE6DD')
root.title('Simple Calculator')
ROOT_SIZE = '380x800'
root.geometry(ROOT_SIZE)


class Buttton(tkinter.Button):
    def __init__(self, button_text, columnn, roww):
        super().__init__()
        self.text = button_text
        self.column = columnn
        self.row = roww
        self.pady = 30
        self.padx = 35
        self.font = ('Avenir', 20, 'bold')

    def create_button(self):
        button = Button(root, text=self.text, padx=self.padx, pady=self.pady, borderwidth=0,
                        command=lambda: button_click(self.text), highlightbackground='#005E7C', highlightthickness=3)
        button.configure(font=self.font)
        button.grid(column=self.column, row=self.row, padx=4, pady=5)


def button_click(number):
    current = num_input.get()
    num_input.delete(0, END)
    num_input.insert(0, current + number)


def clear_button():
    num_input.delete(0, END)


def button_add():
    f_number = num_input.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(f_number)
    num_input.delete(0, END)


def button_equal():
    second_num = num_input.get()
    num_input.delete(0, END)
    if math == 'addition':
        num_input.insert(0, f_num + int(second_num))
    if math == 'subtract':
        num_input.insert(0, f_num - int(second_num))
    if math == 'multiply':
        num_input.insert(0, f_num * int(second_num))
    if math == 'divide':
        num_input.insert(0, f_num / int(second_num))
    if math == 'pow':
        num_input.insert(0, f_num ** int(second_num))


def button_subtract():
    f_number = num_input.get()
    global f_num
    global math
    math = 'subtract'
    f_num = int(f_number)
    num_input.delete(0, END)


def button_multiply():
    f_number = num_input.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(f_number)
    num_input.delete(0, END)


def button_divide():
    f_number = num_input.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(f_number)
    num_input.delete(0, END)


def button_pow():
    f_number = num_input.get()
    global f_num
    global math
    math = 'pow'
    f_num = int(f_number)
    num_input.delete(0, END)


num_input = Entry(root, bg='#F3FFC6', fg='#231F20', font=('Avenir', 18), borderwidth=2)
num_input.grid(columnspan=3, row=0, pady=5)

button0 = Button(root, text='0', padx=120, pady=30, borderwidth=0, command=lambda: button_click('0'), highlightthickness=2, highlightbackground='#005E7C')
button0.grid(columnspan=3, row=4, pady=5, padx=4)
button0.configure(font=('Avenir', 20, 'bold'))

button1 = Buttton('1', 0, 5)
button1.create_button()

button2 = Buttton('2', 1, 5)
button2.create_button()

button3 = Buttton('3', 2, 5)
button3.create_button()

button4 = Buttton('4', 0, 6)
button4.create_button()

button5 = Buttton('5', 1, 6)
button5.create_button()

button6 = Buttton('6', 2, 6)
button6.create_button()

button7 = Buttton('7', 0, 7)
button7.create_button()

button8 = Buttton('8', 1, 7)
button8.create_button()

button9 = Buttton('9', 2, 7)
button9.create_button()

SPECIAL_BUTTONS_COLOR = '#FE5F55'

button_plus = Button(root, text='+', padx=35, pady=30, borderwidth=0, command=button_add, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Plus button
button_plus.configure(font=('Avenir', 20, 'bold'))
button_plus.grid(column=1, row=1)

button_equal = Button(root, text='=', padx=35, pady=30, borderwidth=0, command=button_equal, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Equal button
button_equal.configure(font=('Avenir', 20, 'bold'))
button_equal.grid(column=2, row=1)

button_clear = Button(root, text='Clear', padx=140, pady=4, borderwidth=0, command=clear_button, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Clear button
button_clear.configure(font=('Avenir', 14, 'bold'))
button_clear.grid(row=10, column=0, columnspan=3)

button_subtract = Button(root, text='-', padx=35, pady=30, borderwidth=0, command=button_subtract, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Substract button
button_subtract.configure(font=('Avenir', 20, 'bold'))
button_subtract.grid(column=0, row=2, pady=5, padx=4)

button_multiply = Button(root, text='*', padx=35, pady=30, borderwidth=0, command=button_multiply, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Multiply button
button_multiply.configure(font=('Avenir', 20, 'bold'))
button_multiply.grid(column=1, row=2, pady=5, padx=4)

button_divide = Button(root, text='/', padx=35, pady=30, borderwidth=0, command=button_divide, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Divide button
button_divide.configure(font=('Avenir', 20, 'bold'))
button_divide.grid(column=2, row=2, pady=5, padx=4)

button_pow = Button(root, text='x^y', padx=30, pady=30, borderwidth=0, command=button_pow, highlightbackground=SPECIAL_BUTTONS_COLOR, highlightthickness=2)  # Divide button
button_pow.configure(font=('Avenir', 19, 'bold'))
button_pow.grid(column=0, row=1, pady=5, padx=4)

root.mainloop()
