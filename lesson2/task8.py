#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
#чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

a = int(input('количество чисел: '))
b = int(input('цифра: '))
count = 0
for i in range(1,a+1):
    c = int(input('число' + str(i) + ': '))
    while c > 0:
        if c%10 == b:
            count += 1
        c = c // 10
print(f'цифр {b} - {count}')
