from kivy.app import App
from kivy.uix.button import Button
from plyer import filechooser


# ============================
# kivy application development
# ============================
class SpinSimApp(App):

    def build(self):
        spinSimApp = SpinSim()
        return spinSimApp


if __name__ == '__main__':

    # -------------------
    # hello world example
    # -------------------
    SpinSimApp().run()

    # -------------------
    # file select example
    # -------------------
    # path = filechooser.open_file(title="Choose an STL file",
    #                              filters=[("Stereo-lithography file (.stl)", "*.stl")],
    #                              multiple=True)
    # print(path)
