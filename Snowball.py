from Window import Window

class Snowball:
    def __init__(self):
        self.active = True
    def setup(self):
        pass

    def loop(self):
        pass

    def terminate(self):
        pass

    def run(self):
        window = Window(640,480,"Untitled")
        
        self.setup()

        while not window.shouldClose():

            if self.active:
                self.loop()

            window.finalizeLoop()

        self.terminate()
            
class MyApp(Snowball):
    def setup(self):
        self.a = 5
        self.b = 17
    
    def loop(self):
        pass