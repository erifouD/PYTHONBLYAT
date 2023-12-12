def find_divisors(number):
   divisors=[]
   for i in range(1, number+1):
       if number%i==0:
         divisors.append(i)
   return divisors
number=int(input("Введите число:"))
divisors=find_divisors(number)
for divisor in divisors:
    print(divisor, end=" ")

