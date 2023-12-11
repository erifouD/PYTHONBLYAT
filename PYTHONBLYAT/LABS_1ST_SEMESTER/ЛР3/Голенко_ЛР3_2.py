x=int(input("Значение x:"))
y=int(input("Значение y:"))
if y>0 and x>0:
     z=(y*x)**(1/2)
     print(z)
elif y<0 and x<0:
    z=(y*x)**(1/2)
    print(z)
else:
    z=(x+y)/2
    print(z)
        
