# SEDICOMM University, PCAP - Programming Essentials in Python
# Author        : Zibnitskii Aleksandr
# Date          : 11/04/2020
# Description   : Console Simple Caclulator ver.1
#
# Task          : Написать программу калькулятор, который будет запрашивать 2
#                 значения и что с ними сделать (+,-,/,*). Решение должно сохраняться,
#                 и вы должны дальше с ним работать. Например есть два числа 5,25 и +,
#                 то будет 30, и дальше я ввожу 10 и отнимаю его и так далее. 

save_input = []
first_iter = False

def InputFirstNum():
    global first_iter
    a = input("Input the first number: ")
    return float(a)

def InputSecondNum():
    b = input("Input the second number: ")
    return float(b)

def PrintBanner():
    print("-"*36)
    print("Select a math action [ +, -, / , * ]")
    print("or input 'x' - for exit")

def ActionSelect():
    usersel = input("Your choice: ")
    return usersel

def DoResult(user_input, user_select):
    print("-"*36)

while True:
    print(first_iter)
    save_input.append(InputFirstNum())
    print(first_iter)
    save_input.append(InputSecondNum()) 
    PrintBanner()
    user_choice = ActionSelect()
    if ((user_choice == "+") or (user_choice == "-")):
        DoResult(save_input, user_choice)
    else:
        print("Thank's for your cooperation! Good bye")
        break
    

