import json

# Input
    # • init
    # • onMouseButtonEvent
    # • onMouseMoveEvent
    # • onKeyboardEvent
    # • add
    # • bind
    # • unbind
    # • remove


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

        signature = str(key)
        name = f"{Input.actions[action]}{Input.names[signature]}"

        if hasattr(Input.currentContext, name):

            function = getattr(Input.currentContext, name)
            function(mods)

        else:

            print("not found")         

    @staticmethod
    def add(context):

        Input.contexts[context.name] = context

    @staticmethod
    def bind(name):

        Input.currentContext = Input.contexts[name]

    @staticmethod
    def unbind():

        Input.currentContext = None

    @staticmethod
    def remove(context):

        name = context.name

        if Input.currentContext.name == name: Input.unbind()
        
        Input.contexts[name] = None

    