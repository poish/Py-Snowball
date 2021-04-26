import glfw
from Input import Input

class Window:
    def __init__(self, width, height, caption):
        
        # Initialize the library
        glfw.init()

        # Create a windowed mode window and its OpenGL context
        self.window = glfw.create_window(width, height, caption, None, None)
        if not self.window:
            glfw.terminate()

        self.initializeInput()
        glfw.make_context_current(self.window)

    def initializeInput(self):
        Input.init()
        
        glfw.set_key_callback(self.window, self.onKeyboardEvent)

    def onKeyboardEvent(self, window, key, scancode, action, mods):
        Input.onKeyboardEvent(key, scancode, action, mods)

    def onMouseMoveEvent(self):
        pass

    def onMouseButtonEvent(self):
        pass

    def shouldClose(self):
        return glfw.window_should_close(self.window)

    def finalizeLoop(self):
        glfw.swap_buffers(self.window)
        glfw.poll_events()
    
    def terminate(self):
        glfw.terminate()
