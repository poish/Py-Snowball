from OpenGL.GL import *
import numpy as np
class Buffer:
    
    def __init__(self):

        self.id = glGenBuffers(1)
        self.data = None

    def __del__(self):

        glDeleteBuffers(self.id)
    
    def __call__(self):
        
        return self.id

    def count(self):

        return len(self.data)
    
    def size(self):

        return 4 * len(self.data)


class OpenGLObject:

    def __init__(self, name):
        self.name = name
        self.vao = glGenVertexArrays(1)
        self.vbo = Buffer()
        self.ebo = Buffer()

    def loadData(self):

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo())
        glBufferData(GL_ARRAY_BUFFER, self.vbo.size(), np.array(self.vbo.data, dtype="float32"), GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo())
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.ebo.size(), np.array(self.ebo.data, dtype="uint32"), GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 3 * 4, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        #glDisable(GL_CULL_FACE)

    def draw(self):

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.ebo.count(), GL_UNSIGNED_INT, None)
