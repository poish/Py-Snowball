from Snowball import Snowball
from Context import Context
from Shader import Shader

import numpy as np
from OpenGL.GL import *

class Move(Context):

    def pressKeyA(self, mods):
        self.target.moveLeft()

    def pressKeyD(self, mods):
        self.target.moveRight()

    def pressKeyW(self, mods):
        self.target.moveUp()

    def pressKeyS(self, mods):
        self.target.moveDown()      

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

        self.vertices = np.array([ 0.5, 0.5, 0.0, -0.5, 0.5, 0.0, -0.5, -0.5, 0.0, 0.5, -0.5, 0.0 ], dtype="float32")
        self.elements = np.array([ 0, 1, 2, 0, 2, 3 ], dtype="uint32")

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        self.shader = Shader("vertex.vs", "fragment.fs")

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, 12*4, self.vertices, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6*4, self.elements, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 3 * 4, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        glDisable(GL_CULL_FACE)

        self.sq = Square()

        self.mb = Move("moveContext", True)
        self.mb.setup(self.sq)

    def loop(self):

        glClearColor(0.2, 0.3, 0.8, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        self.shader.use()
        self.shader.setUniform1f("offsetX", self.sq.x)
        self.shader.setUniform1f("offsetY", self.sq.y)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)


m = myApp()
m.run()

