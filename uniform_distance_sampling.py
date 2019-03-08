import math

# points: [absolute_x, absolute_y, ??]

def distance(p1, p2):
    delta_x = p1[0] - p2[0]
    delta_y = p1[1] - p2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

def get_resample_spacing(points):
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    
    top_left_x = min(xs)
    top_left_y = min(ys)
    top_left = [top_left_x, top_left_y]
    
    bottom_right_x = max(xs)
    bottom_right_y = max(ys)
    bottom_right = [bottom_right_x, bottom_right_y]

    diagonal = distance(top_left, bottom_right)

    S = diagonal / 40.0

    return S

# interpolation
def get_resample_points(points, S):
    D = 0
    resampled = []
    resampled.append(points[0])
    point = [None, None]
    

    i = 1
    # points will be changed, so range(1, len(points)) is a bad choice
    while i < len(points):
    #for i in range(1, len(points)):
        d = distance(points[i - 1], points[i])
        if D + d >= S:
            point[0] = points[i - 1][0] + ((S - D) / d) * (points[i][0] - points[i - 1][0])
            point[1] = points[i - 1][1] + ((S - D) / d) * (points[i][1] - points[i - 1][1])
            resampled.append([point[0], point[1]])
            points.insert(i, [point[0], point[1]])
            D = 0
        else:
            D = D + d
        i += 1
    return resampled

def interpolation(points):
    
    S = get_resample_spacing(points)
    resampled = get_resample_points(points, S)
    return resampled

                
if __name__ == '__main__':
    points = [[1, 1], [1, 4], [1, 6], [1, 11], [4, 11], [5, 11], [11, 11], [11, 5], [11, 1], [1, 1]]
    
    resampled = interpolation(points)
    for point in resampled:
        print('%6.2f, %6.2f'%(point[0], point[1]))
