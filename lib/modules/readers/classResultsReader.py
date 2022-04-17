import sys
import numpy as np


class resultsReader:

    def __init__(self):
        self.delimiter = ','
        self.newline   = '_'
        self.separator = '/'
        self.header    = 'h'
        self.array     = 'a'
        self.codec = {'db': '0', 'd8': '1', 'xd3': '2', '21': '3', '8c': '4', 'a3': '5', 'd9': '6',
                      'e4': '7', '9f': '8', 'ee': '9', '85': '.', '56': '-',
                      '2e': 'x', '8b': 'y', 'cb': 'z', 'a2': 'u', '3a': 'v', '14': 'w', 'a1': 'p',
                      'c0': self.delimiter, '42': self.newline, '8f': self.separator, '4d': self.header, '1c': self.array}

    def readDataFromFile(self, a_FileName):

        # =================================================
        # read the file and convert to code readable format
        # =================================================

        # ---------------
        # read a_FileName
        # ---------------
        with open(a_FileName, 'rb') as outfile:
            data = outfile.read()
        data = str(data)[2:-1].replace('\\n', '').replace('\\t', '').replace('\\r', '').split('\\x')[1:]

        # -------------------------------
        # convert to code readable format
        # -------------------------------
        readData = ''
        for val in data:
            readData += self.codec[val]

        # --------------------------------
        # split into header and array data
        # --------------------------------
        readData   = readData.split('h')
        header     = readData[0]
        dataArrays = readData[1].split(self.array)

        # ===========================================
        # read the header and create necessary arrays
        # ===========================================

        # ----------------------------
        # read order of arrays in file
        # ----------------------------

        # ------------------
        # read scramble keys
        # ------------------

        # =====================================
        # read the data into the correct arrays
        # =====================================

        # --------------------------------
        # convert read data to numpy array
        # --------------------------------
        '''
        need to think through this one more and determine the proper loop structure - first attempt would have been wrong
        '''
        dataDict = {}

        # ----------------------
        # unscramble data arrays
        # ----------------------

        # -----------
        # return data
        # -----------
        # return dataDict['x'], dataDict['y'], dataDict['z'], dataDict['u'], dataDict['v'], dataDict['w'], dataDict['p']
