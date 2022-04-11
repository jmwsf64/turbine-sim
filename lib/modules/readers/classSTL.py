from stl import mesh


class stlInput:

    def __init__(self):
        self.normals = None
        self.v0 = None
        self.v1 = None
        self.v2 = None
        self.volume = None
        self.cog = None
        self.inertia = None

    def importSTL(self, stlFile):
        file = mesh.Mesh.from_file(stlFile)
        self.normals = file.normals
        self.volume, self.cog, self.inertia = file.get_mass_properties()
        self.v0 = file.v0
        self.v1 = file.v1
        self.v2 = file.v2
        return self
