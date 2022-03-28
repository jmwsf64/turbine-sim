from modules import moduleSTL as M_STL

stlIn = M_STL.stlInput()
box = stlIn.importSTL('lib/files/box.stl')
print(box.v0)
