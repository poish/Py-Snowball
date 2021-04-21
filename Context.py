from Input import Input

class Context:
    def __init__(self, name):
        self.name = name
        Input.add(self)
    
    def pressKeyA(self, mods):
        print(f"Context {self.name}: key A was pressed")
    
    def use(self, name=None):
        if name == None:
            Input.use(self.name)
        else:
            Input.use(name)
