from wall import Wall
from maze import Maze


def generate(width, height):
    maze = Maze(width, height)

    # TODO Generate a maze using the backtrack algorithm.

    return maze



LEVEL1 = [
    Wall((200, 200), (350, 200)),
    Wall((450, 200), (600, 200)),
    Wall((200, 200), (200, 300)),
    Wall((600, 200), (600, 300)),
    Wall((200, 300), (600, 300)),
    Wall((200, 300), (200, 500)),
    Wall((200, 500), (200, 600)),
    Wall((600, 300), (600, 600)),
    Wall((200, 600), (350, 600)),
    Wall((450, 600), (600, 600)),
    Wall((350, 600), (200, 500))]


LEVEL2 = [
    Wall((200, 100), (300, 100)),
    Wall((300, 100), (300, 200)),
    Wall((300, 200), (200, 200)),
    Wall((200, 200), (200, 100)),
    Wall((200, 200), (200, 300)),
    Wall((200, 300), (100, 300)),
    Wall((100, 300), (100, 200)),
    Wall((100, 200), (200, 200)),
    Wall((400, 300), (600, 300)),
    Wall((600, 300), (600, 400)),
    Wall((600, 400), (400, 400)),
    Wall((400, 400), (400, 300))]