class simConfiguration:

    def __init__(self, a_CaseID):
        self.caseID          = a_CaseID
        self.compressibility = None
        self.turbulenceModel = None
        self.writeCodec = {'i': b'\x01', 'L': b'\x02'}
        self.readCodec  = {'01': 'i', '02': 'L'}

    def writeConfigurationToFile(self):
        compress  = bytearray(self.writeCodec[self.compressibility])
        turbModel = bytearray(self.writeCodec[self.turbulenceModel])

    def readConfigurationFromFile(self):
        compress  = 'i'
        turbModel = 'L'
        self.compressibility = compress
        self.turbulenceModel = turbModel
