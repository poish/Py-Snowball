from Context import Context

class Move(Context):

    def pressKeyA(self, mods):
        self.target.moveLeft()

    def pressKeyD(self, mods):
        self.target.moveRight()

    def pressKeyW(self, mods):
        self.target.moveUp()

    def pressKeyS(self, mods):
        self.target.moveDown()      
