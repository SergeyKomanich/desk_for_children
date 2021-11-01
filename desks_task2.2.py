"""
В школе решили набрать три новых математических класса.
Так как занятия по математике у них проходят в одно и то же время,
было решено выделить кабинет для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов.
Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.

Использовать только арифметические операторы. (Подсказка: понадобятся // + и %) Оператор IF использовать нельзя.
"""

math_class1 = int(input("Enter the number of students: "))
math_class2 = int(input("Enter the number of students: "))
math_class3 = int(input("Enter the number of students: "))

#Узнаем общее количество учеников
total_number_of_pupils = math_class1 + math_class2 + math_class3

# вычисляем количество парт (2-школьника на парту), сколько их останется после деления на 2, складываем эти два значения
number_of_desks = total_number_of_pupils // 2 + total_number_of_pupils % 2
print("Desks need: ", number_of_desks)