import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def closest_pairs(points):
    sorted_points = sorted(points, key=lambda point: point.x)
    return closest_pairs_helper(sorted_points)


def closest_pairs_helper(sorted_points):
    n = len(sorted_points)

    if n <= 3:
        return brute_force_closest_pairs(sorted_points)

    mid = n // 2
    left_points = sorted_points[:mid]
    right_points = sorted_points[mid:]

    left_closest = closest_pairs_helper(left_points)
    right_closest = closest_pairs_helper(right_points)

    min_dist = min(left_closest, right_closest)

    strip_points = []

    for point in sorted_points:
        if abs(point.x - sorted_points[mid].x) < min_dist:
            strip_points.append(point)

    strip_closest = closest_pairs_strip(strip_points, min_dist)

    return min(min_dist, strip_closest)


def closest_pairs_strip(strip_points, min_dist):
    strip_points.sort(key=lambda point: point.y)
    n = len(strip_points)
    min_dist_strip = min_dist

    for i in range(n):
        j = i + 1
        while j < n and (strip_points[j].y - strip_points[i].y) < min_dist_strip:
            min_dist_strip = min(min_dist_strip, distance(strip_points[i], strip_points[j]))
            j += 1

    return min_dist_strip


def brute_force_closest_pairs(points):
    n = len(points)
    min_dist = math.inf

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            min_dist = min(min_dist, dist)

    return min_dist


def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


# Demonstration of the Closest Pairs problem using the divide-and-conquer algorithm
if __name__ == "__main__":
    n = int(input("Enter the number of points: "))
    points = []

    for i in range(n):
        x = float(input(f"Enter x-coordinate for point {i+1}: "))
        y = float(input(f"Enter y-coordinate for point {i+1}: "))
        points.append(Point(x, y))

    min_distance = closest_pairs(points)

    print("Minimum distance between two closest pairs:", min_distance)
