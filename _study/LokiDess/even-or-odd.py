#
# Author        : Zibnitskii Aleksandr
# Date          : 03/05/2020
# Description   : Even or Odd number check
# Task          : Пользователь вводит число, если оно четное вывесть - “Even” если нет - “Odd”
#

num = 0

def checkNumber(num):
    if num == 0:
        rezult = "Your input iz Zero"
        return rezult
    rezult = "Number " + str(num)
    if num % 2 == 0:
        rezult = rezult + " is Even"
    else:
        rezult = rezult + " is Odd"
    return rezult

print("~" * 45)
while num != "***":
    num = input("Введите целое число или '***' для выхода: ")
    if num == "***":
        print("Всего хорошего!")
        print("~" * 45)
        break
    else:
        print(checkNumber(int(num)))
        print("~" * 45)




