from enum import Enum


class GameState(Enum):
    MENU = 0
    BATTLE = 1
    OPEN_WORLD = 2
    ENDED = 3
