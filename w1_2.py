#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

int_check = 1
float_check = 1.1
list_check = ['a', '2']
tuple_check = ('b', '3')
str_check = 'Text'
dict_check = {'text_1': 'Text2'}


list_all = [int_check, float_check, list_check, tuple_check, str_check, dict_check]
for i in list_all:
    print(f'{i} is {type(i)}')