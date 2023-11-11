import pickle

class MapMeneger():
    def __init__(self):
        self.startNew()
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0, 1),
            (0.7, 0.2, 0.35, 1),
            (0.4, 0.5, 0.4, 1),
            (0.35, 0.2, 0.2, 1),
            (0.5, 0.3, 0, 1),
            (0.60, 0.2, 0.7, 1),
        ]

    def getColor(self, z):
        if z < 9:
            return self.colors[z]
        else: 
            return self.colors[9] 

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position, texture):
        model = loader.loadModel("models/block/block.egg")
        texture = loader.loadTexture(f"models/block/{texture}.png")
        model.setTexture(texture)
        model.setPos(position)
        color = self.getColor(position[2])
        model.setColor(color)

        model.setTag("at", str(position))

        model.reparentTo(self.land)

    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
           block.removeNode()

    def delBlockFrom(self, pos):
        x,y,z = self.findHighestEmpty(pos)
        pos = x,y,z-1
        blocks = self.findBlocks(pos)
        for block in blocks:
           block.removeNode()

    def buildBlock(self, pos):
        x, y, z = pos
        new_pos = self.findHighestEmpty(pos)
        if new_pos[2] <= z + 1:
            self.addBlock(new_pos, 'block')


    def loadLand(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
            
                line = line.split(" ")
                x = 0
                for z in line:
                    if z != "\n":
                        for z0 in range(int(z)+1):
                            self.addBlock((int(x), int(y),int(z0)), 'block' )
                        x+=1
                y+=1

    def saveMap(self):
        blocks = self.land.getChildren()
        with open('map.dat',"wb") as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadMap(self):
        self.clear()
        with open('map.dat', "rb") as file:
            lenght = pickle.load(file)
            
            for i in range(lenght):
                pos = pickle.load(file)
                self.addBlock(pos, 'block')


    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        
    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1

        while not self.isEmpty((x,y,z)):
            z += 1

        return (x, y, z)