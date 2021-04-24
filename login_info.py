'''
def login_check(input_id, input_pwd):
    f = open('temp.txt', 'r')
    lines = f.readlines()
    flag = False
    for line in lines:
        temp = line.split('\n')[0]
        id, pwd = temp.split(',')
        if id == input_id and pwd == input_pwd:
            flag = True
            break
    return flag
'''

'''
temp = open('temp.txt', 'r')
lines = temp.readlines()
print(lines)
temp.close()
'''

'''
f = open('temp.txt', 'a')
f.write("\naaa,bbb")
'''
temp = open('temp.txt', 'r')
lines = temp.readlines()

for line in lines:
    temp = line.split('\n')[0]
    id, pwd = temp.split(',')
    print(id)

account = open('temp.txt', 'a')
produce_id = input("Enter the your produce id : ")
account.write("\n" + produce_id)
