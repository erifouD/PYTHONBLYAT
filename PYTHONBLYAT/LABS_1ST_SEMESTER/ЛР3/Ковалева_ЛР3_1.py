
a=int(input('Введите год: '))
if a%4!=0:
    print('365 дней в году')
elif a % 100==0:
    if a%400==0:
        print('366 дней в году')
    else:
        print('365 дней в году')
else:
    print('366 дней в году ')
    
        
