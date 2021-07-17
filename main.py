'''
#71
my_variable = ()
'''

'''
#72
movie_rank = ('닥터스트레인저', '스플릿', '럭키')
'''

'''
#73
t = (1)
'''

'''
#75
t = 1, 2, 3, 4
print(type(t))
'''

'''
#76
t = ('a', 'b', 'c')
t = ('A', 'B', 'C')
print(t)
'''

'''
#77
interest = ('삼성전자', 'LG전자', 'SK')
interest = list(interest)
print(interest)
'''

'''
#78
interest = ['삼성전자', 'LG전자', 'SK']
interest = tuple(interest)
print(interest)
'''

'''
#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
'''

'''
#80
a = []
for i in range (1, 100):
    if i % 2 == 0:
        a.append(i)
print(a)

a = tuple(a)
print(a)
'''

'''
def make_tuple():
    test = []
    for i in range(1, 100):
        if i % 2 == 0:
            test.append(i)
    tuple(test)
    return test

my_tuple = make_tuple()

print(my_tuple)
'''

'''
#81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *c = scores
c, a*, b = scores
print(a)
'''

'''
temp = {}
temp = {'a':123, 123 : 'c', 'a' : 123123123123}
temp['b'] = 123
print(temp)
'''

'''
#84
temp = {}
'''

'''
#85
temp = {'a' : 1000, 'b' : 1200, 'c' : 1800}
'''

'''
#86
temp = {'a' : 1000, 'b' : 1200, 'c' : 1800}
temp['d'] = 1200
temp['e'] = 1500
print(temp)
'''

'''
#87
temp = {'a' : 1000, 'b' : 1200, 'c' : 1800}
print(temp['a'])
'''

'''
#88
temp = {'a' : 1000, 'b' : 1200, 'c' : 1800, 'd' : 1200, 'e' : 1500}
temp['a'] = 1300
print(temp)
'''

'''
#89
temp = {'a' : 1000, 'b' : 1200, 'c' : 1800, 'd' : 1200, 'e' : 1500}
del temp['a']
print(temp)
'''

'''
#91
inventory = {'a' : [300, 20], 'b' : [400, 3], 'c' : [250, 100]}
print(inventory)
'''

'''
#92
inventory = {'a' : [300, 20], 'b' : [400, 3], 'c' : [250, 100]}
print(inventory['a'][0])
'''

'''
#93
inventory = {'a' : [300, 20], 'b' : [400, 3], 'c' : [250, 100]}
print(inventory['a'][1])
'''

'''
#94
inventory = {'a' : [300, 20], 'b' : [400, 3], 'c' : [250, 100]}
inventory['d'] = [500, 7]
print(inventory)
'''

'''
#95
temp = {'a' : 1200, 'b' : 1200, 'c' : 1800, 'd' : 1500, 'e' : 1000}
print(list(temp.keys()))
'''

'''
#96
temp = {'a' : 1200, 'b' : 1200, 'c' : 1800, 'd' : 1500, 'e' : 1000}
print(list(temp.values()))
'''

'''
#97
temp = {'a' : 1200, 'b' : 1200, 'c' : 1800, 'd' : 1500, 'e' : 1000}
values = list(temp.values())
print(values)
total_cost = 0
for value in values:
    total_cost += value

print("total_cost : {}".format(total_cost))
'''


#99
'''
temp = ('a', 'b', 'c')
test = (1, 2, 3)

output = zip(temp, test)

print(list(output))
'''

'''
keys = {'apple', 'pear', 'peach'}

yals = {300, 250, 400}

output = zip(keys, yals)
print(dict(output))
'''

'''
#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']

close_price = [10500, 10300, 10100, 10000, 11000]

output = zip(date, close_price)
print(dict(output))
'''