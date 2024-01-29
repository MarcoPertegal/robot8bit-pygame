from player import *
from sprites import *


def build_map(self, tilemap):
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            Ground(self, j, i)
            if column == "P":
                self.Player = Player(self, j, i)
            if column == 'W':
                Wall(self, j, i)
            if column == 'L':
                Lava(self, j, i)