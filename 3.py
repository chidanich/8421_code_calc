def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def f(*args):
    n1 = num1.get()
    n2 = num2.get()
    tr1 = is_int(n1)
    tr2 = is_int(n2)
    if tr1 == FALSE or tr2 == FALSE:
        v.set("\nНЕВЕРНЫЙ ВВОД\nТОЛЬКО ЦЕЛЫЕ ЧИСЛА")
        return 0
    else:
        k = str((int(n1) % int(n2)) + 1)
        v.set('Вариант:' + k)
from tkinter import*
root=Tk()
root.title("Variant")
lae = Label(root, text= 'Номер в списке', font=('arial',14),  fg="darkblue")
lae.pack()
num1 = Entry(root, width=40, bd=8)
num1.pack()
num1.insert(1,'92')
lae = Label(root, text= 'Кол-во заданий', font=('arial',14),  fg="darkblue")
lae.pack()
num2 = Entry(root, width=40, bd=8)
num2.pack()
bt31 = Button(root,
text="Вариант", #надпись на кнопке
width=35, height=3, #ширина и высота
bg="green", fg="darkblue")
bt31.pack()
bt31.bind("<Button-1>",f)
v = StringVar()
lab = Label(root, textvariable = v, font=('arial',14),  fg="darkblue")
lab.pack()
root.mainloop()