#!/usr/bin/env python
import os
import sys

if sys.version_info[0] > 3:
    print("This game runs on python 3 only")


from RumbleLib import board

# initialize
game = board.Board()

"""
# Choose display method
if len(sys.argv) > 1:
    if sys.argv[1] in ('--console', '-c'):
        from RumbleLib.gui_console import display
        display(game)
        exit(0)
    elif sys.argv[1] in ('--help', '-h'):
        print ('''Usage: game.py [OPTION]\n\n\tPlay a game of chess\n\n\tOptions:\n\t -c, --console\tplay in console mode\n\n''')
        exit(0)

try:
    from RumbleLib.gui_tkinter import display
except ImportError:
    from RumbleLib.gui_console import display
finally:
    display(game)
"""