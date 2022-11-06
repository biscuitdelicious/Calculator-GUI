from tkinter import *

root = Tk()
root.configure(bg='#EFE6DD')
root.title('Simple Calculator')
root.geometry('380x600')


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
        button = Button(root, text=self.text, padx=self.padx, pady=self.pady, borderwidth=0, command=lambda: button_click(self.text))
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


num_input = Entry(root, bg='#F3FFC6', fg='#231F20', font=('Avenir', 18), borderwidth=2)
num_input.grid(columnspan=3, row=0, pady=5)

button0 = Buttton('0', 0, 1)
button0.create_button()

button_plus = Button(root, text='+', padx=35, pady=30, borderwidth=0, command=button_add)
button_plus.configure(font=('Avenir', 20, 'bold'))
button_plus.grid(column=1, row=1)

button_equal = Button(root, text='=', padx=35, pady=30, borderwidth=0, command=button_equal)
button_equal.configure(font=('Avenir', 20, 'bold'))
button_equal.grid(column=2, row=1)

button_clear = Button(root, text='Clear', padx=140, pady=4, borderwidth=0, command=clear_button)
button_clear.configure(font=('Avenir', 14, 'bold'))
button_clear.grid(row=6, column=0, columnspan=3)


button1 = Buttton('1', 0, 3)
button1.create_button()

button2 = Buttton('2', 1, 3)
button2.create_button()

button3 = Buttton('3', 2, 3)
button3.create_button()

button4 = Buttton('4', 0, 4)
button4.create_button()

button5 = Buttton('5', 1, 4)
button5.create_button()

button6 = Buttton('6', 2, 4)
button6.create_button()

button7 = Buttton('7', 0, 5)
button7.create_button()

button8 = Buttton('8', 1, 5)
button8.create_button()

button9 = Buttton('9', 2, 5)
button9.create_button()

button_subtract = Button(root, text='-', padx=35, pady=30, borderwidth=0, command=button_subtract)
button_subtract.configure(font=('Avenir', 20, 'bold'))
button_subtract.grid(column=0, row=2, pady=5, padx=4)

button_multiply = Button(root, text='*', padx=35, pady=30, borderwidth=0, command=button_multiply)
button_multiply.configure(font=('Avenir', 20, 'bold'))
button_multiply.grid(column=1, row=2, pady=5, padx=4)

button_divide = Button(root, text='/', padx=35, pady=30, borderwidth=0, command=button_divide)
button_divide.configure(font=('Avenir', 20, 'bold'))
button_divide.grid(column=2, row=2, pady=5, padx=4)

root.mainloop()
