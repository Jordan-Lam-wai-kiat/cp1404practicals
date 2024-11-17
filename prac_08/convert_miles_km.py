from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometers(App):

    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.output = f"{self.root.ids.output_text.text}"
        return self.root

    def convert_to_kilometers(self, value):
        try:
            result = int(value) * 1.60934
            self.output = str(result)
        except ValueError:
            self.output = str(0.0)

    def increase_number(self, value):
        try:
            result = int(value) + 1
            self.root.ids.input_text.text = str(result)
        except ValueError:
            result = 0 + 1
            self.root.ids.input_text.text = str(result)


    def decrease_number(self, value):
        try:
            result = int(value) - 1
            self.root.ids.input_text.text = str(result)
        except ValueError:
            result = 0 - 1
            self.root.ids.input_text.text = str(result)


MilesToKilometers().run()