import random

choices = ["камень", "ножницы", "бумага"]       #список
total_wins = 0
total_loses = 0

def all_score():                                   #все победы и проигрыши пользователя
    print(f'Всего побед: {total_wins}')
    print(f'Всего проигрышей: {total_loses}')

def menu():                                         #меню
        print('======= КАМЕНЬ НОЖНИЦЫ БУМАГА =======')
        print('1. Играть')
        print('2. Статистика')
        print('3.Выход')
        return int(input ('Выбор:'))
     
def get_user_choice():                  #ввод пользователя
    return input("Выберите камень, ножницы, бумага или выход:").lower()

def print_line():          #оформление
    print("=" * 20) 

def start_game(c):                    #действие игры
    computer = random.choice(choices)
    print_line()
    print("Компьютер выбрал:", computer)
    if c == computer:
        return "draw"
    elif (c == "камень" and computer == "ножницы") or (c == "ножницы" and computer == "бумага") or (c == "бумага" and computer == "камень"):
        return "win"
    else:
        return "lose"

def score_round(user_wins, user_loses, round_number):      #счет
    print(f'Раунд {round_number}')
    print(f'Счет: {user_wins} : {user_loses}')
    

def main():                     #главный(все действия)
    user_wins = 0       #попытки
    user_loses = 0
    user_draw = 0
    round_number = 0  
    while True:                 #повторение действия
        print_line()
        c = get_user_choice()
        
        if c == "выход":
            print_line()
            print("Игра завершена")
            break
        elif c not in choices:
            print_line()
            print("Ошибка ввода")
            continue
        result = start_game(c)
        if result == "win":
            user_wins += 1
            print_line()
            print('Победа')
        elif result == "lose":
            user_loses += 1
            print_line()
            print('Проигрыш')
        else:
             user_draw += 1
             print_line()
             print('Ничья')
        round_number += 1
        score_round(user_wins, user_loses, round_number)
    
        if user_wins == 3:
            print_line()
            print('Игрок выиграл!')
            break
        elif user_loses == 3:
            print_line()
            print('Игрок проиграл!')
            break
    global total_wins
    total_wins += user_wins
    global total_loses 
    total_loses += user_loses 


while True:
    choice = menu()
    if choice == 1:
        main()
    elif choice == 2:
        all_score()
    else:
        print("Игра завершена")
        break 
