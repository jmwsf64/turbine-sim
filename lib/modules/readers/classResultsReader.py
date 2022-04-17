import sys, json
import numpy as np


class resultsReader:

    def __init__(self):
        self.delimiter = ','
        self.newline   = '_'
        self.separator = '/'
        self.header    = 'h'
        self.array     = 'a'
        self.codec = {'db': '0', 'd8': '1', 'd3': '2', '89': '3', '8c': '4', 'a3': '5', 'd9': '6',
                      'e4': '7', '9f': '8', 'ee': '9', '85': '.', 'b4': '-',
                      'de': 'x', '8b': 'y', 'cb': 'z', 'a2': 'u', '1b': 'v', '14': 'w', 'a1': 'p',
                      'c0': self.delimiter, 'f5': self.newline, '17': self.separator, 'ca': self.header, '1c': self.array}

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
        headerData = header.split(self.separator)
        # arrayOrder = headerData[0].split(self.delimiter)

        # ------------------
        # read scramble keys
        # ------------------
        sheetOrder = headerData[1].split(self.delimiter)
        rowOrder   = headerData[2].split(self.delimiter)
        colOrder   = headerData[3].split(self.delimiter)

        # ===========================================
        # read the data into the corresponding arrays
        # ===========================================

        # --------------------------------
        # convert read data to numpy array
        # --------------------------------
        dataDict = {}
        for arr in dataArrays:
            arrayID     = arr[0]
            sheetData   = arr[1:].split(self.separator)
            arraySheets = []
            for sheet in sheetData:
                rowData   = sheet.split(self.newline)
                sheetRows = []
                for row in rowData:
                    sheetRows.append(row.split(self.delimiter))
                arraySheets.append(sheetRows)
            dataDict[arrayID] = np.array(arraySheets, dtype=np.float64)

        # ----------------------
        # unscramble data arrays
        # ----------------------
        dataDims = dataDict['x'].shape
        for arr in dataDict.keys():
            tempArr = np.zeros(dataDims)
            ind0 = 0
            for i in sheetOrder:
                ind1 = 0
                for j in rowOrder:
                    ind2 = 0
                    for k in colOrder:
                        tempArr[int(i), int(j), int(k)] = dataDict[arr][ind0, ind1, ind2]
                        ind2 += 1
                    ind1 += 1
                ind0 += 1
            dataDict[arr] = tempArr
        del tempArr

        # -----------
        # return data
        # -----------
        return dataDict['x'], dataDict['y'], dataDict['z'], dataDict['u'], dataDict['v'], dataDict['w'], dataDict['p']
