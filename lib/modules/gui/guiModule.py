from plyer import filechooser


def chooseBladeStl(btn, a_path):
    file = filechooser.open_file(title="Choose an STL file",
                                 filters=[("Stereo-lithography file (.stl)", "*.stl")],
                                 multiple=True)
    a_path.extend(file)


def chooseSupportStl(btn, a_path):
    file = filechooser.open_file(title="Choose an STL file",
                                 filters=[("Stereo-lithography file (.stl)", "*.stl")],
                                 multiple=True)
    a_path.extend(file)


def printStl(btn, a_path):
    print(a_path)
