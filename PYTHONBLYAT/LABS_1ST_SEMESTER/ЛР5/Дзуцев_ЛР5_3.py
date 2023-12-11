import math

def point_in_circle(point, circle_center, radius):
    dx = point[0] - circle_center[0]
    dy = point[1] - circle_center[1]
    distance = math.sqrt(dx**2 + dy**2)
    
    return distance <= radius

def count_points_in_circle(circle_center, radius, *points):
    count = 0
    for point in points:
        if point_in_circle(point, circle_center, radius):
            count += 1
    return count


circle_center = (10, 10)

radius = 20  

P = (2, 5)  
F = (6, 8)  
L = (1, 9)  

points = [P, F, L]

num_points_in_circle = count_points_in_circle(circle_center, radius, *points)
print(f"Количество точек, лежащих внутри окружности: {num_points_in_circle}")
