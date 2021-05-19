import glfw
from Input import Input

from OpenGL.GL import glViewport

class Window:
    def __init__(self, width, height, caption):
        
        self.width = width
        self.height = height

        # Initialize the library
        glfw.init()

        # Create a windowed mode window and its OpenGL context
        self.window = glfw.create_window(width, height, caption, None, None)
        if not self.window:
            glfw.terminate()

        self.configureCallbacks()
        self.initializeInput()

        glfw.make_context_current(self.window)

    def configureCallbacks(self):

        glfw.set_key_callback(self.window, self.onKeyboardEvent)
        glfw.set_framebuffer_size_callback(self.window, self.onWindowResize)

    def initializeInput(self):
        Input.init()
        
    # Window related callbacks

    def onWindowResize(self, window, width, height):
        glViewport(0,0, width, height)

    # Input related callbacks

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
