# SEDICOMM University, PCAP - Programming Essentials in Python
# Author        : Zibnitskii Aleksandr
# Date          : 18/04/2020
# Description   : Console Simple Caclulator ver.2
#
# Task          : Написать программу калькулятор, который будет запрашивать 2 значения и что с
#                 ними сделать (+,-,/,*). Решение должно сохраняться, и вы должны дальше с ним работать.
#                 Например есть два числа 5,25 и +, то будет 30, и дальше я ввожу 10 и отнимаю его и так
#                 далее.
# Extended      : Дописать калькулятор таким образом, чтобы он работал, даже если есть ошибки в вводе. К
#                 примеру если пользователь захочет разделить на ноль или введёт символ место числа. По
#                 каждой ошибке у вас должен быть свой вывод по типу если /0, то написать что на 0 делить
#                 нельзя и тому подобное. Переписать программу на классах (можно без try/except)

iter = 0
arrData = []
arrResult = []

class Calc():

    def __init__(self):
        pass

    def doResult(self, data):
        self.data = data
        return result

    def getInput(self, mySym):
        global iter
        self.mySym = mySym
        if iter == 0:
            iter += 1

myCalc = Calc()
myCalc.getInput(input("Введите значение (число или знак математической операции): "))






