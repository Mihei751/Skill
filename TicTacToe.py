import random
playing_field = [i for i in range(1, 10)]
wins = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
move_number = 0
step_pl1 = []
step_pl2 = []
player = int(input("If playing alone, enter 1. If playing against each other, enter 2."))


def input_data_pl1(game_symbol):

    while True:
        print("Your turn", game_symbol)
        walks_pl1 = int(input("Where to post?"))
        if walks_pl1 >9 or walks_pl1 <1:
            print('Invalid field number')
            continue
        i = str(playing_field [walks_pl1-1])
        if i in "xo":
            print("Cell busy")
            continue
        else:
            playing_field [walks_pl1 -1] = game_symbol
            step_pl1.append(walks_pl1)
        break



def shows_matrix_playing_field():
    global move_number
    for i in range(3):
        print("|", playing_field [0+i*3],"|", playing_field [1+i*3],"|", playing_field [2+i*3],"|")
    print("Move number", move_number)


def ii(game_symbol):
    q = step_pl1 [move_number - 1]
    global step_pl2
    if move_number == 1:
        if q == 1 or q == 2 or q == 3:
            walks_pl2 = q + 6
            playing_field[walks_pl2 - 1] = game_symbol
            step_pl2.append(walks_pl2)
        if q == 7 or q == 8 or q == 9:
            walks_pl2 = q - 6
            playing_field[walks_pl2 - 1] = game_symbol
            step_pl2.append(walks_pl2)
        if q == 4:
            walks_pl2 = q + 2
            playing_field[walks_pl2 - 1] = game_symbol
            step_pl2.append(walks_pl2)
        if q == 6:
            walks_pl2 = q - 2
            playing_field[walks_pl2 - 1] = game_symbol
            step_pl2.append(walks_pl2)
        if q == 5:
            while True:
                walks_pl2 = random.randint(1, 9)
                if walks_pl2 == 5:
                    continue
                else:
                    playing_field[walks_pl2 - 1] = game_symbol
                break
            step_pl2.append(walks_pl2)
    if move_number > 1:
        while True:
            walks_pl2 = random.randint(1, 9)
            i = str(playing_field[walks_pl2 - 1])
            if i in "xo":
                continue
            else:
                playing_field[walks_pl2 - 1] = game_symbol
            break
        step_pl2.append(walks_pl2)


def check_win ():
    for a in wins:
        if playing_field[a[0]-1] == playing_field[a[1]-1] == playing_field[a[2]-1]:
            return playing_field[a[1]-1]


def main ():
    global move_number
    while True:
        check_win()
        move_number +=1
        if move_number > 3:
            winer = check_win()
            if winer:
                shows_matrix_playing_field()
                print(winer, "Victory!")
                break
        shows_matrix_playing_field()
        input_data_pl1("x")
        if player ==1:
            ii("o")
        else:
            input_data_pl1("o")
        continue


main()












