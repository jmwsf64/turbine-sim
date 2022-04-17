import numpy as np
import lib.modules.readers.classResultsReader as C_RRD
import lib.modules.writers.classResultsWriter as C_RWT

# ===============================
# data to read/write as encrypted
# ===============================

# --------------
# spatial arrays
# --------------
x = np.array([[[0, 1, 2, 3, 4],
               [5, 6, 7, 8, 9]],
              [[10, 11, 12, 13, 14],
               [15, 16, 17, 18, 19]],
              [[20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29]]])
y = np.array([[[0, 1, 2, 3, 4],
               [5, 6, 7, 8, 9]],
              [[10, 11, 12, 13, 14],
               [15, 16, 17, 18, 19]],
              [[20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29]]])
z = np.array([[[0, 1, 2, 3, 4],
               [5, 6, 7, 8, 9]],
              [[10, 11, 12, 13, 14],
               [15, 16, 17, 18, 19]],
              [[20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29]]])

# ---------------
# velocity arrays
# ---------------
# u = np.array([])
# v = np.array([])
# w = np.array([])

# --------------
# pressure array
# --------------
# p = np.array([])

# ===========================================
# write the data to the specified output file
# ===========================================
# writer = C_RWT.resultsWriter()
# writer.writeFileFromData(x, y, z, u, v, w, p, 'output.spnsm')

# =========================================
# read the output file and print the arrays
# =========================================
# reader = C_RRD.resultsReader()
# readData = reader.readDataFromFile('output.spnsm')

# print(readData)
