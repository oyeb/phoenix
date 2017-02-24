from math import sqrt, radians, sin, cos

def map_restriction((newx, newy)):
    '''
    Containing the movement within the walls of the map, here half the cell can be
    outside the map
    '''
    
    if newx > 4992:
        newx = 4992
    if newx < 0:
        newx = 0
    if newy > 2808:
        newy = 2808
    if newy < 0:
        newy = 0
        
    return (newx, newy)

def update_position(tick_time, bot):
    newx = bot['center'][0] + bot['velocity']*tick_time*cos(radians(bot['angle']))
    newy = bot['center'][1] + bot['velocity']*tick_time*sin(radians(bot['angle']))

    bot['center'] = map_restriction((newx, newy))    

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
    precision is 0.01
    """
    
    lx1, ly1 = line_init_pt
    lx2, ly2 = line_end_pt
    x, y = pt
    return (max(lx1, lx2)+0.01 >= x >= min(lx1, lx2)-0.01) and (max(ly1, ly2)+0.01 >= y >= min(ly1, ly2)-0.01)

def collision_bot_static_entity(bot, entity, rad):
    '''
    Checks collision with static objects such as food and viruses. rad = 2 for food,
    rad = 35 for virus. entity is of the form (x, y)
    '''
    
    init = bot['center']
    update_position(20.0, bot)
    end = bot['center']
    d = closest_point_on_line(init, end, entity)

    # Trigonometry
    if ((point_on_lsegment(init, end, d) and dist(d, entity) <= bot['radius']) or
        (dist(init, entity) <= bot['radius']) or
        (dist(end, entity) <= bot['radius'])) and bot['radius'] >= 1.8*rad:
        
        time_coll = (dist(init, d) - sqrt(bot['radius']**2 - dist(d, entity)**2))/bot['velocity']
        print "[*] Event: bot ate a food or virus"
        return (True, time_coll)
    else:
        return (False, None)

def collision_bots_dynamic(bota, botb):
    '''
    Bota is stationary wrt Botb and we take relative velocities
    '''
    
    bota, botb = (bota, botb) if bota['radius'] >= botb['radius'] else (botb, bota)

    vela, velb = bota['velocity'], botb['velocity']
    anga, angb = bota['angle'], botb['angle']
    
    vx = velb*cos(radians(angb)) - vela*cos(radians(anga))
    vy = velb*sin(radians(angb)) - velb*sin(radians(anga))

    init = botb['center']
    end = map_restriction((botb['center'][0]+vx*20, botb['center'][1]+vy*20))
    d = closest_point_on_line(init, end, bota['center'])
    
    if ((point_on_lsegment(init, end, d) and dist(d, bota['center']) <= botb['radius']) or
        (dist(init, bota['center']) <= bota['radius']) or
        (dist(end, bota['center']) <= bota['radius'])) and bota['radius'] >= 1.8*botb['radius']:
        
        time_coll = (dist(init, d) - sqrt(botb['radius']**2 - dist(d, bota['radius'])**2))/sqrt(vx**2 + vy**2)
        print "[*] Event: bot another bot"
        return (True, time_coll)
    else:
        return (False, None)
