#!/home/igor/PycharmProjects/module_8/.venv/bin/python
# -*- coding: utf-8 -*-


def add_everything_up(a, b):
    try:
        return a + b
    except TypeError :
        return str(a) + str(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))