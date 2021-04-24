def make_map():
    tic_map = []
    for i in range(9):
        tic_map.append(" ")
    return tic_map

def print_map(nk_map):
    print('-----')
    print(nk_map[0] + '|' + nk_map[1] + '|' + nk_map[2])
    print('-----')
    print(nk_map[3] + '|' + nk_map[4] + '|' + nk_map[5])
    print('-----')
    print(nk_map[6] + '|' + nk_map[7] + '|' + nk_map[8])
    print('-----')

def check_win(nk_map):
    check = False

    if nk_map[0] == nk_map[1] == nk_map[2] and nk_map[0] != ' ':
        check = True

    elif nk_map[0] == nk_map[4] == nk_map[8] and nk_map[0] != ' ':
        check = True

    elif nk_map[2] == nk_map[4] == nk_map[6] and nk_map[2] != ' ':
        check = True

    elif nk_map[3] == nk_map[4] == nk_map[5] and nk_map[3] != ' ':
        check = True

    elif nk_map[6] == nk_map[7] == nk_map[8] and nk_map[6] != ' ':
        check = True

    elif nk_map[0] == nk_map[3] == nk_map[6] and nk_map[0] != ' ':
        check = True

    elif nk_map[1] == nk_map[4] == nk_map[7] and nk_map[1] != ' ':
        check = True

    elif nk_map[2] == nk_map[5] == nk_map[8] and nk_map[2] != ' ':
        check = True
    return check

