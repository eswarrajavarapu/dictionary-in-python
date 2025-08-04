from tkinter import *
root = Tk()
root.title('Calculator')
entry = Entry(root, width=35,borderwidth=5 )
entry.grid(row=0, column=0, columnspan=3,padx=10, pady=10)
def button_click(number):
    f_num=entry.get()
    entry.delete(0, END)
    entry.insert(0, str(f_num)+str(number))
def button_add():
    global first_num

    first_num=int(entry.get())
    entry.delete(0, END)
    global math

    math= "+"





def button_clear():
    entry.delete(0, END)
def button_equal():
    second_num=int(entry.get())
    entry.delete(0, END)
    if math=="+":
        result = first_num + second_num
        entry.insert(0, result)
    elif math == '*':
        result = first_num * second_num
        entry.insert(0, result)
    elif math == '/':
        result = int(first_num / second_num)
        entry.insert(0, result)
    elif math == '-':
        result = first_num - second_num
        entry.insert(0, result)





def button_mul():
    global first_num
    first_num = int(entry.get())
    entry.delete(0, END)
    global math
    math= '*'


def button_subtract():
    global first_num
    first_num = int(entry.get())
    entry.delete(0, END)
    global math
    math = '-'
def button_divide():
    global first_num
    first_num = int(entry.get())
    entry.delete(0, END)
    global math
    math = '/'
button1 = Button(root,padx=40,pady=20, text='1', command = lambda : button_click(1))
button2 = Button(root,padx=40,pady=20,text='2', command = lambda : button_click(2))
button3 = Button(root,padx=40,pady=20,text='3', command = lambda : button_click(3))
button4 = Button(root,padx=40,pady=20,text='4', command = lambda : button_click(4))
button5 = Button(root,padx=40,pady=20,text='5', command = lambda : button_click(5))
button6 = Button(root,padx=40,pady=20, text='6', command = lambda : button_click(6))
button7 = Button(root,padx=40,pady=20,text='7', command = lambda : button_click(7))
button8 = Button(root,padx=40,pady=20, text='8', command = lambda : button_click(8))
button9 = Button(root,padx=40,pady=20,text='9', command = lambda : button_click(9))
button0 = Button(root,padx=40,pady=20, text='0', command = lambda : button_click(0))
button_add = Button(root,padx=39,pady=20, text='+', command = button_add)
button_clear = Button(root,padx=79,pady=20, text='clear', command = button_clear)
button_equal = Button(root,padx=91,pady=20, text='=', command = button_equal)
button_subtract = Button(root,padx=40,pady=20,text='-', command = button_subtract)
button_mul = Button(root,padx=40,pady=20, text='*', command = button_mul)
button_divide = Button(root,padx=40,pady=20, text='/', command = button_divide)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button0.grid(row=3, column=2)
button9.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()