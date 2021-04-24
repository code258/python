from login_info import login_check
from game_info import make_map, print_map, check_win

i = 0
j = 0
while i != 5:
    input_id = input("Enter the id : ")
    input_pwd = input("Enter the pwd : ")

    flag = login_check(input_id, input_pwd)

    if flag:
        break

    if not flag:
        print("Login Fail")

if flag:
    print("succes")
    a = '0'
    b = 'X'
    turn = 0

    nk_map = make_map()

    print_map(nk_map)
    for i in range(9):
        if turn == 0:
            while True:
                num = int(input("Enter the position : "))
                if nk_map[num] == " ":
                    nk_map[num] = a
                    print_map(nk_map)
                    break
            turn = 1

        else:
            while True:
                num1 = int(input("Enter the position : "))
                if nk_map[num1] == " ":
                    nk_map[num1] = b
                    print_map(nk_map)
                    break
            turn = 0

        print_map(nk_map)
        nk_map_check = check_win(nk_map)

        if nk_map_check:
            break

    if nk_map_check and turn == 0:
        print("X win")
    elif nk_map_check and turn == 1:
        print("O win")

    if nk_map_check == False:
        print("draw")