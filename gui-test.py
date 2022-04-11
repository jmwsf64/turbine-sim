from kivy.app import App
from kivy.uix.button import Button
from plyer import filechooser

# ======================================================================================================================
# example stl file import
# ======================================================================================================================
stlIn = M_STL.stlInput()
box = stlIn.importSTL('lib/files/box.stl')


# ======================================================================================================================
# kivy application development
# ======================================================================================================================

# -------------------
# hello world example
# -------------------
class MyApp(App):

    def build(self):
        # self.icon = r'lib/icons/app-icon.png'
        return Button(text='Hello World')


if __name__ == '__main__':
    # MyApp().run()

    # -------------------
    # file select example
    # -------------------
    path = filechooser.open_file(title="Choose an STL file",
                                 filters=[("Stereo-lithography file (.stl)", "*.stl")],
                                 multiple=True)
    print(path)