import math
def find_median(a, b, c):
    median_a=0.5*math.sqrt(2*(b**2) +2*(c**2)-(a**2))
    return median_a

def find_medians(a, b, c):
     median_a=find_median(a, b, c)
     median_b=find_median(b, a, c)
     median_c=find_median(c, a, b)
     return  median_a, median_b, median_c

a=3
b=4
c=5
medians=find_medians(a, b, c)
print("Медиана к стороне a:", medians[0])
print("Медиана к стороне b:", medians[1])
print("Медиана к стороне c:", medians[2])
