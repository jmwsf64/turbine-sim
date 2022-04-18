import random
import numpy as np


class resultsReadWrite:

    def __init__(self):
        self.delimiter = ','
        self.newline = '_'
        self.separator = '/'
        self.header = 'h'
        self.array = 'a'
        self.writeCodec = {'0': b'\xdb', '1': b'\xd8', '2': b'\xd3', '3': b'\x89', '4': b'\x8c', '5': b'\xa3', '6': b'\xd9',
                           '7': b'\xe4', '8': b'\x9f', '9': b'\xee', '.': b'\x85', '-': b'\xb4',
                           'x': b'\xde', 'y': b'\x8b', 'z': b'\xcb', 'u': b'\xa2', 'v': b'\x1b', 'w': b'\x14', 'p': b'\xa1',
                           self.delimiter: b'\xc0', self.newline: b'\xf5', self.separator: b'\x17', self.header: b'\xca', self.array: b'\x1c'}
        self.readCodec = {'db': '0', 'd8': '1', 'd3': '2', '89': '3', '8c': '4', 'a3': '5', 'd9': '6',
                          'e4': '7', '9f': '8', 'ee': '9', '85': '.', 'b4': '-',
                          'de': 'x', '8b': 'y', 'cb': 'z', 'a2': 'u', '1b': 'v', '14': 'w', 'a1': 'p',
                          'c0': self.delimiter, 'f5': self.newline, '17': self.separator, 'ca': self.header, '1c': self.array}

    def writeDataToFile(self, a_x, a_y, a_z, a_u, a_v, a_w, a_p, a_FileName):

        # ================================================================
        # create header string including array order and data scramble key
        # ================================================================

        # --------------------
        # create scramble keys
        # --------------------
        numSheets = a_x.shape[0]
        numRows = a_x.shape[1]
        numCols = a_x.shape[2]
        sheetScramble = list(np.linspace(0, numSheets - 1, numSheets, dtype=np.int32))
        rowScramble = list(np.linspace(0, numRows - 1, numRows, dtype=np.int32))
        colScramble = list(np.linspace(0, numCols - 1, numCols, dtype=np.int32))
        random.shuffle(sheetScramble)
        random.shuffle(rowScramble)
        random.shuffle(colScramble)

        # -----------------------------------------
        # create string of scramble keys for header
        # -----------------------------------------
        headerScramble = ''
        for i in sheetScramble:
            headerScramble += str(i) + self.delimiter
        headerScramble = headerScramble[:-1] + self.separator
        for i in rowScramble:
            headerScramble += str(i) + self.delimiter
        headerScramble = headerScramble[:-1] + self.separator
        for i in colScramble:
            headerScramble += str(i) + self.delimiter
        headerScramble = headerScramble[:-1] + self.header

        # ------------------------------------------------------
        # shuffle array names to create random array write order
        # ------------------------------------------------------
        arrays = ['x', 'y', 'z', 'u', 'v', 'w', 'p']
        random.shuffle(arrays)
        headerArray = self.delimiter.join(arrays) + self.separator
        header = headerArray + headerScramble

        # --------------------------------------
        # convert header string to binary format
        # --------------------------------------
        writeHeader = b''
        for val in list(header):
            writeHeader += self.writeCodec[val]
        writeHeader = bytearray(writeHeader)

        # ===================================================================
        # create data string while scrambling data according to scramble keys
        # ===================================================================

        # ---------------------------------------
        # create a dictionary of the write arrays
        # ---------------------------------------
        dataDict = {'x': a_x, 'y': a_y, 'z': a_z, 'u': a_u, 'v': a_v, 'w': a_w, 'p': a_p}

        # -----------------------------------
        # convert write data to single string
        # -----------------------------------
        writeString = ''
        for key in arrays:
            writeString += key
            for i in sheetScramble:
                for j in rowScramble:
                    for k in colScramble:
                        writeString += str(dataDict[key][i][j][k]) + self.delimiter
                    writeString = writeString[:-1]
                    writeString += self.newline
                writeString = writeString[:-1]
                writeString += self.separator
            writeString = writeString[:-1] + self.array
        writeString = writeString[:-1]

        # ----------------------
        # convert to binary data
        # ----------------------
        writeData = b''
        for val in list(writeString):
            writeData += self.writeCodec[val]
        writeData = bytearray(writeData)

        # ===================================================
        # create full byte array and write to the output file
        # ===================================================

        # ------------------------------
        # combine header and data arrays
        # ------------------------------
        writeFile = writeHeader + writeData

        # ----------------------------------------
        # delete dictionary of data to save memory
        # ----------------------------------------
        dataDict.clear()

        # ---------------------
        # write the output file
        # ---------------------
        outfile = open(a_FileName, 'wb')
        outfile.write(writeFile)
        outfile.close()

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
            readData += self.readCodec[val]

        # --------------------------------
        # split into header and array data
        # --------------------------------
        readData = readData.split('h')
        header = readData[0]
        dataArrays = readData[1].split(self.array)

        # ===========================================
        # read the header and create necessary arrays
        # ===========================================

        # ----------------------------
        # read order of arrays in file
        # ----------------------------
        headerData = header.split(self.separator)

        # ------------------
        # read scramble keys
        # ------------------
        sheetOrder = headerData[1].split(self.delimiter)
        rowOrder = headerData[2].split(self.delimiter)
        colOrder = headerData[3].split(self.delimiter)

        # ===========================================
        # read the data into the corresponding arrays
        # ===========================================

        # --------------------------------
        # convert read data to numpy array
        # --------------------------------
        dataDict = {}
        for arr in dataArrays:
            arrayID = arr[0]
            sheetData = arr[1:].split(self.separator)
            arraySheets = []
            for sheet in sheetData:
                rowData = sheet.split(self.newline)
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
