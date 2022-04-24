import numpy as np


class meshCreator:

    def __init__(self, a_CaseID):
        self.caseID         = a_CaseID
        self.fileExtension  = '.mspnsm'
        self.boundaryPoints = None
        self.interiorPoints = None
        self.meshFacets     = None
        self.meshPoints     = None
        self.readCodec      = {}
        self.writeCodec     = {}

    def compileBoundaryPoints(self):
        self.boundaryPoints = np.array([])

    def createAdditionalExteriorPoints(self):
        self.interiorPoints = np.array([])

    def generateMesh(self):
        self.meshPoints = np.array([])
        self.meshFacets = np.array([])

    def writeMesh(self, mesh):
        self.writeCodec = {}

    def readMesh(self):
        self.readCodec = {}
