from Snowball import Snowball

from Shader import Shader

import numpy as np
from OpenGL.GL import *

from SceneObject import OpenGLObject


class myApp(Snowball):

    def setup(self):

        self.shader = Shader("vertex.vs", "fragment.fs")

        self.object = OpenGLObject("box")

        self.object.vbo.data = [ 0.5, 0.5, 0.0, -0.5, 0.5, 0.0, -0.5, -0.5, 0.0, 0.5, -0.5, 0.0 ]
        self.object.ebo.data = [ 0, 1, 2, 0, 2, 3 ]

        self.object.loadData()

    def loop(self, dt):

        glClearColor(0.2, 0.3, 0.8, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        self.shader.use()
        #glBindVertexArray(self.vao)
        #glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
        self.object.draw()


m = myApp()

m()

