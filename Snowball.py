from Window import Window

class Snowball:

    def __init__(self):
        self.active = True
        
    def setup(self):
        pass

    def loop(self, dt):
        pass

    def finish(self):
        pass

    def __call__(self):
        window = Window(640,480,"Untitled")
        
        self.setup()

        while not window.shouldClose():

            if self.active:
                self.loop(0)

            window.finalizeLoop()

        self.finish()