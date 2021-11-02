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
# вычисляем количество парт (2-школьника на парту)
desks_for_class1 = math_class1 // 2 + math_class1 % 2
desks_for_class2 = math_class2 // 2 + math_class2 % 2
desks_for_class3 = math_class3 // 2 + math_class3 % 2
#Узнаем общее количество парт
number_of_desks = desks_for_class1 + desks_for_class2 + desks_for_class3
print("Desks need: ", number_of_desks)
