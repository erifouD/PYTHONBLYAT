a=int(input("Введите сумму покупок:"))
if a>500:
    if a>1000:
        a=a*0.95
        print(a)
    else:
        a=a*0.97
        print(a)
else:
    print("Сумма со скидкой:",a)
    
            
        
