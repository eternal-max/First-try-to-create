#Задача 1 Вариант 1
def get_time(answer):
    if answer == 'Time out': 
        return None

    prom = answer[-1:-4:-1]
    return int(prom[::-1])

receive = 0
to = 0
res = []

ping = input('ping ')

for i in range(4):
    answer = input()

    time = get_time(answer)
    if time is None:
        to += 1
    else:
        res.append(time)
        receive += 1

proc = int((to / 4) * 100)

print('Ping statistics for 209.85.135.147:')
print(f'Packets: Sent = 4 Received = {receive} Lost = {to} ({proc}% loss)')
print('Approximate round trip times:')
print(f'Minimum = {min(res)} Maximum = {max(res)} Average = {sum(res) // len(res)}')


#Задача 2 Вариант 1
def digital_root(number):
    while len(number) > 1:
        total = 0

        for digit in number:
            total += int(digit)

        number = str(total)

    return int(number)

def is_happy(ticket):
    for i in range(1, len(ticket)):
        left = ticket[:i]
        right = ticket[i:]

        if digital_root(left) == digital_root(right):
            return "YES"   
    return "NO"

ticket = input()
print(is_happy(ticket))