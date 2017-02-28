# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with this source code.

from engine.gameloop import setup_arena, gameloop, check_config, commit
from json import loads
import os, argparse

if __name__ == "__main__":
    print "="*80
    print "Starting Engine".center(80)
    print "="*80

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest='cfile', type=str, default=None)
    args = parser.parse_args()
    
    cdir = os.path.dirname(os.path.realpath('__file__'))
    if args.cfile is None:
        args.cfile = os.path.abspath(os.path.join(cdir, "config.json"))
    config_file = open(args.cfile, 'r')
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

    gameloop(
        game_config['bots'],
        game_config['map'],
        game_config['timeout'],
        game_config['max_iters'],
        game_config['arena'],
        game_config['commit_paths'],
        game_config['filenames'],
        game_config['move_schema']
    )

    print '='*80
    print 'Game Over'.center(80)
    print '='*80
