import json
import glfw

class Input:

    currentContext = None

    contexts = {}

    keys = {}
    names = {}

    actions = ["release", "press"]

    @staticmethod
    def init():

        source = open("glfwKeyCodes.json")
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

        name = f"{Input.actions[action]}{Input.names[str(key)]}"

        if hasattr(Input.currentContext, name):
            function = getattr(Input.currentContext, name)
            function(mods)
        else:
            print("not found")         

    @staticmethod
    def add(context):
        Input.contexts[context.name] = context

    @staticmethod
    def use(name):
        Input.currentContext = Input.contexts[name]

print(glfw.RELEASE)