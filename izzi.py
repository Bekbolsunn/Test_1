# Создать список ten, состоящий из целых чисел от одного до десяти
ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ten)
# Создать список evens, который состоит из четных чисел списка ten
evens = list(filter(lambda x: x % 2 == 0, ten))
# Вывести на экран список возведенных в квадрат чисел от списка evens.
print(evens)
events = list(map(lambda x: x ** 2, evens))
print(events)
# (Использовать лямбда-функции, filter, map)

# Создать функцию для вывода объекта списка по указанному индексу.
# Функция должна работать в бесконечном цикле с командой выхода.
# Индекс должен запрашиваться программой при запуске.
# При неверно указанном индексе использовать исключения с подсказкой ввода актуальных индексов указанного списка.
# У функции должен быть один аргумент по умолчанию -  список ten.



def ten1(lst):
    while 1:
        try:
            number = input("введите индекс: ")
            if number == 'stop':
                break
            else:
                print(lst[int(number)])
        except Exception:
            print(f"индекс: от 0 до {len(lst) - 1}")


ten1(ten)

