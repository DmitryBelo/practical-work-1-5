# Задание 1
'''p = {'Vlad':36, 'Bob':25, 'Katia':17, 'Peter':14, 'Anton':47}
print(p)'''

# Задание 2
'''for item in p:
    print(item)
for item in p:
    print(p[item])'''
    
# Задание 3
'''y = {'n':39, 'q':25, 'e':1, 'r':5, 's':8, 'm':80, 'f':36, 'c':88, 'z':96, 'l':27}
for item in y:
    if (y[item] % 2) == 0:
        y[item] = 200
print(y)'''

# Задание 4
'''for item in y:
    if (y[item] > 10):
        print(y[item])'''
        
# Задание 5
y = {'n':39, 'q':25, 'e':1, 'r':5, 's':8, 'm':80, 'f':36, 'c':88, 'z':96, 'l':27}
sumy = 0
for item in y:
    sumy = sumy + y[item]
print(sumy)
