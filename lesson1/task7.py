'''7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
или равносторонним.'''

a = float(input('первый отрезок: '))
b = float(input('второй отрезок: '))
c = float(input('третий отрезок: '))

if a+b>=c and a+c>=b and b+c>= a:
    if a==b or b==c or c==a:
        if a==b and a==c:
            print('равносторонний')
        else:
            print('равнобедренный')
    else:
        print('разносторонний')
else:
    print('треугольник не существует')
