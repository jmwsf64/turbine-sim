from kivy.app import App
from kivy.uix.button import Button
from plyer import filechooser


# ============================
# kivy application development
# ============================
class MyApp(App):

    def build(self):
        self.icon = r'lib/files/icons/spin-sim.png'
        return Button(text='Hello World')


if __name__ == '__main__':

    # -------------------
    # hello world example
    # -------------------
    MyApp().run()

    # -------------------
    # file select example
    # -------------------
    # path = filechooser.open_file(title="Choose an STL file",
    #                              filters=[("Stereo-lithography file (.stl)", "*.stl")],
    #                              multiple=True)
    # print(path)
