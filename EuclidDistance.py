import math

def euclidDistance(point1, point2): #iki nokta arasındaki mesafe
  
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

points = [(1, 2), (4, 6), (2, 3), (5, 7)]

for i in range(len(points)):     # tüm noktalar arasındaki mesafeler
  
  for j in range(i + 1, len(points)):

    distance = euclidDistance(points[i], points[j])

    print(f"Nokta {points[i]} ile nokta {points[j]} arasındaki mesafe: {distance}")

# minimum mesafe
distances = [euclidDistance(points[i], points[j]) for i in range(len(points)) for j in range(i + 1, len(points))]

min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")

# nokta (1, 2) ile nokta (4, 6) arasındaki mesafe: 5.0
# nokta (1, 2) ile nokta (2, 3) arasındaki mesafe: 1.4142135623730951
# nokta (1, 2) ile nokta (5, 7) arasındaki mesafe: 6.4031242374328485
# nokta (4, 6) ile nokta (2, 3) arasındaki mesafe: 3.605551275463989
# nokta (4, 6) ile nokta (5, 7) arasındaki mesafe: 1.4142135623730951
# nokta (2, 3) ile nokta (5, 7) arasındaki mesafe: 5.0
# minimum mesafe: 1.4142135623730951