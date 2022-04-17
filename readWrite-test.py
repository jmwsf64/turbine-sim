import numpy as np
import lib.modules.readers.classResultsReader as C_RRD
import lib.modules.writers.classResultsWriter as C_RWT

# ========================================
# data to read/write in custom file format
# ========================================

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
u = np.array([[[0.64345014, -0.55829817, 0.8262379, 0.74961439, 0.63505058],
               [-1.28897414, 1.23228946, -0.97049823, 0.70006478, -0.05691932]],
              [[-0.83428849, 0.3420417, -0.71206633, -0.93088233, -0.67911077],
               [-0.99226709, 0.32718733, -0.17121412, -0.88707578, -0.49421164]],
              [[0.02450344, -0.46767478, 1.24893906, 1.40707394, 0.03011951],
               [0.73870223, -0.27560314, -0.41443749, 2.11529066, 0.05680994]]])

v = np.array([[[0.17716905, -1.20999969, 0.46936722, 1.38477511, 2.33357225],
               [-1.79894835, 0.4400689, 0.16575696, -0.25577792, -0.5120221]],
              [[0.47676121, 1.3314757, -1.44080575, -0.45844577, 1.52070792],
               [-1.01751679, 0.20607083, -0.46224274, 1.57204086, -0.3573411]],
              [[-1.06887129, 0.23107734, 1.70780153, -0.21645786, 0.51200505],
               [1.16964311, 0.50997888, -0.22355362, 1.13378256, -0.09518594]]])

w = np.array([[[-1.02284962, -1.32292399, 1.27278496, -0.67281027, 0.88414435],
               [-0.43630242, 1.94301863, 1.3428904, 0.7895750, 9 - 1.28153805]],
              [[1.79796367, 0.01464176, -1.28629991, 2.21822169, -1.25090995],
               [0.29654884, 0.4608185, -0.07676054, -1.34842502, -1.10989465]],
              [[-0.52437792, 2.81710507, 0.22174233, -1.05297012, -0.90723715],
               [-1.27158043, -1.33144063, -0.040859, 2.13268515, 0.18340196]]])

# --------------
# pressure array
# --------------
p = np.array([[[3.00217868, 0.8839569, 4.12235872, 6.84964285, 5.35324116],
               [3.1474931, 5.9938211, 7.98435019, 0.81712674, 7.13864755]],
              [[9.63708867, 0.36445591, 6.68599544, 8.25871732, 7.41697198],
               [6.55536133, 1.49892616, 8.81382672, 5.01061607, 4.38921729]],
              [[8.25217503, 1.9127678, 7.29848348, 0.50491023, 0.5732046],
               [9.05059054, 2.50719305, 7.96317473, 3.60223668, 7.1359925]]])

# ===========================================
# write the data to the specified output file
# ===========================================
writer = C_RWT.resultsWriter()
writer.writeFileFromData(x, y, z, u, v, w, p, 'output.spnsm')

# =========================================
# read the output file and print the arrays
# =========================================
reader = C_RRD.resultsReader()
r_x, r_y, r_z, r_u, r_v, r_w, r_p = reader.readDataFromFile('output.spnsm')

# ============================================
# print results to verify correct input/output
# ============================================
dims     = x.shape
numElems = dims[0]*dims[1]*dims[2]
print('x:', numElems == sum(sum(sum(x == r_x))))
print('y:', numElems == sum(sum(sum(y == r_y))))
print('z:', numElems == sum(sum(sum(z == r_z))))
print('u:', numElems == sum(sum(sum(u == r_u))))
print('v:', numElems == sum(sum(sum(v == r_v))))
print('w:', numElems == sum(sum(sum(w == r_w))))
print('p:', numElems == sum(sum(sum(p == r_p))))
