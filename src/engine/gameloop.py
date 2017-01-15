from botctl import Botctl

def gameloop(args):
    """
    This is the game loop, it takes the moves, processes it, writes the new
    state to the medium (here pipe).
    """

    bot = [Botctl(i) for i in args]

    while True:
        # moves = [bot[i].get_move() for i in xrange(len(bot))]
        # print moves
        break

    
