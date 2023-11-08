#!/usr/bin/env python3
import sys
import argparse
from asciimatics.effects import Print
from asciimatics.renderers.figlettext import FigletText
from asciimatics.renderers.box import Box
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

from maintitle import MainMenuView
from memberlist import MemberListView, MemberView
from accountlist import AccountListView, AccountAddView, AccountEditView, TransmitView
from database import ContinentalModel, memoryContinentalModel


def john(screen):
    scenes = []

    # Title
    effects = [
        Print(screen,
              Box(screen.width, screen.height, uni=screen.unicode_aware),
              0, 0,
              colour=Screen.COLOUR_GREEN,
              bg=Screen.COLOUR_BLACK,
              ),
        Print(screen,
              FigletText("CONTIN", "slant"),
              y=3, x=1,
              colour=Screen.COLOUR_GREEN,
              bg=Screen.COLOUR_BLACK,
              ),
        Print(screen,
              FigletText("ENTAL", "slant"),
              y=8, x=7,
              colour=Screen.COLOUR_GREEN,
              bg=Screen.COLOUR_BLACK,
              ),
        Print(screen,
            FigletText("PRESS X KEY", "term"),
            y=18, x=15,
            colour=Screen.COLOUR_GREEN,
            bg=Screen.COLOUR_BLACK,
            ),
    ]
    scenes.append(Scene(effects, 0))

    screen.clear()
    screen.refresh()
    screen.play(scenes, stop_on_resize=True)

def wick(screen, scene):
    scenes = [
        Scene([MainMenuView(screen, contacts)], -1, name="Main"),
        Scene([MemberListView(screen, contacts)], -1, name="Member List"),
        Scene([MemberView(screen, contacts)], -1, name="Edit Member"),
        Scene([AccountListView(screen, contacts)], -1, name="Account List"),
        Scene([AccountAddView(screen, contacts)], -1, name="Add Account"),
        Scene([AccountEditView(screen, contacts)], -1, name="Edit Account"),
        Scene([TransmitView(screen, contacts)], -1, name="Transmit")
    ]

    screen.clear()
    screen.refresh()
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

def main():
    last_scene = None

    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--dbfile',
                        action='store_true',
                        default=False,
                        help='The database file to be opened')
    parser.add_argument('-m',
                        '--memory',
                        action='store_true',
                        default=True,
                        help='The database might be stored in memory')

    args = parser.parse_args()

    global contacts
    if args.dbfile:
        contacts = ContinentalModel()
    elif args.memory:
        contacts = memoryContinentalModel()

    while True:
        try:
            Screen.wrapper(john, catch_interrupt=True)
            Screen.wrapper(wick, catch_interrupt=False, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene

if __name__ == '__main__':
    main()