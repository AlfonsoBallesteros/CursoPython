# -*- coding: utf-8 -*-
for i in range(5):
    print(i)
print('-------------------')
for j in range(30):
    if j % 3 != 0:
        continue
    else:
        print(j**2)
print('-------------------')
for j in range(30):
    if j % 3 == 0:
        print(j , ' -> ' , j**2)
    elif j == 22:
        break
print('-------------------')
railroad = 'ferrocaril'
for letter in railroad:
    print(letter)