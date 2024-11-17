from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta

class DynamicLabels(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # create a button for each data entry, specifying the text
            temp_button = Label(text=name)
            temp_button.bind(on_press=self.press_entry)
            # set the button's background colour
            temp_button.background_color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # get name (dictionary key) from the text of Button we clicked on
        name = instance.text
        # change the button's background colour
        instance.background_color = ALTERNATIVE_COLOUR
        # update status text
        self.status_text = f"{name}'s number is {self.name_to_phone[name]}"

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.main.clear_widgets()

DynamicLabels().run()
