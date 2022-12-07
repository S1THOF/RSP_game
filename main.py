import random


print("Добро пожаловать в игру 'Камень-ножницы-бумага'!")
name = input("Введите ваше имя: ")
user_choice = ""
ai_choice = ""
select = ["R", "S", "P"]
choice_repeat = ""
repeat = True
while repeat:
    user_choice = input("Для выбора введите 'R' (Камень), 'S' (Ножницы), 'P' (Бумага): ")
    ai_choice = random.choice(select)
    print("Компьютер выбрал: ", ai_choice)
    if user_choice.lower() == "r" and ai_choice.lower() == "s":
        print(name, "победил!")
    elif user_choice.lower() == "r" and ai_choice.lower() == "p":
        print("Компьютер победил!")
    elif user_choice.lower() == "s" and ai_choice.lower() == "r":
        print("Компьютер победил!")
    elif user_choice.lower() == "s" and ai_choice.lower() == "p":
        print(name, "победил!")
    elif user_choice.lower() == "p" and ai_choice.lower() == "r":
        print(name, "победил!")
    elif user_choice.lower() == "p" and ai_choice.lower() == "s":
        print("Компьютер победил!")
    elif user_choice.lower() == ai_choice.lower():
        print("Ничья!")
    else:
        user_choice = input("Для выбора введите 'R' (Камень), 'S' (Ножницы), 'P' (Бумага): ")
    choice_repeat = input("Еще разок? (y/n)")
    if choice_repeat.lower() == "y":
        repeat = True
    elif choice_repeat.lower() == "n":
        print("Хорошего дня!")
        repeat = False
    else:
        choice_repeat = input("Еще разок? (y/n)")
