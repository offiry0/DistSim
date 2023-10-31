from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create existing buttons/labels
        button1 = Button(text='Button 1')
        label1 = Label(text='Label 1')

        # Add existing widgets to the layout with a specific ratio
        layout.add_widget(button1)
        layout.add_widget(label1)

        # Generate some data
        data = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

        # Create a figure with a specific size for the histogram
        fig, ax = plt.subplots(figsize=(8, 16))  # Width: 8 inches, Height: 6 inches

        # Create a histogram plot
        ax.hist(data, bins='auto')

        # Create a FigureCanvasKivyAgg instance to display the plot in Kivy
        canvas = FigureCanvasKivyAgg(fig)

        # Add the histogram plot to the layout with a specific ratio
        layout.add_widget(canvas)

        return layout

MyApp().run()
