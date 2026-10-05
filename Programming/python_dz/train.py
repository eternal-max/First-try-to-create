#Задача 1 Вариант 1
w, h = map(int, input().split())
n = int(input())

a = [[0] * h for _ in range(w)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            a[x][y] = 1

print(w * h - sum(map(sum, a)))

#Задача 2 Вариант 1 
n, m = map(int, input().split())

colors = []
for _ in range(n):
    s = map(str, input())
    colors += list(s)

numbers = []
for _ in range(n):
    numbers += list(map(int, input().split()))

mask = {
    0: {'.'},
    1: {'.', 'B'},
    2: {'.', 'G'},
    3: {'.', 'G', 'B'},
    4: {'.', 'R'},
    5: {'.', 'R', 'B'},
    6: {'.', 'R', 'G'},
    7: {'.', 'R', 'G', 'B'}
}

ok = True
for i in range(n * m):
    if colors[i] not in mask[numbers[i]]:
        ok = False
        
if ok == True:
    print('YES')
else:
    print('NO')