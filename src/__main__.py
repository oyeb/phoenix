from engine.gameloop import gameloop

if __name__ == "__main__":
    print "="*80
    print "Starting Engine".center(80)
    print "="*80    

    gameloop([['/usr/bin/python', 'python', '/home/homonculus/Code/Projects/phoenix/bots/bot1.py']])
