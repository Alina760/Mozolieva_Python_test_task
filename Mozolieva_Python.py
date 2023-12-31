import os

bracket_sequence_text = """При тестировании скобочной последовательности "[((())()(())]]" можно заметить следующее:

    1.Правило открытости и закрытости:
Для каждой открывающей скобки должна быть соответствующая закрывающая скобка того же типа.
В данной последовательности имеется правильное соответствие между открывающими и закрывающими скобками типов
"(", "(", "(", ")", "(", ")", ")", "(", "(", ")", ")", ")", ")",
но последняя скобка является закрывающей квадратной скобкой "]".

    2.Правило правильного порядка:
Правильная скобочная последовательность должна иметь правильный порядок открытия и закрытия скобок.
В данной последовательности мы видим, что внутри последовательности присутствует пара скобок "()", 
но эта пара заключена внутри квадратных скобок "[]". Такое вложение нарушает правило правильного порядка.

    3.Исходя из вышесказанного, скобочная последовательность "[((())()(())]]" не является правильной.
Чтобы исправить ее и сделать правильной, нужно заменить закрывающую квадратную скобку в конце на открывающую квадратную скобку.
Таким образом, исправленная правильная скобочная последовательность будет выглядеть так: "[((())()(()))]".
В этой исправленной последовательности все скобки имеют соответствующие пары и правильный порядок открытия и закрытия."""


def number_check():
    print("Задание: Число больше семи")
    while True:
        try:
            number = float(input("Введите  число "))
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    if (number > 7):
        print("Результат: " + "Привет")


def name_check():
    print(" Задание: Вячеслав")
    name = input("Введите имя ")

    if (name == "Вячеслав"):
        print("Результат: " + "Привет, Вячеслав")
    else:
        print("Результат: " + "Нет такого имени")


def find_in_list():
    print("Задание: Массив")
    while True:
        try:
            input_str = input("Введите элементы массива через пробел: ")
            input_list = input_str.split()

            my_list = []
            for item in input_list:
                if float(item) % 3 == 0 and float(item) != 0:
                    my_list.append(float(item))
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    print("Результат:", *my_list)


def bracket_sequence():
    try:
        if os.path.exists("bracket_sequence.txt"):

            file = open("bracket_sequence.txt", 'r',encoding='utf-8')
            content = file.read()
            file.close()
            print(content)
        else:
            print(bracket_sequence_text)
    except Exception as e:
        print(bracket_sequence_text)


def end_of_the_algorithm():
    print("Алгоритм отработал.")
    input("Нажмите Enter, чтобы продолжить...")


work_app = True
while work_app:
    os.system('cls')

    print(""" __________________________________________________________________
            Впишите номер задания
              1- "Число больше семи",
              2- "Вячеслав" или
              3- "Массив".
              4- " Cкобочная последовательность"
               Для выхода впишите 9.
______________________________________________________________________
                                    """)
    number = input()
    if (number not in ["1", "2", "3", "4", "9"]):
        print("Некорректный ввод.")
        input("Нажмите Enter, чтобы продолжить...")

    elif (number == "1"):
        os.system('cls')
        number_check()
        end_of_the_algorithm()
    elif (number == "2"):
        os.system('cls')
        name_check()
        end_of_the_algorithm()
    elif (number == "3"):
        os.system('cls')
        find_in_list()
        end_of_the_algorithm()
    elif (number == "4"):
        os.system('cls')
        bracket_sequence()
        input("Нажмите Enter, чтобы продолжить...")

    else:
        work_app = False
