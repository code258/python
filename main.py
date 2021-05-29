'''
import random

a = []

for k in range(0, 10):
    b = random.randrange(10)
    a.append(b)

print(a)

for i in range(10):
    for i in range(0, 9):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

print(a)
'''

'''
import random
def make_list():
    a = []
    for k in range(0, 10):
        b = random.randrange(10)
        a.append(b)
    return a

a = make_list()
print(a)

def change_list():
    for i in range(10):
        for i in range(0, 9):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

    return a

a = change_list()
print(a)
'''
import random

a = []

for k in range(0, 10):
    b = random.randrange(10)
    a.append(b)

print(a)
c = 0

for j in range(len(a)):
    if c > a[j]:
        c = a[j]
print(c)


'''
for l in range(0, 10):
    for j in range(0, 10):
        if a[j] == c:
            print(a[j])
            break
        if a[j] != c and j == 9:
            c += 1
'''

'''
1. 함수화를 먼저 시키고
2. select sort

4,2,1,3,100

1,2,4,3,100

1,2,3,4,100
'''