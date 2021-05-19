from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_COMPILE_STATUS, GL_LINK_STATUS, \
    glCreateShader, glShaderSource, glCompileShader, glGetShaderiv, glGetShaderInfoLog, \
    glCreateProgram, glAttachShader, glLinkProgram, glGetProgramiv, glGetProgramInfoLog, \
    glDeleteShader, glDeleteProgram, glGetUniformLocation, glUseProgram, glUniform1f

# Shader     
    # • init
    # • del
    # • setUniform1f, setUniform2f, setUniform3f, setUniform4f

class Shader:

    def __init__(self, vertexPath=None, fragmentPath=None):
        
        if vertexPath and fragmentPath:
            source = ShaderSource(vertexPath, fragmentPath)
            self.id = source.createProgram()

            print(f"vertex status: {source.status[GL_VERTEX_SHADER]}")
            print(f"fragment status: {source.status[GL_FRAGMENT_SHADER]}")
            print(f"link status: {source.status[GL_LINK_STATUS]}")

    def __del__(self):

        glDeleteProgram(id)

    def use(self):

        glUseProgram(self.id)

    def setUniform1f(self, name, value):
        
        location = glGetUniformLocation(self.id, name)
        glUniform1f(location, value)


# ShaderSource      
    # • init    
    # • createShader
    # • createProgram

class ShaderSource:

    def __init__(self, vertexPath, fragmentPath):
        vertexFile = open(vertexPath)
        fragmentFile = open(fragmentPath)

        self.vertexSource = vertexFile.read()
        self.fragmentSource = fragmentFile.read()

        vertexFile.close()
        fragmentFile.close()

        self.status = {
            GL_VERTEX_SHADER: None,
            GL_FRAGMENT_SHADER: None,
            GL_LINK_STATUS: None
        }
        self.infoLog = {
            GL_VERTEX_SHADER: None,
            GL_FRAGMENT_SHADER: None,
            GL_LINK_STATUS: None
        }

    def createShader(self, source, shaderType):

        shader = glCreateShader(shaderType)

        glShaderSource(shader, source, None)
        glCompileShader(shader)

        self.status[shaderType] = glGetShaderiv(shader, GL_COMPILE_STATUS)
        self.infoLog[shaderType] = glGetShaderInfoLog(shader)

        return shader

    def createProgram(self):

        vertexShader = self.createShader(self.vertexSource, GL_VERTEX_SHADER)
        fragmentShader = self.createShader(self.fragmentSource, GL_FRAGMENT_SHADER)

        program = glCreateProgram()
        glAttachShader(program, vertexShader)
        glAttachShader(program, fragmentShader)
        glLinkProgram(program)

        self.status[GL_LINK_STATUS] = glGetProgramiv(program, GL_LINK_STATUS)
        self.infoLog[GL_LINK_STATUS] = glGetProgramInfoLog(program)

        glDeleteShader(vertexShader)
        glDeleteShader(fragmentShader)

        return program
