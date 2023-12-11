import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
def max_distance(points):
    max_dist=0
    max_points=()
    for i in range(len(points)):
        for j in range(i+1,len(points)):
          dist = distance(points[i][0], points[i][1], points[j][0], points[j][1])
          if dist > max_dist:
             max_dist = dist
             max_points =(points[i],points[j])
    return max_points
points = [(1,2),(3,4),(5,6),(7,8)]
max_points = max_distance(points)
max_dist = distance(max_points[0][0],max_points[0][1],max_points[1][0],max_points[1][1])
print(f"{max_dist},{max_points[0]} and {max_points[1]}.")
