# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int(config):
    """
    config - имя конфигурационного файла коммутатора

    Возвращает кортеж словарей:
    - первый словарь: порты в режиме access
      { 'FastEthernet0/12':10,
        'FastEthernet0/14':11,
        'FastEthernet0/16':17 }
    - второй словарь: порты в режиме trunk
      { 'FastEthernet0/1':[10,20],
        'FastEthernet0/2':[11,30],
        'FastEthernet0/4':[17] }

    """
    intLs = []
    intLsTrunk = []
    intLsAccess = []
    vlanLsAccess = []
    vlanLsTrunk = []
    fileLs = []
    with open(config) as f:
        fileLs += f.readlines()
        for i,line in enumerate(fileLs):
            if line.startswith('interface Fast'):
                intLs.append(line[line.find('Fast'):-1:])
            elif 'mode access' in line:
                i += 1
                if 'access vlan' in fileLs[i]:
                    k = fileLs[i].split()[-1:]
                    vlanLsAccess.append(int(k[0]))
                    intLsAccess.append(intLs.pop(-1))
                else:
                    vlanLsAccess.append(1)
                    intLsAccess.append(intLs.pop(-1))
            elif 'allowed vlan' in line:
                k = (line.split()[-1:])[0].split(',')
                ls = []
                for j in k:
                    ls.append(int(j))
                vlanLsTrunk.append(ls)
                intLsTrunk.append(intLs.pop(-1))
    dictAccess = dict(zip(intLsAccess,vlanLsAccess))
    dictTrunk = dict(zip(intLsTrunk,vlanLsTrunk))
    return dictAccess, dictTrunk
#    pass

print(get_int('config_sw2.txt'))
