class Scene:
    def __init__(self, name):
        pass

    def add(self, object): # Object might be a scene object, light or a camera
        pass
    
    def get(self, name):
        pass

    def remove(self, name):
        pass

    def draw(self, target=None):
        # for all scene objects set up textures, projections, uniforms, shaders 
        # execute draw calls
        # if target is None, draw to screenBuffer otherwise draw to the named Layer
        pass
