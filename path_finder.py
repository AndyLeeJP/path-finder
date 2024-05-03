import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "O", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "X", "#", "#", "#", "#", "#"]
]

def print_maze(maze, stdscr, path=[]):
    RED = curses.color_pair(1)
    BLUE = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j*2, value, RED)

def start_position(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j


def find_path(maze, stdscr):
    start = "o"
    end = "x"
    start_place = start_position(maze, start)

    q = queue.Queue()
    q.put((start_place, [start_place]))


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
