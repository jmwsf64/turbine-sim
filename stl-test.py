from lib.modules.readers import classSTLReader as C_STL


# =======================
# example stl file import
# =======================
stlIn = C_STL.stlInput()
box = stlIn.importSTL('lib/files/box.stl')

# ===================
# imported properties
# ===================
print('\n\nNormals: \n', box.normals)
print('\n\nVolume:  ', box.volume)
print('\n\nx-coords:\n', box.v0)
print('\n\ny-coords:\n', box.v1)
print('\n\nz-coords:\n', box.v2)
print('\n\nCOG:     \n', box.cog)
print('\n\nInertia: \n', box.inertia)
