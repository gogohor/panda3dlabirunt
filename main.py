from direct.showbase.ShowBase import ShowBase
from mapmaneger import MapMeneger
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapMeneger()
        self.land.loadLand("map2.txt")
        self.hero = Hero((0,0,1), self.land)
        


game = Game()
game.run()
