from tkinter import *
from tkinter import messagebox
import random
import pickle


def string_to_set(st):
    st = st.replace(',', ' ')
    st = st.replace(';', ' ')
    st = st.replace(':', ' ')
    st = st.replace('.', ' ')
    st = list(st.split(' '))
    for i in range(st.count('')):
        st.remove('')
    st = {int(i) for i in st}
    return st


def manually():
    selfA['state'] = NORMAL
    selfB['state'] = NORMAL
    selfC['state'] = NORMAL
    powA['state'] = DISABLED
    powB['state'] = DISABLED
    powC['state'] = DISABLED


def randomly():
    selfA['state'] = DISABLED
    selfB['state'] = DISABLED
    selfC['state'] = DISABLED
    powA['state'] = NORMAL
    powB['state'] = NORMAL
    powC['state'] = NORMAL


def notx(X, U):
    noX = set(U)
    for element in X:
        if element in noX:
            noX.remove(element)
    return noX


def gen_u_set(x):
    if rl.get() == '':
        r = 0
    else:
        r = int(rl.get())

    if ll.get() == '':
        l = 0
    else:
        l = int(ll.get())

    s = set()
    for i in range(x):
        s.add(random.randint(l, r))

    while len(s) < x:
        s.add(random.randint(l, r))
    return s


def generator():
    global A, B, C, U

    v = variables.get()
    if v == 0:
        if selfA.get() == '':
            A = set()
        else:
            A = string_to_set(selfA.get())

        if selfB.get() == '':
            B = set()
        else:
            B = string_to_set(selfB.get())

        if selfC.get() == '':
            C = set()
        else:
            C = string_to_set(selfC.get())
    if v == 1:
        if powA.get() == '':
            A = set()
        else:
            A = gen_u_set(int(powA.get()))

        if powB.get() == '':
            B = set()
        else:
            B = gen_u_set(int(powB.get()))

        if powC.get() == '':
            C = set()
        else:
            C = gen_u_set(int(powC.get()))

    if rl.get() == '':
        do = 0
    else:
        do = int(rl.get()) + 1

    if ll.get() == '':
        vid = 0
    else:
        vid = int(ll.get())

    U = set(range(vid, do))
    reslab.configure(text='A = {}\n'
                               'B = {}\n'
                               'C = {}\n'
                               'U = {}'.format(A, B, C, U))


def symrazn(X, Y):
    newx = set()
    for element in X:
        if element not in Y:
            newx.add(element)
    for element in Y:
        if element not in X:
            newx.add(element)
    return newx


def save_to_file(current_file):
    file = open('file.txt', 'ab')
    pickle.dump(current_file, file)
    file.close()


def save_to_res(current_file):
    file = open('res.txt', 'ab')
    pickle.dump(current_file, file)
    file.close()


def save_to_res_file(current_file):
    file = open('file1.txt', 'ab')
    pickle.dump(current_file, file)
    file.close()


def window_2():
    window2 = Toplevel(root)
    window2.title("Вікно №2")
    window2.geometry("600x400")
    window2.resizable(0, 0)
    gsample = Label(window2, text="D = not((notA U notB) ∩ ((notB U notC))")
    gsample.place(x=5, y=0)

    def show_solve():
        res1 = notx(A, U) | notx(B, U)
        res2 = notx(B, U) | notx(C, U)
        res3 = res1 & res2
        res4 = notx(res3, U)
        solve_lab = Label(window2, text=f"notA = {notx(A, U)}\n"
                                            f"notB = {notx(B, U)}\n"
                                            f"notC = {notx(C, U)}\n"
                                            f"1) notA U notB = {res1}\n"
                                            f"2) notB U notC = {res2}\n"
                                            f"3) (notA U notB) ∩ (notB U notC) = {res3}\n"
                                            f"4) not((notA U notB) ∩ (notB U notC)) = {res4}\n", font='Arial 10')
        solve_lab.place(x=5, y=120)
    res_lab = Label(window2, text='A = {}\n'
                                       'B = {}\n'
                                       'C = {}\n'
                                       'U = {}'.format(A, B, C, U),
                         font="Arial 10", justify=LEFT)
    res_lab.place(x=5, y=20)
    solve_butt = Button(window2, text="Розв'язати", width=20, command=show_solve)
    solve_butt.place(x=5, y=95)
    save_butt = Button(window2, text="Записати результат", width=30,
                           command=save_to_res(notx((notx(A, U) | notx(B, U)) & (notx(B, U) | notx(C, U)), U)))
    save_butt.place(x=350, y=95)


def window_3():
    window3 = Toplevel(root)
    window3.title("Вікно №3")
    window3.geometry("600x300")
    window3.resizable(0, 0)

    def show_sol():
        res1 = A | C
        res2 = B & res1
        solve_lab = Label(window3, text=f"A U C = {res1}\n"
                                            f"B ∩ (A U C) = {res2}", font='Arial 14')
        solve_lab.place(x=5, y=200)
    gsample = Label(window3, text="Спрощений вираз:\n" 
                                  "D = B ∩ (A U C)", font='Arial 12')

    gsample.place(x=5, y=0)
    res_lab = Label(window3, text='A = {}\n'
                                       'B = {}\n' 
                                       'C = {}\n'
                                       'U = {}'.format(A, B, C, U), font="Arial 12", justify=LEFT)
    res_lab.place(x=5, y=50)
    solve_butt = Button(window3, text="Розв'язати", width=20, command=show_sol)
    solve_butt.place(x=5, y=150)
    save_butt = Button(window3, text='Записати результат', width=30, command=save_to_file((B & (A | C))))
    save_butt.place(x=350, y=150)


def window_4():
    global X, Y
    window4 = Toplevel(root)
    window4.title("Вікно №4")
    window4.geometry("400x250")
    window4.resizable(0, 0)
    X = notx(A, U)
    Y = C
    mainlable = Label(window4, text="Заданий вираз:\n"
                                    "Z = X Δ Y", font='Arial 14')
    mainlable.place(x=90, y=5)
    operand_lab = Label(window4, text=f'X = {notx(A, U)}\n'
                                      f'Y = {C}\n'
                                      f'Виконання за допомогою авторського методу:\n' 
                                      f'Z = X Δ Y = {symrazn(X, Y)}\n', justify=LEFT, font='Arial 9')
    operand_lab.place(x=10, y=50)
    save_butt = Button(window4, text="Записати результат", width=30, command=save_to_res_file(symrazn(X, Y)))
    save_butt.place(x=10, y=150)


def window_5():
    window5 = Toplevel(root)
    window5.title("Вікно №5")
    window5.geometry("800x400")
    window5.resizable(0, 0)

    def difference():
        res_lab = Label(window5, text=f"Результат неспрощеного виразу: {set1}\n"
                                      f"Результат спрощеного виразу: {set2}\n" 
                                      f"Результат виразу Z за авторським методом: {set11}\n"
                                      f"Результат виразу Z за вбудованим методом: {set12}\n",
                                      font='Arial 12', justify=LEFT)
        res_lab.place(x=20, y=30)
        label = Label(window5, text=f"Виконання спрощеного і не спрощеного виразів: {res1}\n"
                                    f"Виконання за вбудованим і авторським методами: {res2}\n",
                                    font='Arial 13', justify=LEFT)
        label.place(x=10, y=170)

    cur_file = open('res.txt', 'rb')
    cur_file1 = open('file.txt', 'rb')
    cur_file2 = open('file1.txt', 'rb')
    set1 = pickle.load(cur_file)
    set2 = pickle.load(cur_file1)
    set11 = pickle.load(cur_file2)
    set12 = X ^ Y
    res1 = 'Результати сходяться. Все вірно!' if set1 == set2 else 'Помилка'
    res2 = 'Результати сходяться. Все вірно!' if set11 == set12 else 'Помилка'
    corelabel = Label(window5, text="Перевірмо, чи однаково працюють методи:")
    corelabel.place(x=10, y=130)
    save_butt = Button(window5, text="Порівняти результати обчислень:", width=81, command=difference)
    save_butt.place(x=10, y=350)


def window_6():
    G = 12
    N = 21
    result = ((N + G % 60) % 30 + 1)
    student = "П.І.Б.: Реу Дар'я Юріївна\nГрупа: ІО-12\nНомер варіанту: " + str(result)
    messagebox.showinfo(title="Дані студента", message=student)


root = Tk()
root.title("Меню")
root.geometry("600x600")
root.resizable(0, 0)

A = set()
B = set()
C = set()
U = set()
result5 = set()
final_result = set()
X = set()
Y = set()
variables = IntVar()
variables.set(0)
radbtn0 = Radiobutton(root, text="Ввести множини власноруч", variable=variables, value=0, command=manually)
radbtn1 = Radiobutton(root, text="Згенерувати множини", variable=variables, value=1, command=randomly)
radbtn0.place(x=0, y=0)
radbtn1.place(x=0, y=20)
reslab = Label(root, text='A = {}\n'
                          'B = {}\n'
                          'C = {}\n'
                          'U = {}'.format(A, B, C, U), font="Arial 10", justify=LEFT)
reslab.place(x=270, y=10)

LabA = Label(text="Введіть множину А:")
LabA.place(x=0, y=48)
LabB = Label(text="Введіть множину B:")
LabB.place(x=0, y=78)
LabC = Label(text="Введіть множину C:")
LabC.place(x=0, y=108)

selfA = Entry()
selfA.place(x=120, y=50)
selfB = Entry()
selfB.place(x=120, y=80)
selfC = Entry()
selfC.place(x=120, y=110)

LabA1 = Label(text="Введіть потужність А:")
LabA1.place(x=0, y=138)
LabB1 = Label(text="Введіть потужність B:")
LabB1.place(x=0, y=168)
LabC1 = Label(text="Введіть потужність C:")
LabC1.place(x=0, y=198)

powA = Entry(state=DISABLED)
powA.place(x=120, y=140)
powB = Entry(state=DISABLED)
powB.place(x=120, y=170)
powC = Entry(state=DISABLED)
powC.place(x=120, y=200)

LabU = Label(text="Введіть універсальну множину, від:")
LabU.place(x=0, y=230)
ll = Entry()
ll.place(x=120, y=250)
LabU1 = Label(text="до:")
LabU1.place(x=95, y=260)
rl = Entry()
rl.place(x=120, y=280)

buttgen = Button(text="Сгенерувати множини", width=75, command=generator)
buttgen.place(x=20, y=310)
stb = Button(text="Дані студента", width=75, command=window_6)
stb.place(x=20, y=350)
but1 = Button(text="Вікно 2", width=75, command=window_2)
but1.place(x=20, y=400)
but2 = Button(text="Вікно 3", width=75, command=window_3)
but2.place(x=20, y=450)
but3 = Button(text="Вікно 4", width=75, command=window_4)
but3.place(x=20, y=500)
but4 = Button(text="Вікно 5", width=75, command=window_5)
but4.place(x=20, y=550)

root.mainloop()
