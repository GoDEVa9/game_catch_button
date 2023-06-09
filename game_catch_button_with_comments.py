from tkinter import * #импортируем библиотеку для создание графических (GUI) приложений
import random #импортируем модуль для получения псевдорандомных чисел
from datetime import datetime #импортируем из модуля функцию для получения информации про время

root = Tk() #создаём окно приложения, присваиваем его переменной

stime = datetime.now() #создаём переменную, которой будет присвоено время при первом нажатии на кнопку
score = 0 #переменная для отсчёта количества нажатий на кнопку
def click(): #функция, которая задействуется при нажатии на кнопку
    global score, stime #с помощью оператора global получаем доступ к изменению глобальных переменных (объявленных вне блока оператора)
    b.place(x=random.randint(10, 470), y=random.randint(2, 470)) #с помощью метода .place задаём каждый раз при нажатии кнопки координаты для неё с помощью непредсказуемых псевдорандомных чисел
    ntime =  datetime.now() #вычисляем время последнего нажатия на кнопку 
    str1 = str(stime-ntime) #вычисляем разницу во времени между временем начала игры и настоящим, переводим данные в строковый тип
    if  int(str1[15]) <= 1: #проверяем, прошло ли больше заданного времени (сравниваем число, обозначающее секунды, переводим его в числовой тип, получаем возможность сравнивать, сравниваем с 1)
        Label(root, text='Вы не успели').place(relx=0.5, rely=0.5) #если времени прошло слишком много, выводим "Вы не успели"
    if score <= 9: #проверяем, меньше ли 10 раз была нажата кнопка
        score+=1 #если, да, то прибавляем к переменной-счётчику единицу
        if score == 1: #проверяем, один ли раз только была нажата кнопка
            stime = datetime.now() #если да, присваиваем внешней (глобальной) переменной значение времени первого нажатия на кнопку, отсчёт времени начинается
    else: #если не сработали предыдущие блоки с if
        Label(root, text='Поздравляем\n Вы выиграли').place(relx=0.5, rely=0.5) #выводим метку с поздравлением с победой
    
root.title('Игра') #задаём название приложения
root.geometry('500x500') #задаём размеры окна
root.resizable(False, False) #убираем возможность для пользователя растягивать окно по горизонтали и по вертикали
b=Button(root, text='Нажми', activebackground='red', command=click) #создаём кнопку. самое главное - атрибут command, который позволяет присвоить функцию, которая будет активироваться при нажатии на кнопку
b.place(x=random.randint(10, 470), y=random.randint(2, 470)) #задаём изначальное расположение кнопки непредсказуемо, но в определённом диапазоне в px, в соответствии с размером окна приложения, заданного с помощью .geometry()
root.mainloop() #всегда в конце применяем данный метод для своевременного обновления приложения


   