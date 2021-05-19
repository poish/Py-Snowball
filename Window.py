from OpenGL.raw.GL.VERSION.GL_1_0 import glLineWidth
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
        glfw.set_mouse_button_callback(self.window, self.onMouseButtonEvent)
        glfw.set_cursor_pos_callback(self.window, self.onMouseMoveEvent)
        glfw.set_framebuffer_size_callback(self.window, self.onWindowResize)

    def initializeInput(self):

        Input.init()
        
    # Window related callbacks

    def onWindowResize(self, window, width, height):
        self.width = width
        self.height = height
        glViewport(0,0, width, height)

    # Input related callbacks

    def onKeyboardEvent(self, window, key, scancode, action, mods):
        Input.onKeyboardEvent(key, scancode, action, mods)

    def onMouseMoveEvent(self, window, x, y):

        uniform_x = x / self.width
        uniform_y = y / self.height

        #Input.onMouseMoveEvent(uniform_x, uniform_y)
    #
    def onMouseButtonEvent(self, window, button, action, mods):

        Input.onMouseButtonEvent(button, action, mods)

    # state flags

    def shouldClose(self):
        
        return glfw.window_should_close(self.window)

    # auxiliary functions

    def finalizeLoop(self):
        glfw.swap_buffers(self.window)
        glfw.poll_events()
