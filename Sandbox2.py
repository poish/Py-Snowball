from Snowball import Snowball
from Context import Context
from Shader import ShaderSource
from OpenGL.GL import GL_VERTEX_SHADER

class cameraControl(Context):
    def pressKeyW(self, mods):
        print("up")

    def pressKeyA(self, mods):
        print("left")

    def pressKeyS(self, mods):
        print("down")

    def pressKeyD(self, mods):
        print("right")

class myApp(Snowball):
    def setup(self):

        vc = cameraControl("viewControl")
        vc.use()
        
        s = ShaderSource("vertex.vs", "fragment.fs")
        s.createShader(s.vertexSource, GL_VERTEX_SHADER)

    def loop(self):
        pass



m = myApp()
m.run()

