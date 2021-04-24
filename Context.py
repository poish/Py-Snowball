from Input import Input

class Context:
    def __init__(self, name):
        self.name = name
        Input.add(self)

    def use(self, name=None):
        if name == None:
            Input.use(self.name)
        else:
            Input.use(name)

# Functions implementing key actions should contain:
# 1. an action:
# press or release    e.g pressKeyA or releaseKeyA

# 2. an identifier:
# KeyA ... KeyZ  For alphabetic keys    e.g pressKeyA(self, mods)
# Num0 ... Num9  For Numpad keys        e.g pressNum0(self, mods)
# Key0 ... Key9                         e.g pressKey0(self, mods)
# Enter, Esc, Space