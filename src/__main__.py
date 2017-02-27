# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with this source code.

from engine.gameloop import setup_arena, gameloop, check_config, commit
from json import loads
import os

if __name__ == "__main__":
    print "="*80
    print "Starting Engine".center(80)
    print "="*80

    cdir = os.path.dirname(os.path.realpath('__file__'))
    config_file = open(os.path.join(cdir, "config.json"), 'r')
    game_config = loads(config_file.read().strip())
    
    check_config(
        game_config['bots'],
        game_config['map'],
        game_config['arena'],
        game_config['commit_paths'],
        game_config['api_dir']
    )
    setup_arena(
        game_config['arena'],
        game_config['bots'],
        game_config['api_dir']
    )

    summary = gameloop(
        game_config['bots'],
        game_config['map'],
        game_config['timeout'],
        game_config['max_iters'],
        game_config['arena'],
        game_config['commit_paths'],
        game_config['filenames']
    )

    print '='*80
    print 'Game Summary'.center(80)
    print '='*80
    print summary