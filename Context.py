from Input import Input

# Context
    # • init
    # • use     activates a context with a given name, if no name is specified, the context instance itself is activated

class Context:
    def __init__(self, name, active):

        self.name = name
        Input.add(self)

        if active: self.use()

    def __del__(self):

        Input.remove(self)

    def setup(self, target):
        
        self.target = target

    def use(self, name=None):

        Input.bind(name) if name else Input.bind(self.name)
            

# Functions implementing key actions should contain:
# 1. an action:
# press or release    e.g pressKeyA or releaseKeyA

# 2. an identifier:
# KeyA ... KeyZ  For alphabetic keys    e.g pressKeyA(self, mods)
# Num0 ... Num9  For Numpad keys        e.g pressNum0(self, mods)
# Key0 ... Key9                         e.g pressKey0(self, mods)
# Enter, Esc, Space