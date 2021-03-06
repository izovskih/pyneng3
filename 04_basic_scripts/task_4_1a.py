# -*- coding: utf-8 -*-
'''
Задание 4.1a

Всё, как в задании 4.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 4.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

addrStr,cidrStr = input('Enter address and mask in format X.X.X.X/XX: ').split('/')
addr = addrStr.split('.')
mask = [0, 0, 0, 0]
for i in range(int(cidrStr)):
    mask[i//8] = mask[i//8] + (1 << (7 - i % 8))
net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])
print('Network:')
print(''.join('{:<10}'.format(i) for i in net))
print(''.join('{:10}'.format(bin(int(i))[2:].zfill(8)) for i in net))
print('\nMask:')
print('/' + cidrStr)
print(''.join('{:<10}'.format(int(i)) for i in mask))
print(''.join('{:10}'.format(bin(int(i))[2:].zfill(8)) for i in mask))


