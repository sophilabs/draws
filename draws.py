import curses
import sys
import random
import csv


class Draw(object):

    def __init__(self, filename):
        with open(filename) as input:
            self.users = [row for row in csv.DictReader(input)]

    def loop(self):
        print sys.stdin.readline()

if __name__ == '__main__':
    Draw(sys.argv[1]).loop()
