# laguages = ["go", "java", 'Rust', "php", "python", "javascript", "ruby"]
# lang1 = "php"
# for spisok in laguages:
## z   if spisok == lang1:
#       print(lang1)
#       break

"""Напишите код, который берет цифру 7, умножает саму на себя же 5 раз"""
# i = 5
# c = 7
# for a in range(5):
#    c = c * 7
#    print(c)


"""Напишите код, который выведен на экран списка языков с нумерацией. 
языки = ['go', 'java', 'php', 'python', ' javascript', 'ruby'] 
Вывод: 0 go 1 java 2 php 3 python 4 javascript 5 ruby
"""
"""

"""
"""
items = ['молоко', 'сыр', 'творог', 'кефир', 'яблоко']
for i, item in enumerate(items):
    print(i + 1, item)
"""
"""

"""
"""
Напишите цикл который выведет на экран:
1,2,3,4,5,6,7,8,9,10, 9,8,7,6,5,4,3,2,1 Усиление:
Получите такой же результат но с ОДНИМ циклом """
"""
"""
"""
number = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
print(number + "  " + number[::-1] )
"""
"""

for number in range(1, 11):
    print(number, end=',')
for b in reversed(range(1, 10)):
    print(b, end=',')
"""
"""
spisok = ['go', 'java', 'php', 'python', ' javascript', 'ruby']
i = 1
for spisoks in spisok:
    print(i,spisoks)
    i += 1
"""
"""

У вас есть список имён: names = ('Максат','Лязат','Даньяр', 'Айбек', 'Атай', 'Салават',
 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан',)
Если первое имя = 0, второе имя = 1 и т.д.
"""
"""
names = ('Максат', 'Лязат', 'Даньяр', 'Айбек', 'Атай', 'Салават',
         'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан',)
i = 1
for name in names:
    print(i, name)
    i += 1
"""
"""
names = ('Максат', 'Лязат', 'Даньяр', 'Айбек', 'Атай', 'Салават',
         'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан',)
i = 1
for name in names:
    print(i, name)
    i += 1
"""

"""
У вас всё тот же список
имён:
имена = ('Максат', 'Лязат', 'Даниар', 'Айбек', 'Атай', 'Салават',
               'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат',' Аслан',)
Вы вводите каждое 2 имени.Подсказка: Всего имён 13.
"""
"""
names = ('Максат', 'Лязат', 'Даньяр', 'Айбек', 'Атай', 'Салават',
         'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат', 'Аслан',)
i = 13
print(names[0:13:2])
"""
"""
Есть переменная, которая хранит в себе число: Необходимо написать возможные условия для проверки: 
1. Это числовое трёхзначное? 
2. Это число положительное и чётное? 
3. Это событие выходило на 31 без остатка? 
4. Если это число больше 100 и оно появляется на 17 без остатка или
это число больше 150 и равно 13 ** 2 тогда показывается, что это зачисло 

for i in range(100, 1000):
    if i % 2 == 0:
        if i % 31 == 0:
            if i % 17 == 0 or i >= 150 or i == 13 ** 2:
                print(i)
"""
"""
9. Сгенерировать 200 чисел от -100 до 100:
  1. Каждое число которое делиться на 13 без остатка возводить в квадрат если оно чётное
  2. Каждое 7 число проверять на НЕчестность и выводить на экран если оно нечётное.
  3. Посчитать сколько чисел подходят под первое условие
  4. Посчитать сколько чисел подходят под второе условие
"""
'''
for i in range(-100, 100):
    if i % 13 == 0 //2 == 0:
        if i ** 2 // 7:
            print(i)
'''

"""
p = int(input("показатель: "))
n = int(input("Прелель: "))
i = 1
while i ** p  n:
    print(i ** p, end=" ")
    i +=1
print("\n Последнее число,"
     "возведение в степень:", i - 1)
"""
"""
k = int(input("Введите сумму кредита: "))
p = float(input("Введите процентную ставку: "))
m = int(input("Введите количество месяцев: "))
a = k * 0.01*p*(1+0.01*p)**m/((1+0.01*p)**m-1)
print(a)
"""

"""
k = float(input("Обхват по бюсту: "))
m = float(input("по бедрам: "))
n = float(input("по талии: "))
t = float(input("рост: "))
p = float(input("вес"))
k = 
"""
"""
o = int(input("Оклад работника: "))
dk = int(input("Колмчество календарных дней по производственному календарю: "))
df = int(input("Количество фактически отработанных дней: "))
p = int(input("Премии и надбавки, стимулирующие и мотивирующие выплаты"))
n = 13
u = int(input("Различный удержание: "))
zp = (o/dk*df+p) * ((100 - n)/100)
print(zp)
"""
"""
orm = int(input('Выберите количество оперативной памяти 4 или 8: '))
hard = int(input('Выберите объем: 256, 512, 1024 Gb: '))
ssd = int(input('Выберите 1 если SSD, выберите 0 если HDD: '))
price = int(input('Введите цену: '))
condition = int(input('Выберите состояние ноутбука 1 если новый, выберите 0 если б/у: '))

asus = 'Asus 550x 300$ 4Gb 1024HDD б/у'
acer = 'Acer Predator 600$ 4Gb 1024HDD новый'
samsung = 'Samsung 150 Turbo 900$ 8Gb 256SSD б/у'
hp = 'Hp 550x 1000$ 8Gb 256SSD новый'

'orm ssd hard condition price'

if orm == 4 and hard >= 1024 and ssd == False and price >= 300 and condition == False:
    print(asus, "Поздравляю с приобретением")

if orm == 4 and hard >= 1024 and ssd == False and price >= 600 and condition == True:
    print(acer, "Поздравляю с приобретением")

if orm == 8 and hard >= 256 and ssd == True and price >= 900 and condition == False:
    print(samsung, "Поздравляю с приобретением")

if orm == 8 and hard >= 256 and ssd == True and price >= 1000 and condition == True:
    print(hp, "Поздравляю с приобретением")
"""
"""
FIO = input("what is your surname name patronymic?: ")
age = int(input("How old are you?: "))
gender = input("What is you gender?: ")
place = input("Place of work?: ")
placeStud = input("Place of study?: ")
theCourse = int(input("What course?: "))
which = input("in which direction?: ")
programming = input("HaveYouStudiedProgrammingBefore?: ")
salaries = input("DediredSalary?: ")

Ilyas = "Ilyas"

if FIO == "Abdyzhaparov Ilyas Turusbekivich" and age == 29 and gender == "boy" \
        and place == "programmer" and placeStud == "ITCBOOTCAMP" \
        and theCourse == 5 and which == "python" and programming == "yes" and salaries >= "2500$":
    print(Ilyas)
"""

"""
stamp = (input("Выберите марку: "))
volume = float(input("Выберите объем двигателя: "))
price = int(input("Укажите цену: "))
color = input("Выберите цвет: ")
year = int(input("Выберите год: "))

mercedes = "mercedes-benz S-class"
BMW = "BMW e34"
Toyota = "Toyota Camry 50 S.E."

if stamp == "S-class" and volume >= 5 and price >= 8000 and color == "черный" and year >= 2004:
    print(mercedes, "Поздравляю с приобретением")

if stamp == "e34" and volume >= 2.5 and price >= 5000 and color == "темно-синий" and year >= 1995:
    print(BMW, "поздравляем с приобретением")

if stamp == "Camry 50" and volume >= 2.4 and price >= 13000 and color == "белый" and year >= 2013:
    print(Toyota, "поздравляем с приобретением")
"""

"""
cars = ["Mercedes", "BMW", "Toyota"]
for i, car in enumerate(cars):
    print(i + 1, car)
"""
"""

"""
"""
a = int(input("VVedite chislo: "))
b = int(input("Vvedite 2 chislo: "))
def sum(a,b):
    return a+b
print(sum(a,b))
"""
"""
breed = (input("Выберите породу: "))
color = (input("какой выбираете цвет:"))
ring = int(input("Выберите кольцо: "))
size = int(input("Выберите размер: "))

eagle1 = "dwarf"
eagle2 = "bald"
eagle3 = "imperial eagle"

if breed == "dwarf" and color == "gray" and ring >= 5 and size >= 50:
    print(eagle1, "Поздравляю с приобретением")
if breed == "bald eagle" and color == "bold with-gray" and ring >= 4 and size >= 70:
    print(eagle2,"Поздравляю с приобретением")
if breed == "imperial eagle" and color == "black" and ring >= 5 and size >= 70:
    print(eagle3, "Поздравляю с приобретением")
"""
"""
"""
"""
names = ("Jyldyz", "Aigerim",)
names2 = ("Bekmamat", "Nurbek",)
names3 = ("Azamat", "Shirin",)
names4 = ("Azamat", "Shirin",)
names5 = ("Azamat", "Shirin",)
empty = [names, names2, names3, names4, names5]
print(empty)
"""

"""
a = ("acer", "hp", "samsung")
for i in a:
    print(i)
"""
# Numbers (числа)    1 1.2
# Strings (строки)  'yui'
# Lists (списки) [1, 2 "sfs"]
# Dictionaries (словари)
# Tuples (кортежи)  (1,2)
# Sets (множества)
# Boolean (логический тип данных) "true, false"

"""
вариант1
enp = ['bwnd', 123, 12.3, (12, 'dsD')]
print(enp)
вариант2
names = "Mercedes"
names1 = 11.2
names2 = [1, 2, "sfs"]
names3 = (1, 2)
names4 = True and False
empty = [names, names1, names2, names3, names4]"""
"""
a = ["1", "1", "2", "3", "5", "8", "13", "21", "34", "55", "89"]
print("\n".join(a))
"""
"""
a = ["Iskender", "Ilyas", "Iman", "Jibek", "Madina"]
b = ""
print(b.join(a))
"""
"""
Создать 2 списка (List) заполнить данными, к первому списку добавить все объекты второго списка 
"""
"""
a = ["list"]
b = ["list2", "list3"]
print(a + b)
"""

"""
PROBLEM 5

Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack".

"""
"""
list = ['Jack', 'Jimmy', 'Jackson', 'Jhon',
     'Jackson', 'Jhon',  'Jimmy', 'Jackson',
     'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson',
     'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy',
     'Jack', 'Jackson', 'Jhon']
print(list.count("Jack"))
"""

""""
PROBLEM 6
Удалить из Листа №1 объект "Oskar"
"""
"""
list = ['Oscar', 'Jack', 'Jimmy', 'Jackson']
list.pop(0)
print(list)
"""

"""
PROBLEM 7

Создать пустой лист.

Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.
"""
"""
list = []
list.append("Ilyas 1992 Python")
print(list)
"""
"""
Взять Лист №2 из Google Colab узнать индекс объекта
(строки) "loop" и удалить его по индексу 
"""
"""
pythonList = ["int", "str", "bool", "if", "else", "elif",
              "loop", "tuple", "list", "None", True, False]
print(pythonList.index("loop"))
pythonList.pop(6)
print(pythonList)
"""
"""
Взять Лист №3 из Google Colab и посчитать произведение 
этих чисел т.е. умножить их все и вывести результат.
"""
"""
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
total = 0
for i in numbers:
    i = i * i
    total += i 
print(total)
total2 = 1
for i in numbers:
    total2 = total2 * i
print(total2)
"""
"""
numbers = [123, 32, 32, 43, 23, 45, ]
total = 1
for i in numbers:
    total = total * i
print(total)
"""

"""
number = (345, 53444, 2423, 423, 3)
total = 1
for i in number:
    total = total * i
print(total)
"""
"""
number = (5, 6, 7, 8, 9)
total = 1
for i in number:
    total = total * i
print(total)
"""
"""

words = 'itcbootcamp123course3445'
numbers = []
letters = []
for i in words:
    if i.isdigit():
        numbers.append(int(i))
    else:
        letters.append(i)
print(numbers)
print(letters)
"""
"""
"""
"""
Взять Лист №2 и вывести объекты с 1 по 3 индекс 
"""
"""
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList[1:4])
"""
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = len(numbers) // 2
print(numbers[0], a, numbers[-1])
"""
"""
words = ['anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar',
         'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means',
         'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку']
for i in words:
    if str.lower(i) == str.lower(i) [::-1]:
        print(i, "is polindrom")
    else:
        print(i, "" "not polindrom")
"""
"""
Общие значения списков
Даны списки:
Нужно вернуть список, который состоит из элементов, общих для этих двух списков
"""
"""
list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_1.extend(list_2)
print(list_1)
"""

"""
list1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in list1:

    if i in list2:
        c.append(i)
print(c)
"""
"""
dates_of_birth = {3, 10, 11, 13, 31, 21, 1, 10, 3, 5, 6, 6}
dates_of_birth.discard(7)
print(dates_of_birth)
"""
"""
Найти объекты которые есть и в SET №2 и в SET №3 из Google Colab
"""
"""
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.difference(farm_2))
"""
"""
В SET №3 из Google Colab найдите объекты которых нет SET №2
"""
"""
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = farm_2.difference(farm_1)
print(farm_3)
"""
"""
Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.

А затем удалите через .pop() элемент и посмотрите что же вы удалили

"""
"""
set = {"cow", "horse", "donkey", "cat", "dog"}
set.add("cat")
print(set)
set.pop()
"""
"""
Из Dictionary №1:
Добавьте в меню 
'besh_barmak' который стоит  130 сом.
Оказалось лагман слишком дешевый. Обновите цену на 135
Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
Удалить borsh
"""
"""
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({"besh barmak": 130})
menu.update({"lagman": 135})
menu.pop("borsh")
print(menu)
"""
"""
Из Dictionary №1:
Добавьте в меню 
напитки как ключ "drinks", 
А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.
"""
"""
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu["drink"] = 'Coca-cola', 'Sprite', 'Fanta'
print(menu)
"""
"""
Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
С помощь цикла for пройти вывести на экран строку:
"Здравствуйте <Имя>  Прекрасная профессия <Профессия>"
"""
"""
names = {'Niyaz': "medic", 'Adilet': "kosmonavt", 'Azamat': "slesar", 'Kadyr': "miliciya", 'Sultan': "biznesman"}
for i in names:
    print(i, names, "здраствуйте", "Прекрасная профессия!")
"""

"""
Создайте SET который хранит в себе все методы  для работы  с  SET.
Создайте второй SET который хранит в себе  методы  для работы  
с  Dictionary которые вы сегодня узнали.
Проверьте какие методы похожи у этих типов данные
"""
"""
set = {"difference", "add", "pop"}
set2 = {"update", "pop", "keys"}
print(set.intersection(set2))
"""

"""
Создайте пустой словарь.
Запустите цикл который 3 раза спросит его имя и его пароль.
Записывайте имя пользователя как ключ, а пароль как его значение
"""
"""
a = {}
b = a["Ilyas"] = "python"
for i in b:
    print(a)
"""
"""
my_set = set()
for i in range(10):
    num = input("what is your name: ")
    my_set.add(num)
print(my_set)
print(tuple(my_set))
"""
"""
dic = {}
print(type(dic))
dic = 3
while dic < 4:
    print(dic)
    dic += 3
print({'Ilyas': 'python'})
"""
"""
set = {"cow", "horse", "donkey", "cat", "dog"}
set.add("cat")
print(set)
set.pop()
"""
"""
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
all_months = months_a.union(months_b)
all_months.add("dec")
all_months.update(months_a, months_b)
all_months |= months_a | months_b
print(all_months)
"""
"""
x = {1, 2, 3}
y = {4, 3, 6}
x.intersection_update(y)
print(x)
"""
"""
dict_sample = {"Company": "Toyota",
               "model": "premio",
               "year": 2012}
x = dict_sample["model"]
print(x)
"""
"""
car = {"Company": "BMW",
       "Model": "X5",
       "Year": 2021}
print(car)
"""
"""
import turtle

colors = ["red", "purple", "blue",
          "green", "yellow", "orange"]
t = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 5)
    t.forward(x)
    t.left(50)
"""
"""
number = 12321

if str(number)[::-1] == str(number):
    print("Number:", number, " is a Palindrome")
else:
    print("Number:", number, " is not a Palindrome")

"""
"""
number = "ara"
if str(number)[::-1] == str(number):
    print("number", number, "this is polindrom")
else:
    print("number", number, "not a polindrom")

slovo = "Anna"
if str(slovo)[::1] == str(slovo):
    print(slovo, "да это полиндром")
else:
    print(slovo, "нет это не полиндром")
"""
"""

words = ["Anna",  'Civic', 'Kayak', 'Level', 'Madam',
         'Mom', 'Noon', 'Racecar', 'Radar', 'еще',
         'кабак', 'шалаш', 'лишил','language', 'which',
         'means', 'vendor', 'слова', 'фраза', 'введите',
         'слово', 'кнопку',]"""

name = 232
if str(name)[::-1] == str(name):
    print(name, "eto polindrom")
else:
    print(name, "eto ne polindrom")
"""
language = input('Какой язык вы знаете?: ')
age = int(input("Введите ваш возраст?: "))
experience = int(input("Введите ваш опыт?: "))
salary = int(input("Какую зарплату желаете:? "))

Maksat = "Python"
Bakyt = "java"
Mirbek = "javascript"

if language == "Python" and age >= 18 <= 65 and experience >= 3 and salary >= 55000 <= 60000:
    print(Maksat, "Максат, поздравляю Вы приняты на работу!!!")

if language == "java" and age >= 18 <= 65 and experience >= 3 and salary >= 35000 <= 40000:
    print(Bakyt, "Бакыт, поздравляю Вы приняты на работу!!!")

if language == "javascript" and age >= 18 <= 65 and experience >= 3 and salary >= 45000 <= 50000:
    print(Mirbek, "Мирбек, поздравляю Вы приняты на работу!!!")

else:
    print("и больше никто не принят!")
"""
"""
a = 343
if str(a)[::-1] == str(a):
    print(a, "this is polindrom")
else:
    print(a, "not is polindrom")
"""
