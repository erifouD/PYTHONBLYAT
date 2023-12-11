def f(d,b):
    return ((d[0]-b[0])**2+(d[1]-b[1])**2+(d[2]-b[2])**2)**0.5 
X=[float(i) for i in input("Введите координаты точки X").split()]
Y=[float(j) for j in input("Введите координаты точки Y").split()]
Z=[float(k) for k in input("Введите координаты точки Z").split()]
T=[float(a) for a in input("Введите координаты точки T").split()]
##XY=f(X,Y)
##XZ=f(X,Z)
##XT=f(X,T)
##YZ=f(Y,Z)
##YT=f(Y,T)
##ZT=f(Z,T)
c=['X  и Y','X и Z','X и T','Y и Z','Y и T','Z и T']
a=[f(X,Y),f(X,Z),f(X,T),(Y,Z),f(Y,T),f(Z,T)]
m=100000000000000000000000000000000000000000
for i in (0,len(a)+1):
    if i<m:
        m=a[i]
        L=c[i]
print('Минимальное расстояние между точками',L,'равное',m)
