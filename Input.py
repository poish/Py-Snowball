import json
import glfw



class Input:

    currentContext = None
    keys = {}
    names = {}
    @staticmethod
    def init():

        Input.currentContext = context()
        source = open("Py-Snowball/glfwKeyCodes.json")

        data = json.load(source)
        Input.keys = data["codes"]
        Input.names = data["names"]

    @staticmethod
    def onMouseButtonEvent(self):
        pass

    @staticmethod
    def onMouseMoveEvent(self):
        pass

    @staticmethod
    def onKeyboardEvent(key, scancode, action, mods):

        name = f"press{Input.names[str(key)]}"

        if action == glfw.PRESS:
            if hasattr(Input.currentContext, name):
                function = getattr(Input.currentContext, name)
                function()
            else:
                print("not found")

class context:
    def pressKeyA(self):
        print("Key A was pressed")