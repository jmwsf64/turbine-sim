from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import lib.modules.gui.guiModule as guiM


# --------------------------------------------
# configure images on buttons to be resizeable
# --------------------------------------------
Config.set('graphics', 'resizable', True)


# ======================
# kivy application class
# ======================
class SpinSimApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bladeFiles   = []
        self.supportFiles = []
        self.icon = 'lib/files/icons/spin-sim.png'

    def build(self):

        # ------------------------
        # create layout parameters
        # ------------------------
        layout = GridLayout(rows=2, cols=2)

        # --------------
        # create buttons
        # --------------
        btn1 = Button(text='Select Blade STL File',
                      size_hint_x=None,
                      width=150,
                      size_hint_y=None,
                      height=25,
                      on_release=lambda button: guiM.chooseBladeStl('btn1', self.bladeFiles))

        btn2 = Button(text='Print Blade STL Path',
                      size_hint_x=None,
                      width=150,
                      size_hint_y=None,
                      height=25,
                      on_release=lambda button: guiM.printStl('btn2', self.bladeFiles))

        btn3 = Button(text='Select Blade STL File',
                      size_hint_x=None,
                      width=150,
                      size_hint_y=None,
                      height=25,
                      on_release=lambda button: guiM.chooseBladeStl('btn1', self.supportFiles))

        btn4 = Button(text='Print Blade STL Path',
                      size_hint_x=None,
                      width=150,
                      size_hint_y=None,
                      height=25,
                      on_release=lambda button: guiM.printStl('btn2', self.supportFiles))

        # ---------------------
        # add buttons to layout
        # ---------------------
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        # -------------
        # return layout
        # -------------
        return layout


# ====================
# run kivy application
# ====================
SpinSimApp().run()
