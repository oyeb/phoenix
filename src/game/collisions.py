from math import abs, sqrt

def closest_point_on_line(line_init_pt, line_end_pt, sep_pt):
    lx1, ly1 = line_init_pt
    lx2, ly2 = line_end_pt
    x, y = sep_pt

    A1 = ly2 - ly1
    B1 = lx1 - lx2

    C1 = (ly2 - ly1)*lx1 + (lx1 - lx2)*ly1
    C2 = -B1*x + A1*y

    det = A1**2 + B1**2

    if(det != 0):
        cx = (A1*C1 - B1*C2)/det
        cy = (A1*C2 + B1*C1)/det
    else:
        cx = x
        cy = y

    return (x, y)

def dist(i, j):
    x1, y1 = i
    x2, y2 = j
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def check_collision_bots(bota, botb):
    return dist(bota['center'], botb['center']) <= max(bota['radius'], botb[radius])

