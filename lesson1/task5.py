#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))
if a>b:
    c=a-b-1
else:
    c=b-a-1
print(f'буква {chr(a)} стоит на {a-96} месте, буква {chr(b)} стоит на {b-96} месте, между ними {c} букв')