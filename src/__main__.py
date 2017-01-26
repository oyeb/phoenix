# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with is source code.

from engine.gameloop import gameloop
from json import loads
import os

if __name__ == "__main__":
    print "="*80
    print "Starting Engine".center(80)
    print "="*80

    cdir = os.path.dirname(os.path.realpath('__file__'))
    a = open(os.path.join(cdir, "bots_config.json"), 'r')
    bot_start_config = map(loads, a.read().strip().split('\n'))

    b = open(os.path.join(cdir, "map_config.json"), 'r')
    map_text = open(loads(b.read().strip()), 'r').read()

    gameloop(bot_start_config, map_text)
