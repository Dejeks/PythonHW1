'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
'''
arr = list(map(int,input().split()))

if arr[2] % arr[1] == 0 or arr[2] % arr[0] == 0:
    print('yes')
else:
    print('no')