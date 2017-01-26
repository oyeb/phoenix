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

    bots_config_dir = os.path.dirname(os.path.realpath('__file__'))
    a = open(os.path.join(bots_config_dir, "bots_config.json"), 'r')
    bot_start_config = map(loads, a.read().strip().split('\n'))

    gameloop(bot_start_config)
