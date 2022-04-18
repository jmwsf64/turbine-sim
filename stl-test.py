from lib.modules.io import classSTLReader as C_STL


# =======================
# example stl file import
# =======================
stlIn = C_STL.stlInput()
box   = stlIn.importSTL('lib/files/testing/box.stl')

# ===================
# imported properties
# ===================
print('\n\nNormals: \n', box.normals)
print('\n\nVolume:  ', box.volume)
print('\n\nx-coords:\n', box.x)
print('\n\ny-coords:\n', box.y)
print('\n\nz-coords:\n', box.z)
print('\n\nCOG:     \n', box.cog)
print('\n\nInertia: \n', box.inertia)
