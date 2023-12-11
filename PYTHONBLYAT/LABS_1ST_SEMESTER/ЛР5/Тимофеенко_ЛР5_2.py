import math
def is_point(x,y,a,b,R):
    distance = math.sqrt((x-a)**2+(y-b)**2)
    if distance<R:
        return True
    else:
        return False
    R = 5
    a = 0
    b = 0
    p1 = 3
    p2 = 4
    f1 = 2
    f2 = 2
    l1 = 11
    l2 = 12
    count = 0
    if is_point_inside_circle(p1,p2,a,b,R):
        count += 1
    if is_point_inside_circle(f1,f2,a,b,R):
        count += 1
    if is_point_inside_circle(l1,l2,a,b,R):
        count += 1 
        print(f"Внутри окружности лежит {count} точек.")
