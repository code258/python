'''
a = int(input())
b = 0
c = []
for i in range(1, a):
    if a % i == 0:
        b += 1

if b == 1:
    print("True")
elif a == 1:
        print("1")
else:
    print("False")
'''

'''
c = []
b = 0

for a in range (0, 100):

    for i in range(1, a):
        if a % i == 0:
            b += 1

    if b == 1:
        c.append(a)
        b = 0

    else:
        b = 0

print(c)
'''

'''
def prime_number(a):
    b = 0
    for i in range(1, a):
        if a % i == 0:
            b += 1
    if b == 1:
        return b

c = []
for a in range(1, 100):

    b = prime_number(a)
    if b == 1:
        c.append(a)

print(c)
'''

'''
a = int(input("Enter the number : "))
total_num = 100
num = 0
while total_num != a:
    if a < total_num:
        total_num = int(total_num / 2)
        print("total_num : {}".format(total_num))

    elif a > total_num:
        total_num = int(total_num + (total_num / 2))
        print("total_num : {}".format(total_num))
'''

