import math 
def distance(p1,p2):
    return math.sqrt((p2[0]-p1)**2 + (p2[1] - p1[1])**2)

def farthest_point(points):
    far = points[0]
    max_dist = math.sqrt(far[0]**2 + far[1]**2)
    for p in points:
        d = math.sqrt(p[0]**2 + p[1]**2)
        if d > max_dist:
            max_dist = d
            far = p
    return far

n = int(input("enter number of points:"))
points = []

for i in range(n):
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    points.append((x,y))

p1 = tuple(map(int, input("enter first point (x,y):").split()))
p2 = tuple(map(int, input("enter second point (x,y):").split()))

print("Distance=", distance(p1, p2))
print("Farthest point=", farthest_point(points))


    
