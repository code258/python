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

nk_map = make_map()

print_map(nk_map)

c = 0
while c != 1:
    a = '0'

    while True:
        num = int(input("Enter the position : "))
        if nk_map[num] == " ":
            nk_map[num] = a
            print_map(nk_map)
            break

    b = 'X'

    while True:
        num1 = int(input("Enter the position : "))
        if nk_map[num1] == " ":
            nk_map[num1] = b
            print_map(nk_map)
            break



def win():
    if nk_map[0] == a and nk_map[1] == a and nk_map[2] == a:
        c = 1
        print("O win")

    if nk_map[0] == a and nk_map[4] == a and nk_map[8] == a:
        c = 1
        print("O win")

    if nk_map[2] == a and nk_map[4] == a and nk_map[6] == a:
        c = 1
        print("O win")

    if nk_map[3] == a and nk_map[4] == a and nk_map[5] == a:
        c = 1
        print("O win")

    if nk_map[6] == a and nk_map[7] == a and nk_map[8] == a:
        c = 1
        print("O win")

    if nk_map[0] == a and nk_map[3] == a and nk_map[6] == a:
        c = 1
        print("O win")

    if nk_map[1] == a and nk_map[4] == a and nk_map[7] == a:
        c = 1
        print("O win")

    if nk_map[2] == a and nk_map[5] == a and nk_map[8] == a:
        c = 1
        print("O win")


'''
    if nk_map[0] == a and nk_map[1] == a and nk_map[2] == a:
        c = 1
        print("O win")
    if nk_map[0] == a and nk_map[4] == a and nk_map[8] == a:
        c = 1
        print("O win")
    if nk_map[2] == a and nk_map[4] == a and nk_map[6] == a:
        c = 1
        print("O win")
    if nk_map[3] == a and nk_map[4] == a and nk_map[5] == a:
        c = 1
        print("O win")
    if nk_map[6] == a and nk_map[7] == a and nk_map[8] == a:
        c = 1
        print("O win")
    if nk_map[0] == a and nk_map[3] == a and nk_map[6] == a:
        c = 1
        print("O win")
    if nk_map[1] == a and nk_map[4] == a and nk_map[7] == a:
        c = 1
        print("O win")
    if nk_map[2] == a and nk_map[5] == a and nk_map[8] == a:
        c = 1
        print("O win")




    if nk_map[0] == b and nk_map[1] == b and nk_map[2] == b:
        c = 1
        print("X win")
    if nk_map[0] == b and nk_map[4] == b and nk_map[8] == b:
        c = 1
        print("X win")
    if nk_map[2] == b and nk_map[4] == b and nk_map[6] == b:
        c = 1
        print("X win")
    if nk_map[3] == b and nk_map[4] == b and nk_map[5] == b:
        c = 1
        print("X win")
    if nk_map[6] == b and nk_map[7] == b and nk_map[8] == b:
        c = 1
        print("X win")
    if nk_map[0] == b and nk_map[3] == b and nk_map[6] == b:
        c = 1
        print("X win")
    if nk_map[1] == b and nk_map[4] == b and nk_map[7] == b:
        c = 1
        print("X win")
    if nk_map[2] == b and nk_map[5] == b and nk_map[8] == b:
        c = 1
        print("X win")
'''
