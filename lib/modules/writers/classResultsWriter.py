import random
import numpy as np


class resultsWriter:

    def __init__(self):
        self.delimiter = ','
        self.newline   = '_'
        self.separator = '/'
        self.header    = 'h'
        self.array     = 'a'
        self.codec = {'0': b'\xdb', '1': b'\xd8', '2': b'\xd3', '3': b'\x21', '4': b'\x8c', '5': b'\xa3', '6': b'\xd9',
                      '7': b'\xe4', '8': b'\x9f', '9': b'\xee', '.': b'\x85', '-': b'\x56',
                      'x': b'\x2e', 'y': b'\x8b', 'z': b'\xcb', 'u': b'\xa2', 'v': b'\x3a', 'w': b'\x14', 'p': b'\xa1',
                      self.delimiter: b'\xc0', self.newline: b'\x42', self.separator: b'\x8f', self.header: b'\x4d', self.array: b'\x1c'}

    def writeFileFromData(self, a_x, a_y, a_z, a_u, a_v, a_w, a_p, a_FileName):

        # ================================================================
        # create header string including array order and data scramble key
        # ================================================================

        # --------------------
        # create scramble keys
        # --------------------
        numSheets = a_x.shape[0]
        numRows   = a_x.shape[1]
        numCols   = a_x.shape[2]
        sheetScramble = list(np.linspace(0, numSheets-1, numSheets, dtype=np.int32))
        rowScramble   = list(np.linspace(0, numRows-1,   numRows,   dtype=np.int32))
        colScramble   = list(np.linspace(0, numCols-1,   numCols,   dtype=np.int32))
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
            writeHeader += self.codec[val]
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
            writeData += self.codec[val]
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
