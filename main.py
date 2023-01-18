from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyIntegerInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        # Only allow integers to be entered
        if substring.isdigit():
            super(MyIntegerInput, self).insert_text(substring, from_undo=from_undo)


class CollectData(GridLayout):  # creating the structure
    def __init__(self, **kwargs):  # implement alot functions and agruments
        super(CollectData, self).__init__()
        self.cols = 2  # of columns
        """Enter the name below """
        self.add_widget(Label(text='What is your name: '))
        self.name = TextInput()  # type name into text box
        self.add_widget(self.name)
        self.name.size_hint = (0.5, 0.5)
        self.name.halign = 'center'
        self.name.valign = 'center'

        """Enter one side of a square below """
        self.add_widget(Label(text='Enter one side of Square: '))
        self.square = MyIntegerInput()  # type name into text box
        self.add_widget(self.square)
        self.square.size = (0.5, 0.5)
        self.square.halign = 'center'
        self.square.valign = 'center'
        self.square.width = 300

        """Enter one side of a Circle below """
        self.add_widget(Label(text='Enter Radius of Circle'))
        self.circle = MyIntegerInput()  # type name into text box
        self.add_widget(self.circle)
        self.circle.size = (0.5, 0.5)
        self.circle.halign = 'center'
        self.circle.valign = 'center'
        self.circle.width = 300

        """Enter Height of a Triangle below """
        self.add_widget(Label(text='Enter height of Triangle'))
        self.triangleH = MyIntegerInput()  # type name into text box
        self.add_widget(self.triangleH)
        self.triangleH.size = (0.5, 0.5)
        self.triangleH.halign = 'center'
        self.triangleH.valign = 'center'
        self.triangleH.width = 300

        """Enter Base below """
        self.add_widget(Label(text='Enter Base of Triangle'))
        self.triangleB = MyIntegerInput()  # type name into text box
        self.add_widget(self.triangleB)
        self.triangleB.size = (0.5, 0.5)
        self.triangleB.halign = 'center'
        self.triangleB.valign = 'center'
        self.triangleB.width = 300

        """Enter the name of Ellipse axis a and axis b gender below """
        self.add_widget(Label(text='Enter axis 1 of Elipse'))
        self.axis1 = MyIntegerInput()  # type name into text box
        self.add_widget(self.axis1)
        self.axis1.size = (0.5, 0.5)
        self.axis1.halign = 'center'
        self.axis1.valign = 'center'
        self.axis1.width = 300

        """Enter the name of Ellipse axis a and axis b gender below """
        self.add_widget(Label(text='Enter axis 2 of Ellipse'))
        self.axis2 = MyIntegerInput()  # type name into text box
        self.add_widget(self.axis2)
        self.axis2.size = (0.5, 0.5)
        self.axis2.halign = 'center'
        self.axis2.valign = 'center'
        self.axis2.width = 300

        """button design next"""
        self.press = Button(text="Click to find Area")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        self.output = Label(text='')  # Create an empty label
        self.add_widget(self.output)  # Add the label to the
        self.output.halign = 'center'
        self.output.valign = 'center'
        self.output.color = (1, 0, 0, 1)

    def click_me(self, instance):
        square = int(self.square.text)
        s_square = (square * square)

        radius = float(self.circle.text)
        c_area = 3.14159265359 * (radius ** 2)

        triangleH = float(self.triangleH.text)
        triangleB = float(self.triangleB.text)
        t_area = (triangleH * triangleB) / 2

        axis1 = float(self.axis1.text)
        axis2 = float(self.axis2.text)
        ellipse = ((axis1 * axis2) * 3.14159265359)

        self.output.text += "Hi " + self.name.text + " and welcome! \n"
        self.output.text += "Area of Square is: " + str(round(s_square, 2)) + "\n"
        self.output.text += "Area of circle is: " + str(round(c_area, 2)) + "\n"
        self.output.text += "Area of Triangle is: " + str(round(t_area, 2)) + "\n"
        self.output.text += "Area of Ellipse is: " + str(round(ellipse, 2))


class RunFuncsHere(App):
    def build(self):
        return CollectData()  # call childApp


if __name__ == "__main__":
    RunFuncsHere().run()
