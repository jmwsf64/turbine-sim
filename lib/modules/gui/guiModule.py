from plyer import filechooser


def chooseStl(btn):
    path = filechooser.open_file(title="Choose an STL file",
                                 filters=[("Stereo-lithography file (.stl)", "*.stl")],
                                 multiple=True)
    return path
