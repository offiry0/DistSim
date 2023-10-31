from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')

        # Create a Label widget
        label = Label(text='Hello, World!', size_hint=(1, 1))

        # Define the background color
        with label.canvas.before:
            Color(1, 0, 0, 1)  # Set the color to red (RGB values and alpha)
            self.rect = Rectangle(pos=label.pos, size=label.size)

        # Bind the background color to update with the label position and size changes
        label.bind(pos=self.update_rect, size=self.update_rect)

        box.add_widget(label)
        return box

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MyApp().run()
