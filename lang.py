
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

