from stl import mesh


class stlInput:

    def __init__(self):
        self.normals = None
        self.x = None
        self.y = None
        self.z = None
        self.volume = None
        self.cog = None
        self.inertia = None

    def importSTL(self, stlFile):
        file = mesh.Mesh.from_file(stlFile)
        self.normals = file.normals
        self.volume, self.cog, self.inertia = file.get_mass_properties()
        self.x = file.v0
        self.y = file.v1
        self.z = file.v2
        return self
