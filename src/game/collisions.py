from math import sqrt

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

    return (cx, cy)

def dist(i, j):
    x1, y1 = i
    x2, y2 = j
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def point_on_lsegment(line_init_pt, line_end_pt, pt):
    """
    Can only be used in conjuction with closest_point_on_line()
    """
    
    lx1, ly1 = line_init_pt
    lx2, ly2 = line_end_pt
    x, y = pt
    return (max(lx1, lx2) >= x >= min(lx1, lx2)) and (max(ly1, ly2) >= y >= min(ly1, ly2))
    

def check_collision_bots(bota, botb):
    a, b = (bota['radius'], botb['radius']) if bota['radius'] >= botb['radius'] else (botb['radius']. bota['radius'])
    if a >= 1.8*b:
        return dist(bota['center'], botb['center']) <= a
    else:
        return False

def check_collision_bot_food(bot, food):
    return dist(bot['center'], food) <= bot['radius']
    
def check_collision_bot_virus(bot, virus):
    virusrad = 35
    if bot['radius'] >= 1.8*virusrad:
        return dist(bot['center'], virus) <= bot['radius']
    else:
        return False
