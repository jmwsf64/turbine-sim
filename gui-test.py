from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
import lib.modules.gui.guiModule as guiF


# ======================
# kivy application class
# ======================
class SpinSimApp(App):

    def build(self):

        # ------------------------
        # create layout parameters
        # ------------------------
        sizeX = 800
        sizeY = 800
        layout = FloatLayout(size=(sizeX, sizeY))

        # --------------
        # create buttons
        # --------------
        btn1 = Button(text='Hello World!',
                      size_hint=(0.15, 0.1),
                      pos=(0, 300))
        btn2 = Button(text='Select an STL file',
                      size_hint=(0.35, 0.1),
                      pos=(500, 0),
                      on_press=guiF.chooseStl)

        # ---------------------
        # add buttons to layout
        # ---------------------
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        # -------------
        # return layout
        # -------------
        return layout


# ====================
# run kivy application
# ====================
SpinSimApp().run()
