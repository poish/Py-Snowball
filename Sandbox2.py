from Snowball import Snowball

from Shader import Shader

import numpy as np
from OpenGL.GL import *

from MoveTool import Move

from SceneObject import OpenGLObject
class Square:

    def __init__(self):

        self.x = 0
        self.y = 0
    
    def moveLeft(self):

        self.x -= 0.1

    def moveRight(self):

        self.x += 0.1

    def moveUp(self):

        self.y += 0.1

    def moveDown(self):

        self.y -= 0.1



class myApp(Snowball):

    def setup(self):

        self.vertices = [ 0.5, 0.5, 0.0, -0.5, 0.5, 0.0, -0.5, -0.5, 0.0, 0.5, -0.5, 0.0 ]
        self.elements = [ 0, 1, 2, 0, 2, 3 ]

        #self.vao = glGenVertexArrays(1)
        #self.vbo = glGenBuffers(1)
        #self.ebo = glGenBuffers(1)

        self.shader = Shader("vertex.vs", "fragment.fs")

        #sglBindVertexArray(self.vao)

        #glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        #glBufferData(GL_ARRAY_BUFFER, 12*4, np.array(self.vertices, dtype="float32"), GL_STATIC_DRAW)

        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        #glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6*4, np.array(self.elements, dtype="uint32"), GL_STATIC_DRAW)

        #glVertexAttribPointer(0, 3, GL_FLOAT, False, 3 * 4, None)
        #glEnableVertexAttribArray(0)

        #glBindBuffer(GL_ARRAY_BUFFER, 0)
        #glBindVertexArray(0)

        #glDisable(GL_CULL_FACE)

        self.object = OpenGLObject("box")

        self.object.vbo.data = self.vertices
        self.object.ebo.data = self.elements

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

