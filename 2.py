# Функция "transl_into_8421" перевода чисел в код 8-4-2-1
# Передается "dec_num" - вводимое десятичное число
# Возвращает "num_8421" - число в коде 8-4-2-1


def transl_into_8421(dec_num):
    dec_num = str(dec_num)
    minus = dec_num.find('-')
    dec_num = dec_num.replace('-', '')

    num_8421 = " ".join(["0" * (4 - len(str(bin(int(i))[2:]))) + str(bin(int(i))[2:]) for i in str(dec_num)])

    if minus != -1:
        num_8421 = "-" + num_8421
    return num_8421


# Функция "transl_into_dec" перевода чисел в десятичный код
# Передается "num8421" - вводимое 8-4-2-1 число
# Возвращает "decnum" - число в десятичном коде

def transl_into_dec(num8421):
    num8421 = num8421.replace(' ', '')
    minus = num8421.find('-')
    num8421 = num8421.replace('-', '')
    if len(num8421) % 4 == 1:
        num8421 = '0'*3 + num8421
    if len(num8421) % 4 == 2:
        num8421 = '0'*2 + num8421
    if len(num8421) % 4 == 3:
        num8421 = '0' + num8421
    for i in range(0, len(num8421), 4):
        a=str(int(num8421[i])*2**3 + int(num8421[i+1])*2**2 + int(num8421[i+2])*2 + int(num8421[i+3]))
        if int(a) >=10 :
            flag=0
            decnum ="Запрещенная комбинация"
            return decnum, flag

    flag=1
    decnum = "".join([str(int(num8421[i])*2**3 + int(num8421[i+1])*2**2 + int(num8421[i+2])*2 + int(num8421[i+3])) for i in range(0, len(num8421), 4)])
    if minus != -1:
        decnum = "-" + decnum

    return decnum,flag

#Безопасный ввод
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Безопасный ввод8421
def is_8421(s):
    try:
        int(s,2)
        return True
    except ValueError:
        return False

# Графическая оболочка

def n8421(*args):

    dec_num = num.get()
    dec_num = dec_num.replace('+', '')
    tr = is_int(dec_num)
    slist1 = []
    slist2 = []
    if tr == FALSE:

        var.set("\nНЕВЕРНЫЙ ВВОД\nТОЛЬКО ЦЕЛЫЕ ЧИСЛА")
        return 0
    else:
        num8421 = transl_into_8421(dec_num)
        var.set('\nРешение:' + '\n' + dec_num + ' = ' + num8421 )
        num8421 = num8421.replace(' ', '')
        for i in range(0, int(len(num8421)), 4):
            slist2.insert(i, str(num8421[i]) + str(num8421[i + 1]) + str(num8421[i + 2]) + str(num8421[i + 3]))
        for i in range(0, int(len(str(dec_num)))):
            slist1.insert(i, str(dec_num[i]) )
        for l23 in fra7.grid_slaves():
           l23.grid_forget()
        for i,j in enumerate(slist1):
            l23 = Label(fra7,text='%s' % (j), relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',14))
            l23.grid(row=0, column=i, sticky=NSEW)
        for i,j in enumerate(slist2):
            l23 = Label(fra7,text='%s' % (j), relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',14))
            l23.grid(row=1, column=i, sticky=NSEW)
        return num8421

def ndec(*args):
    slist1 = []
    slist2 = []
    num8421 = numd.get()
    num8421 = num8421.replace('+', '')
    tr = is_int(num8421)
    tr1 = is_8421(num8421)
    if tr == FALSE or tr1 == FALSE:

        va.set("\nНЕВЕРНЫЙ ВВОД\nТОЛЬКО ЦЕЛЫЕ ЧИСЛА В КОДЕ 8421\nДОПУСТИМЫ ТОЛЬКО 0 И 1")
        return 0
    else:
        minus = num8421.find('-')
        num8421 = num8421.replace('-', '')
        if len(num8421) % 4 == 1:
            num8421 = '0'*3 + num8421
        if len(num8421) % 4 == 2:
            num8421 = '0'*2 + num8421
        if len(num8421) % 4 == 3:
            num8421 = '0' + num8421
        if minus != -1:
            num8421='-'+num8421
        num842, flag = transl_into_dec(num8421)
        if flag == 0:

            va.set(num842)
        else:
            va.set('\nРешение:' + '\n' + num8421 + ' = ' + num842)

            minus = num8421.find('-')
            num8421 = num8421.replace('-', '')
            num842 = num842.replace('-', '')
            for i in range(0, int(len(num8421)), 4):
                slist1.insert(i, str(num8421[i]) + str(num8421[i + 1]) + str(num8421[i + 2]) + str(num8421[i + 3]))
            for i in range(0, int(len(str(num842)))):
                slist2.insert(i, str(num842[i]))
            for l23 in fra8.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist1):
                l23 = Label(fra8, text='%s' % (j), relief=RIDGE, bg='#FAFF8D', fg="darkblue", font=('arial', 14))
                l23.grid(row=0, column=i, sticky=NSEW)
            for i, j in enumerate(slist2):
                l23 = Label(fra8, text='%s' % (j), relief=RIDGE, bg='#FAFF8D', fg="darkblue", font=('arial', 14))
                l23.grid(row=1, column=i, sticky=NSEW)
        return num842


def nsum(*args):
    nm1 = num1.get()
    nm2 = num2.get()
    nm1 = nm1.replace(' ', '')
    nm2 = nm2.replace(' ', '')
    minus1 = nm1.find('-')
    minus2 = nm2.find('-')
    nm1 = nm1.replace('-', '')
    nm2 = nm2.replace('-', '')
    tr = is_int(nm1)
    tr1 = is_8421(nm1)
    if tr == FALSE or tr1 == FALSE:
        num1.delete(0, END)
        num1.insert(1,"НЕВЕРНЫЙ ВВОД /ТОЛЬКО ЦЕЛЫЕ ЧИСЛА В КОДЕ 8421 /ДОПУСТИМЫ ТОЛЬКО 0 И 1")
        return 0
    tr111 = is_int(nm2)
    tr11 = is_8421(nm2)
    if tr111 == FALSE or tr11 == FALSE:
        num2.delete(0, END)
        num2.insert(2, "НЕВЕРНЫЙ ВВОД /ТОЛЬКО ЦЕЛЫЕ ЧИСЛА В КОДЕ 8421 /ДОПУСТИМЫ ТОЛЬКО 0 И 1")
        return 0

    if len(nm1) % 4 == 1:
        nm1 = '0'*3 + nm1
    if len(nm1) % 4 == 2:
        nm1 = '0'*2 + nm1
    if len(nm1) % 4 == 3:
        nm1 = '0' + nm1
    if len(nm2) % 4 == 1:
        nm2 = '0'*3 + nm2
    if len(nm2) % 4 == 2:
        nm2 = '0'*2 + nm2
    if len(nm2) % 4 == 3:
        nm2 = '0' + nm2
    if len(nm1) != len(nm2):
        if len(nm1) > len(nm2):
            nm2 = '0'*(len(nm1)-len(nm2)) + nm2
        elif len(nm2)>len(nm1):
            nm1 = '0'*(len(nm2)-len(nm1)) + nm1
    slist1 = []
    slist14 = []
    slist2 = []
    slist3 = []
    slist41 =[]
    slist46 = []
    slist51 = []
    slist56 = []
    for i in range(0,int(len(nm1)),4):
        slist1.insert(i, str(nm1[i])+str(nm1[i+1])+str(nm1[i+2])+str(nm1[i+3]))
        slist2.insert(i, str(nm2[i])+str(nm2[i+1])+str(nm2[i+2])+str(nm2[i+3]))
    flag = 0
    if minus1 == -1 and minus2 == -1:
        for i in range(int(len(slist1))-1,-1,-1):
            tk1 = str(int(slist1[i],2) + int(slist2[i],2))
            if flag == 1:
                tk1 = str(int(tk1)+1)
                slist41.insert(i, '+1')
                slist51.insert(i, '0001')
            else:
                slist41.insert(i, '   ')
                slist51.insert(i, '   ')
            if int(tk1) > 15:
                flag = 1  # перенос в старшую тетраду
            elif int(tk1) <= 15:
                flag = 0

            if int(tk1) >= 10:  # получение запрещенной комбинации
                tk1 = str(int(tk1)+6)
                slist46.insert(i, '+6')
                slist56.insert(i, '0110')
            else:
                slist46.insert(i, '    ')
                slist56.insert(i, '    ')
            if int(tk1) > 15:
                flag = 1
            tk1 = str(bin(int(tk1)))[2:]
            tk1 = '0'*(4-len(tk1)) + tk1
            tk1 = tk1[-4:]
            slist3.insert(i, tk1)
            if i == 0 and flag == 1:

                slist3.insert(0, '0001')

                slist1.insert(0, '')
                slist2.insert(0, '')
                slist41.insert(0, '+1')
                slist51.insert(0, '0001')
                slist46.insert(0, '')
                slist56.insert(0, '')

        n1 = n2 = sym = cor = cor1 = peren = peren1 = ''

        for i in range(0,len(slist3)):
            n1 = n1 + ' ' + slist1[i]
            n2 = n2 + ' ' + slist2[i]
            sym = sym + ' ' + slist3[i]

            peren = peren + ' ' + slist41[i]
            peren1 = peren1 + ' ' + slist51[i]
        for i in range(0, len(slist46)):
            cor = cor + ' ' + slist46[i]
            cor1 = cor1 + ' ' + slist56[i]
        k ,fla = transl_into_dec(sym)
        k1 ,fla = transl_into_dec(nm1)
        k2 ,fla = transl_into_dec(nm2)
        if k1 == 'Запрещенная комбинация':
            num1.delete(0, END)
            num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
            return 0
        if k2 == 'Запрещенная комбинация' :
            num2.delete(0, END)
            num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
            return 0
        p = int(k1) + int(k2)
        sr = transl_into_8421(p)

        sr = str(sr).replace(' ', '')
        for i in range(0,int(len(sr)),4):
            slist14.insert(i, str(sr[i])+str(sr[i+1])+str(sr[i+2])+str(sr[i+3]))
        nu1, flag = transl_into_dec(nm1)
        nu2, flag = transl_into_dec(nm2)
        s2,flag = transl_into_dec(sym)

        l23 = Label(fra5, text='', relief=RIDGE)

        slist14.insert(0, 'Сумма :')
        slist1.insert(0, ' Слагаемое 1 :')
        slist2.insert(0, 'Слагаемое 2:')
        slist41.insert(0, 'Перенос еденицы :')
        slist51.insert(0, 'Перенос еденицы :')
        slist46.insert(0, 'Коррекция на 6 :')
        slist56.insert(0, 'Коррекция на 6 :')
        slist14.insert(len(slist14), ' = ')
        slist1.insert(len(slist1), ' = ')
        slist2.insert(len(slist2), ' =')
        slist41.insert(len(slist41), '')
        slist51.insert(len(slist51), '')
        slist46.insert(len(slist46), '')
        slist56.insert(len(slist56), '')
        slist14.insert(len(slist14), p)
        slist1.insert(len(slist1), k1)
        slist2.insert(len(slist2), k2)
        slist41.insert(len(slist41), '')
        slist51.insert(len(slist51), '')
        slist46.insert(len(slist46), '')
        slist56.insert(len(slist56), '')
        for l23 in fra5.grid_slaves():
           l23.grid_forget()
        for i,j in enumerate(slist41):
            l23 = Label(fra5,text='%s' % (j), relief=RIDGE,bg='lightgreen', fg="darkblue", font=('arial',10))
            l23.grid(row=0, column=i, sticky=NSEW)

        for i,j in enumerate(slist46):
            l23 = Label(fra5,text='%s' % (j), relief=RIDGE,bg='lightgreen', fg="darkblue", font=('arial',10))
            l23.grid(row=1, column=i, sticky=NSEW)

        for i,j in enumerate(slist1):
            l23 = Label(fra5,text='%s' % (j), relief=RIDGE,bg='lightgreen', fg="darkblue", font=('arial',10))
            l23.grid(row=2, column=i, sticky=NSEW)

        for i,j in enumerate(slist2):
            l23 = Label(fra5,text='%s' % (j), relief=RIDGE,bg='lightgreen', fg="darkblue", font=('arial',10))
            l23.grid(row=3, column=i, sticky=NSEW)

        for i, j in enumerate(slist14):
            l23 = Label(fra5, text='', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
            l23.grid(row=5, column=i, sticky=NSEW)
        l23 = Label(fra5, text='+', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
        l23.grid(row=5, column=0, sticky=NSEW)

        for i,j in enumerate(slist56):
            l23 = Label(fra5,text='%s' % (j), relief=RIDGE,bg='lightgreen', fg="darkblue", font=('arial',10))
            l23.grid(row=6, column=i, sticky=NSEW)

        for i,j in enumerate(slist51):
            l23 = Label(fra5,text='%s' % (j), relief=RIDGE,bg='lightgreen', fg="darkblue", font=('arial',10))
            l23.grid(row=7, column=i, sticky=NSEW)

        for i, j in enumerate(slist14):
            l23 = Label(fra5, text=' ', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
            l23.grid(row=8, column=i, sticky=NSEW)

        for i, j in enumerate(slist14):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE,bg='green', fg="darkblue", font=('arial',10))
            l23.grid(row=9, column=i, sticky=NSEW)
        l23 = Label(fra5, text='+', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
        l23.grid(row=8, column=0, sticky=NSEW)
    elif minus1 == -1 and minus2 != -1:
        flag = 0
        if nm1 >= nm2:
            for i in range(int(len(slist1)) - 1, -1, -1):
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm1)
            k2, fla = transl_into_dec(nm2)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)
            slist2[0] = ' - ' + slist2[0]
            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Слагаемое 1:')
            slist2.insert(0, ' Слагаемое 2:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14), p)
            slist1.insert(len(slist1), k1)
            slist2.insert(len(slist2), ' - ' + k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')

            for l23 in fra5.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra5, text='+', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='green', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra5, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)
        elif nm1 < nm2:
            flag=0
            for i in range(int(len(slist1)) - 1, -1, -1):
                buf = slist1[i]
                slist1[i] = slist2[i]
                slist2[i] = buf
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k1, fla = transl_into_dec(nm2)
            k2, fla = transl_into_dec(nm1)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            slist1[0] = ' - ' + slist1[0]
            slist14[0] = ' - ' + slist14[0]
            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Слагаемое 2:')
            slist2.insert(0, ' Слагаемое 1:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14),' - ' + str(p))
            slist1.insert(len(slist1),' - ' + k1)
            slist2.insert(len(slist2), k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            for l23 in fra5.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra5, text='+', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='green', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra5, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)
    elif minus1 != -1 and minus2 == -1:
        flag = 0
        if nm1 > nm2:
            for i in range(int(len(slist1)) - 1, -1, -1):
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]
                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm1)
            k2, fla = transl_into_dec(nm2)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)
            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)
            slist1[0] = ' - ' + slist1[0]
            slist14[0] = ' - ' + slist14[0]
            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Слагаемое 1:')
            slist2.insert(0, ' Слагаемое 2:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14),' - ' + str(p))
            slist1.insert(len(slist1), ' - ' +k1)
            slist2.insert(len(slist2), k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')

            for l23 in fra5.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra5, text='+', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='green', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra5, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)
        elif nm1 < nm2:
            flag = 0
            for i in range(int(len(slist1)) - 1, -1, -1):
                buf = slist1[i]
                slist1[i] = slist2[i]
                slist2[i] = buf
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm2)
            k2, fla = transl_into_dec(nm1)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)
            slist2[0] = ' - ' + slist2[0]
            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Слагаемое 2:')
            slist2.insert(0, ' Слагаемое 1:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14),  str(p))
            slist1.insert(len(slist1),  k1)
            slist2.insert(len(slist2), ' - ' + k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')

            for l23 in fra5.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra5, text='+', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra5, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)
            for i, j in enumerate(slist14):
                l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='green', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra5, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)
    elif minus1 !=-1 and minus2 != -1:
        for i in range(int(len(slist1)) - 1, -1, -1):
            tk1 = str(int(slist1[i], 2) + int(slist2[i], 2))
            if flag == 1:
                tk1 = str(int(tk1) + 1)
                slist41.insert(i, '+1')
                slist51.insert(i, '0001')
            else:
                slist41.insert(i, '   ')
                slist51.insert(i, '   ')
            if int(tk1) > 15:
                flag = 1  # перенос в старшую тетраду
            elif int(tk1) <= 15:
                flag = 0

            if int(tk1) >= 10:  # получение запрещенной комбинации
                tk1 = str(int(tk1) + 6)
                slist46.insert(i, '+6')
                slist56.insert(i, '0110')
            else:
                slist46.insert(i, '    ')
                slist56.insert(i, '    ')
            if int(tk1) > 15:
                flag = 1
            tk1 = str(bin(int(tk1)))[2:]
            tk1 = '0' * (4 - len(tk1)) + tk1
            tk1 = tk1[-4:]
            slist3.insert(i, tk1)
            if i == 0 and flag == 1:
                slist3.insert(0, '0001')

                slist1.insert(0, '')
                slist2.insert(0, '')
                slist41.insert(0, '+1')
                slist51.insert(0, '0001')
                slist46.insert(0, '')
                slist56.insert(0, '')

        n1 = n2 = sym = cor = cor1 = peren = peren1 = ''

        for i in range(0, len(slist3)):
            n1 = n1 + ' ' + slist1[i]
            n2 = n2 + ' ' + slist2[i]
            sym = sym + ' ' + slist3[i]
            peren = peren + ' ' + slist41[i]
            peren1 = peren1 + ' ' + slist51[i]
        for i in range(0, len(slist46)):
            cor = cor + ' ' + slist46[i]
            cor1 = cor1 + ' ' + slist56[i]
        k, fla = transl_into_dec(sym)
        k1, fla = transl_into_dec(nm1)
        k2, fla = transl_into_dec(nm2)
        if k1 == 'Запрещенная комбинация':
            num1.delete(0, END)
            num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
            return 0
        if k2 == 'Запрещенная комбинация':
            num2.delete(0, END)
            num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
            return 0
        p = int(k1) + int(k2)
        sr = transl_into_8421(p)

        sr = str(sr).replace(' ', '')
        for i in range(0, int(len(sr)), 4):
            slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
        nu1, flag = transl_into_dec(nm1)
        nu2, flag = transl_into_dec(nm2)
        s2, flag = transl_into_dec(sym)

        l23 = Label(fra5, text='', relief=RIDGE)
        slist1[0] = ' - ' + slist1[0]
        slist2[0] = ' - ' + slist2[0]
        slist14[0] = ' - ' + slist14[0]
        slist14.insert(0, 'Сумма :')
        slist1.insert(0, ' Слагаемое 1 :')
        slist2.insert(0, 'Слагаемое 2:')
        slist41.insert(0, 'Перенос еденицы :')
        slist51.insert(0, 'Перенос еденицы :')
        slist46.insert(0, 'Коррекция на 6 :')
        slist56.insert(0, 'Коррекция на 6 :')
        slist14.insert(len(slist14), ' = ')
        slist1.insert(len(slist1), ' = ')
        slist2.insert(len(slist2), ' =')
        slist41.insert(len(slist41), '')
        slist51.insert(len(slist51), '')
        slist46.insert(len(slist46), '')
        slist56.insert(len(slist56), '')
        slist14.insert(len(slist14), ' - ' + str(p))
        slist1.insert(len(slist1), ' - ' + k1)
        slist2.insert(len(slist2), ' - ' + k2)
        slist41.insert(len(slist41), '')
        slist51.insert(len(slist51), '')
        slist46.insert(len(slist46), '')
        slist56.insert(len(slist56), '')
        for l23 in fra5.grid_slaves():
            l23.grid_forget()
        for i, j in enumerate(slist41):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
            l23.grid(row=0, column=i, sticky=NSEW)
        for i, j in enumerate(slist46):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
            l23.grid(row=1, column=i, sticky=NSEW)
        for i, j in enumerate(slist1):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
            l23.grid(row=2, column=i, sticky=NSEW)
        for i, j in enumerate(slist2):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
            l23.grid(row=3, column=i, sticky=NSEW)
        for i, j in enumerate(slist14):
            l23 = Label(fra5, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=i, sticky=NSEW)
        l23 = Label(fra5, text='+', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
        l23.grid(row=5, column=0, sticky=NSEW)

        for i, j in enumerate(slist56):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
            l23.grid(row=6, column=i, sticky=NSEW)
        for i, j in enumerate(slist51):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='lightgreen', fg="darkblue", font=('arial', 10))
            l23.grid(row=7, column=i, sticky=NSEW)
        for i, j in enumerate(slist14):
            l23 = Label(fra5, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=i, sticky=NSEW)
        for i, j in enumerate(slist14):
            l23 = Label(fra5, text='%s' % (j), relief=RIDGE, bg='green', fg="darkblue", font=('arial', 10))
            l23.grid(row=9, column=i, sticky=NSEW)
        l23 = Label(fra5, text='+', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
        l23.grid(row=8, column=0, sticky=NSEW)

    return sym

def nmin(*args):
    nm1 = num14.get()
    nm2 = num24.get()
    nm1 = nm1.replace(' ', '')
    nm2 = nm2.replace(' ', '')
    minus1 = nm1.find('-')
    minus2 = nm2.find('-')
    nm1 = nm1.replace('-', '')
    nm2 = nm2.replace('-', '')
    tr = is_int(nm1)
    tr1 = is_8421(nm1)
    if tr == FALSE or tr1 == FALSE:
        num14.delete(0, END)
        num14.insert(1,"НЕВЕРНЫЙ ВВОД /ТОЛЬКО ЦЕЛЫЕ ЧИСЛА В КОДЕ 8421 /ДОПУСТИМЫ ТОЛЬКО 0 И 1")
        return 0
    tr111 = is_int(nm2)
    tr11 = is_8421(nm2)
    if tr111 == FALSE or tr11 == FALSE:
        num24.delete(0, END)
        num24.insert(2, "НЕВЕРНЫЙ ВВОД /ТОЛЬКО ЦЕЛЫЕ ЧИСЛА В КОДЕ 8421 /ДОПУСТИМЫ ТОЛЬКО 0 И 1")
        return 0

    if len(nm1) % 4 == 1:
        nm1 = '0'*3 + nm1
    if len(nm1) % 4 == 2:
        nm1 = '0'*2 + nm1
    if len(nm1) % 4 == 3:
        nm1 = '0' + nm1
    if len(nm2) % 4 == 1:
        nm2 = '0'*3 + nm2
    if len(nm2) % 4 == 2:
        nm2 = '0'*2 + nm2
    if len(nm2) % 4 == 3:
        nm2 = '0' + nm2
    if len(nm1) != len(nm2):
        if len(nm1) > len(nm2):
            nm2 = '0'*(len(nm1)-len(nm2)) + nm2
        elif len(nm2)>len(nm1):
            nm1 = '0'*(len(nm2)-len(nm1)) + nm1
    slist1 = []
    slist14 = []
    slist2 = []
    slist3 = []
    slist41 =[]
    slist46 = []
    slist51 = []
    slist56 = []
    for i in range(0,int(len(nm1)),4):
        slist1.insert(i, str(nm1[i])+str(nm1[i+1])+str(nm1[i+2])+str(nm1[i+3]))
        slist2.insert(i, str(nm2[i])+str(nm2[i+1])+str(nm2[i+2])+str(nm2[i+3]))
    if minus1 == -1 and minus2 == -1:
        if nm1>=nm2:
            flag = 0
            for i in range(int(len(slist1))-1,-1,-1):
                if flag == 1:
                    if int(slist1[i], 2) > 0:
                        y = int(slist1[i],2) - 1
                        tk1 = str(y - int(slist2[i], 2))
                        slist41.insert(i, '1 ->')
                        slist51.insert(i, '0001')
                    elif int(slist1[i], 2) == 0:
                        flag == 1
                        y = int(slist1[i], 2) - 1
                        tk1 = str(y - int(slist2[i], 2))
                        slist41.insert(i, '1 ->')
                        slist51.insert(i, '0001')
                else:
                  slist41.insert(i, '   ')
                  slist51.insert(i, '   ')
                  tk1 = str(int(slist1[i],2) - int(slist2[i],2))

                if int(slist1[i],2) < int(slist2[i],2):
                    flag = 1  # заем

                    u = '1'+str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i],2) >= int(slist2[i],2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0'*(4-len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)


            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0,len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            #k ,fla = transl_into_dec(minu)
            k1 ,fla = transl_into_dec(nm1)
            k2 ,fla = transl_into_dec(nm2)
            if k1 == 'Запрещенная комбинация':
                num14.delete(0, END)
                num14.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация' :
                num24.delete(0, END)
                num24.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0,int(len(sr)),4):
                slist14.insert(i, str(sr[i])+str(sr[i+1])+str(sr[i+2])+str(sr[i+3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            #s2,flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)

            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Уменьшаемое :')
            slist2.insert(0, 'Вычитаемое:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14), p)
            slist1.insert(len(slist1), k1)
            slist2.insert(len(slist2), k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')

            for l23 in fra6.grid_slaves():
               l23.grid_forget()
            for i,j in enumerate(slist41):
                l23 = Label(fra6,text='%s' % (j), relief=RIDGE,bg='#FFDFDF', fg="darkblue", font=('arial',10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i,j in enumerate(slist46):
                l23 = Label(fra6,text='%s' % (j), relief=RIDGE,bg='#FFDFDF', fg="darkblue", font=('arial',10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i,j in enumerate(slist1):
                l23 = Label(fra6,text='%s' % (j), relief=RIDGE,bg='#FFDFDF', fg="darkblue", font=('arial',10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i,j in enumerate(slist2):
                l23 = Label(fra6,text='%s' % (j), relief=RIDGE,bg='#FFDFDF', fg="darkblue", font=('arial',10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i,j in enumerate(slist56):
                l23 = Label(fra6,text='%s' % (j), relief=RIDGE,bg='#FFDFDF', fg="darkblue", font=('arial',10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i,j in enumerate(slist51):
                l23 = Label(fra6,text='%s' % (j), relief=RIDGE,bg='#FFDFDF', fg="darkblue", font=('arial',10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text=' ', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE,bg='#EE6666', fg="darkblue", font=('arial',10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE,bg='lightblue', fg="darkblue", font=('arial',10))
            l23.grid(row=8, column=0, sticky=NSEW)
        elif nm1<nm2:
            flag = 0
            for i in range(int(len(slist1)) - 1, -1, -1):
                buf = slist1[i]
                slist1[i] = slist2[i]
                slist2[i] = buf
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm2)
            k2, fla = transl_into_dec(nm1)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)
            slist1[0] = ' - ' + slist1[0]
            slist14[0] = ' - ' + slist14[0]

            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Вычитаемое:')
            slist2.insert(0, ' Уменьшаемое:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14), ' - ' + str(p))
            slist1.insert(len(slist1), ' - ' + k1)
            slist2.insert(len(slist2), k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')

            for l23 in fra6.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#EE6666', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)

    elif minus1 !=-1 and  minus2 != -1:
        if nm1<=nm2:
            flag = 0
            for i in range(int(len(slist1)) - 1, -1, -1):
                buf = slist1[i]
                slist1[i] = slist2[i]
                slist2[i] = buf
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm2)
            k2, fla = transl_into_dec(nm1)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)

            slist2[0] = ' - ' + slist2[0]
            slist14.insert(0, 'Разность :')
            slist1.insert(0, ' Вычитаемое:')
            slist2.insert(0, ' Уменьшаемое:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14),  str(p))
            slist1.insert(len(slist1),  k1)
            slist2.insert(len(slist2),  ' - ' + k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')

            for l23 in fra6.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#EE6666', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)
        elif nm1 > nm2:
            flag = 0
            for i in range(int(len(slist1)) - 1, -1, -1):
                if flag == 1:
                    y = int(slist1[i], 2) - 1
                    tk1 = str(y - int(slist2[i], 2))
                    slist41.insert(i, '1 ->')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                    tk1 = str(int(slist1[i], 2) - int(slist2[i], 2))

                if int(slist1[i], 2) < int(slist2[i], 2):
                    flag = 1  # заем

                    u = '1' + str(slist1[i])
                    tk1 = str(int(u, 2) - int(slist2[i], 2))
                    tk1 = str(int(tk1) - 6)
                    slist46.insert(i, '-6')
                    slist56.insert(i, '0110')
                elif int(slist1[i], 2) >= int(slist2[i], 2):
                    flag = 0
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm1)
            k2, fla = transl_into_dec(nm2)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) - int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)
            if len(slist14) < len(slist1):
                slist14.insert(0, '0000')
            l23 = Label(fra5, text='', relief=RIDGE)
            slist1[0] = ' - ' + slist1[0]
            slist14[0] = ' - ' + slist14[0]
            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Уменьшаемое:')
            slist2.insert(0, ' Вычитаемое:')
            slist41.insert(0, 'Заем еденицы :')
            slist51.insert(0, 'Заем еденицы :')
            slist46.insert(0, 'Коррекция на -6 :')
            slist56.insert(0, 'Коррекция на -6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14),' - ' + str(p))
            slist1.insert(len(slist1), ' - ' +k1)
            slist2.insert(len(slist2), k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            for l23 in fra6.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#EE6666', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=0, sticky=NSEW)
    elif minus1 == -1 and minus2 != -1:
        flag = 0
        if nm1 >= nm2 or nm1<nm2:

            for i in range(int(len(slist1)) - 1, -1, -1):
                tk1 = str(int(slist1[i], 2) + int(slist2[i], 2))
                if flag == 1:
                    tk1 = str(int(tk1) + 1)
                    slist41.insert(i, '+1')
                    slist51.insert(i, '0001')
                else:
                    slist41.insert(i, '   ')
                    slist51.insert(i, '   ')
                if int(tk1) > 15:
                    flag = 1  # перенос в старшую тетраду
                elif int(tk1) <= 15:
                    flag = 0

                if int(tk1) >= 10:  # получение запрещенной комбинации
                    tk1 = str(int(tk1) + 6)
                    slist46.insert(i, '+6')
                    slist56.insert(i, '0110')
                else:
                    slist46.insert(i, '    ')
                    slist56.insert(i, '    ')
                if int(tk1) > 15:
                    flag = 1
                tk1 = str(bin(int(tk1)))[2:]
                tk1 = '0' * (4 - len(tk1)) + tk1
                tk1 = tk1[-4:]
                slist3.insert(i, tk1)
                if i == 0 and flag == 1:
                    slist3.insert(0, '0001')

                    slist1.insert(0, '')
                    slist2.insert(0, '')
                    slist41.insert(0, '+1')
                    slist51.insert(0, '0001')
                    slist46.insert(0, '')
                    slist56.insert(0, '')

            n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

            for i in range(0, len(slist3)):
                n1 = n1 + ' ' + slist1[i]
                n2 = n2 + ' ' + slist2[i]
                minu = minu + ' ' + slist3[i]

                peren = peren + ' ' + slist41[i]
                peren1 = peren1 + ' ' + slist51[i]
            for i in range(0, len(slist46)):
                cor = cor + ' ' + slist46[i]
                cor1 = cor1 + ' ' + slist56[i]
            #k, fla = transl_into_dec(minu)
            k1, fla = transl_into_dec(nm1)
            k2, fla = transl_into_dec(nm2)
            if k1 == 'Запрещенная комбинация':
                num1.delete(0, END)
                num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            if k2 == 'Запрещенная комбинация':
                num2.delete(0, END)
                num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
                return 0
            p = int(k1) + int(k2)
            sr = transl_into_8421(p)

            sr = str(sr).replace(' ', '')
            for i in range(0, int(len(sr)), 4):
                slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
            nu1, flag = transl_into_dec(nm1)
            nu2, flag = transl_into_dec(nm2)
            s2, flag = transl_into_dec(minu)

            l23 = Label(fra5, text='', relief=RIDGE)

            slist14.insert(0, 'Сумма :')
            slist1.insert(0, ' Уменьшаемое :')
            slist2.insert(0, 'Вычитаемое:')
            slist41.insert(0, 'Перенос еденицы :')
            slist51.insert(0, 'Перенос еденицы :')
            slist46.insert(0, 'Коррекция на 6 :')
            slist56.insert(0, 'Коррекция на 6 :')
            slist14.insert(len(slist14), ' = ')
            slist1.insert(len(slist1), ' = ')
            slist2.insert(len(slist2), ' =')
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            slist14.insert(len(slist14), p)
            slist1.insert(len(slist1), k1)
            slist2.insert(len(slist2), k2)
            slist41.insert(len(slist41), '')
            slist51.insert(len(slist51), '')
            slist46.insert(len(slist46), '')
            slist56.insert(len(slist56), '')
            for l23 in fra6.grid_slaves():
                l23.grid_forget()
            for i, j in enumerate(slist41):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=0, column=i, sticky=NSEW)

            for i, j in enumerate(slist46):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=1, column=i, sticky=NSEW)

            for i, j in enumerate(slist1):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=2, column=i, sticky=NSEW)

            for i, j in enumerate(slist2):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=3, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=5, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=0, sticky=NSEW)

            for i, j in enumerate(slist56):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=6, column=i, sticky=NSEW)

            for i, j in enumerate(slist51):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
                l23.grid(row=7, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
                l23.grid(row=8, column=i, sticky=NSEW)

            for i, j in enumerate(slist14):
                l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#EE6666', fg="darkblue", font=('arial', 10))
                l23.grid(row=9, column=i, sticky=NSEW)
            l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))

            l23.grid(row=8, column=0, sticky=NSEW)
    elif minus1 != -1 and minus2 == -1:
        flag = 0
        for i in range(int(len(slist1)) - 1, -1, -1):
            tk1 = str(int(slist1[i], 2) + int(slist2[i], 2))
            if flag == 1:
                tk1 = str(int(tk1) + 1)
                slist41.insert(i, '+1')
                slist51.insert(i, '0001')
            else:
                slist41.insert(i, '   ')
                slist51.insert(i, '   ')
            if int(tk1) > 15:
                flag = 1  # перенос в старшую тетраду
            elif int(tk1) <= 15:
                flag = 0

            if int(tk1) >= 10:  # получение запрещенной комбинации
                tk1 = str(int(tk1) + 6)
                slist46.insert(i, '+6')
                slist56.insert(i, '0110')
            else:
                slist46.insert(i, '    ')
                slist56.insert(i, '    ')
            if int(tk1) > 15:
                flag = 1
            tk1 = str(bin(int(tk1)))[2:]
            tk1 = '0' * (4 - len(tk1)) + tk1
            tk1 = tk1[-4:]
            slist3.insert(i, tk1)
            if i == 0 and flag == 1:
                slist3.insert(0, '0001')

                slist1.insert(0, '')
                slist2.insert(0, '')
                slist41.insert(0, '+1')
                slist51.insert(0, '0001')
                slist46.insert(0, '')
                slist56.insert(0, '')

        n1 = n2 = minu = cor = cor1 = peren = peren1 = ''

        for i in range(0, len(slist3)):
            n1 = n1 + ' ' + slist1[i]
            n2 = n2 + ' ' + slist2[i]
            minu = minu + ' ' + slist3[i]

            peren = peren + ' ' + slist41[i]
            peren1 = peren1 + ' ' + slist51[i]
        for i in range(0, len(slist46)):
            cor = cor + ' ' + slist46[i]
            cor1 = cor1 + ' ' + slist56[i]
        # k, fla = transl_into_dec(minu)
        k1, fla = transl_into_dec(nm1)
        k2, fla = transl_into_dec(nm2)
        if k1 == 'Запрещенная комбинация':
            num1.delete(0, END)
            num1.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
            return 0
        if k2 == 'Запрещенная комбинация':
            num2.delete(0, END)
            num2.insert(1, "ЗАПРЕЩЕННАЯ КОМБИНАЦИЯ")
            return 0
        p = int(k1) + int(k2)
        sr = transl_into_8421(p)

        sr = str(sr).replace(' ', '')
        for i in range(0, int(len(sr)), 4):
            slist14.insert(i, str(sr[i]) + str(sr[i + 1]) + str(sr[i + 2]) + str(sr[i + 3]))
        nu1, flag = transl_into_dec(nm1)
        nu2, flag = transl_into_dec(nm2)
        s2, flag = transl_into_dec(minu)

        l23 = Label(fra5, text='', relief=RIDGE)
        slist14[0] = ' - ' + slist14[0]
        slist1[0] = ' - ' + slist1[0]
        slist2[0] = ' - ' + slist2[0]
        slist14.insert(0, 'Сумма :')
        slist1.insert(0, ' Уменьшаемое :')
        slist2.insert(0, 'Вычитаемое:')
        slist41.insert(0, 'Перенос еденицы :')
        slist51.insert(0, 'Перенос еденицы :')
        slist46.insert(0, 'Коррекция на 6 :')
        slist56.insert(0, 'Коррекция на 6 :')
        slist14.insert(len(slist14), ' = ')
        slist1.insert(len(slist1), ' = ')
        slist2.insert(len(slist2), ' =')
        slist41.insert(len(slist41), '')
        slist51.insert(len(slist51), '')
        slist46.insert(len(slist46), '')
        slist56.insert(len(slist56), '')
        slist14.insert(len(slist14), ' - ' + str(p))
        slist1.insert(len(slist1), ' - ' + k1)
        slist2.insert(len(slist2), ' - ' + k2)
        slist41.insert(len(slist41), '')
        slist51.insert(len(slist51), '')
        slist46.insert(len(slist46), '')
        slist56.insert(len(slist56), '')
        for l23 in fra6.grid_slaves():
            l23.grid_forget()
        for i, j in enumerate(slist41):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
            l23.grid(row=0, column=i, sticky=NSEW)

        for i, j in enumerate(slist46):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
            l23.grid(row=1, column=i, sticky=NSEW)

        for i, j in enumerate(slist1):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
            l23.grid(row=2, column=i, sticky=NSEW)

        for i, j in enumerate(slist2):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
            l23.grid(row=3, column=i, sticky=NSEW)

        for i, j in enumerate(slist14):
            l23 = Label(fra6, text='', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=5, column=i, sticky=NSEW)
        l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
        l23.grid(row=5, column=0, sticky=NSEW)

        for i, j in enumerate(slist56):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
            l23.grid(row=6, column=i, sticky=NSEW)

        for i, j in enumerate(slist51):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#FFDFDF', fg="darkblue", font=('arial', 10))
            l23.grid(row=7, column=i, sticky=NSEW)

        for i, j in enumerate(slist14):
            l23 = Label(fra6, text=' ', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))
            l23.grid(row=8, column=i, sticky=NSEW)

        for i, j in enumerate(slist14):
            l23 = Label(fra6, text='%s' % (j), relief=RIDGE, bg='#EE6666', fg="darkblue", font=('arial', 10))
            l23.grid(row=9, column=i, sticky=NSEW)
        l23 = Label(fra6, text='-', relief=RIDGE, bg='lightblue', fg="darkblue", font=('arial', 10))

        l23.grid(row=8, column=0, sticky=NSEW)





def dlt(*args):
    num1.delete(0, END)
    num2.delete(0, END)
    return 0
def dlt4(*args):
    num14.delete(0, END)
    num24.delete(0, END)
    return 0
def dlt1(*args):
    num.delete(0, END)
    return 0
def dlt2(*args):
    numd.delete(0, END)
    return 0
from tkinter import *


root=Tk()
root.title("8421 - code Calculator")
frat = Frame(root,width=2500,height=2000,bg="lightblue", bd=2,)
frab = Frame(root,width=2500,height=2000,bg="lightblue", bd=2,)
frat.pack(side =TOP)
frab.pack(side =BOTTOM)
fra1 = Frame(frat,width=2500,height=2000,bg="lightblue", bd=2,)
fra2 = Frame(frat,width=2500,height=2000,bg="#FAFF8D",bd=2)
fra3 = Frame(frab,width=2500,height=2500,bg="lightgreen",bd=2)
fra5 = Frame(fra3,width=500,height=200,bg="lightgreen",bd=0)
fra4 = Frame(frab,width=2500,height=2000,bg="#FFDFDF",bd=2)
fra6 = Frame(fra4,width=500,height=200,bg="#FFDFDF",bd=2)
fra1.pack(side =LEFT)
fra2.pack(side =RIGHT)
fra3.pack(side = LEFT)
fra4.pack(side = RIGHT)
fra5.pack(side = BOTTOM)
fra6.pack(side = BOTTOM)
fra7 = Frame(fra1,width=250,height=100,bg="lightblue",bd=2)
fra7.pack(side = BOTTOM)
fra8 = Frame(fra2,width=250,height=100,bg="#FAFF8D",bd=2)
fra8.pack(side = BOTTOM)
# SUM
label = Label( fra3, text = 'Сложение в коде 8421', font=('arial',10), bg="lightgreen", fg="darkblue")
label.pack()
num1 = Entry(fra3, width=80, bd=8)
num1.insert(1,'Введите число в коде 8421')
lae = Label(fra3, text= '+', font=('arial',10), bg="lightgreen", fg="darkblue")
num2 = Entry(fra3, width=80, bd=8)
num2.insert(1,'Введите число в коде 8421')
num1.pack()
lae.pack()
v1 = StringVar()
num2.pack()
bt31 = Button(fra3,
text="Очистить", #надпись на кнопке
width=30, height=1, #ширина и высота
bg="green", fg="darkblue")
bt31.pack()
bt31.bind("<Button-1>",dlt)
bt3 = Button(fra3,
text="Решение", #надпись на кнопке
width=30, height=2, #ширина и высота
bg="green", fg="darkblue")
bt3.pack()
bt3.bind("<Button-1>",nsum)
label4 = Label( fra3, text= 'Сложение проходит по правилам двоичного сложения \nПри получение запрещенной комбинация производится коррекция,прибавлением 6\nПри получение на ввод одного отрицательного числа - сложение заменяется вычитанием\nКомбинации 1010,1011,1100,1101,1110,1111- запрещены\n\n ', font=('arial',10), bg="lightgreen", fg="darkblue")
label4.pack()


# MIN
label = Label( fra4, text = 'Вычитание в коде 8421', font=('arial',10), bg="#FFDFDF", fg="darkblue")
label.pack()
num14 = Entry(fra4, width=80, bd=8)
lae4 = Label(fra4, text= '-', font=('arial',10), bg="#FFDFDF", fg="darkblue")
num24 = Entry(fra4, width=80, bd=8)
num14.pack()
lae4.pack()
v14 = StringVar()
num24.pack()
num14.insert(1,'Введите число в коде 8421')
num24.insert(1,'Введите число в коде 8421')
bt31 = Button(fra4,
text="Очистить", #надпись на кнопке
width=30, height=1, #ширина и высота
bg="#EE6666", fg="darkblue")
bt31.pack()
bt31.bind("<Button-1>",dlt4)
bt34 = Button(fra4,
text="Решение", #надпись на кнопке
width=30, height=2, #ширина и высота
bg="#EE6666", fg="darkblue")
bt34.pack()
bt34.bind("<Button-1>",nmin)

label4 = Label( fra4, text= 'Вычитание происходит по правилам двоичного вычитания поразрядно \nПри необходимости занять еденицу из старшего разряда произвожится коррекция на -6\nПри получении на ввод одного отрицательного числа вычитание заменяется сложением\nДля удобства вычислений из большего по модулю вычитается меньшее\nКомбинации 1010,1011,1100,1101,1110,1111- запрещены ', font=('arial',10), bg="#FFDFDF", fg="darkblue")
label4.pack()


# 10-8421

label = Label( fra1, text = 'Перевод из десчятичной СС в 8421-код', font=('arial',10), bg="lightblue", fg="darkblue")
label.pack()
num = Entry(fra1, width=80, bd=7)
num.pack()
num.insert(1,'Введите десятичное число')
bt11 = Button(fra1,
text="Очистить", #надпись на кнопке
width=30, height=1, #ширина и высота
bg="#81BEF7", fg="darkblue")
bt11.pack()
bt11.bind("<Button-1>",dlt1)
bt = Button(fra1,
text="Перевести в код-8421", #надпись на кнопке
width=30, height=2, #ширина и высота
bg="#81BEF7", fg="darkblue")
bt.pack()
bt.bind("<Button-1>",n8421)
var = StringVar()
sol1 = StringVar()
label4 = Label( fra1, text= 'Каждая цифра десятичного числа \nпереводится в двоичную и, при необходимости,\nдополняется до 4-х знаков незначащими нулями \n (напр. 2=0010)', font=('arial',10), bg="lightblue", fg="darkblue")
label4.pack()
label = Label( fra1, textvariable=var, font=('arial',10), bg="lightblue", fg="darkblue")
label.pack()

# 8421-10

label4 = Label( fra2, text= 'Перевод из кода 8421 в десятичную СС', font=('arial',10), bg="#FAFF8D", fg="darkblue")
label4.pack()
numd = Entry(fra2, width=80, bd=7)
numd.pack()
numd.insert(1,'Введите число в коде 8421')
bt21 = Button(fra2,
text="Очистить", #надпись на кнопке
width=30, height=1, #ширина и высота
bg="#FFE305", fg="darkblue")
bt21.pack()
bt21.bind("<Button-1>",dlt2)
btd = Button(fra2,
text="Перевести в десятичную систему", #надпись на кнопке
width=30, height=2, #ширина и высота
bg="#FFE305", fg="darkblue")
btd.pack()
btd.bind("<Button-1>",ndec)
va = StringVar()
sol2 = StringVar()
label4 = Label( fra2, text= 'Число в коде 8-4-2-1 делится на разряды \nпо 4 цифры, начиная с конца числа. \nКаждый из разрядов переводится в \nдесятичную СС, как двоичное число \n(напр. 0010=2)\nКомбинации 1010,1011,1100,1101,1110,1111\n - запрещены ', font=('arial',10), bg="#FAFF8D", fg="darkblue")
label4.pack()
labe = Label( fra2, textvariable=va,  font=('arial',10),  bg="#FAFF8D", fg="darkblue", )
labe.pack()
root.mainloop()