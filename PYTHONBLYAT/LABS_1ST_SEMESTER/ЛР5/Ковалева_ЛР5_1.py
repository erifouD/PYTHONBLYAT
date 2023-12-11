def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def twin(n):
    for i in range(n,2*n-1):
        if is_prime(i) and is_prime(i+2):
            print(f'({i}, {i+2})')
n=int(input('Введите n: '))
print(twin(n))
    
