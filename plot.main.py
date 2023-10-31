from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import numpy as np
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib as mpl
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.properties import ListProperty
from kivy.uix.label import Label

class RoundedButton(ButtonBehavior, Label):
    background_color = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = 90
        self.font_size = 40
        self.border_radius = [15, ]
        self.padding = [50, 10]

class TransparentBoxLayout(BoxLayout):
    pass


class FrontPage(Screen):
    def on_enter(self):
        self.box = TransparentBoxLayout(orientation='vertical', spacing=20, padding=(20, 100, 20, 20))

        # Add 6 buttons with labels "Distribution 1" to "Distribution 6"
        for i in range(1, 7):
            button_container = BoxLayout(orientation='horizontal', spacing=20)

            button = RoundedButton(text=f'Distribution {i}', font_size=30)
            # Set different background colors based on the button index
            if i == 1:
                button.background_color = (1, 0, 0, 1)  # Red color for the first button
            elif i == 2:
                button.background_color = (0, 1, 0, 1)  # Green color for the second button
            elif i == 3:
                button.background_color = (0, 0, 1, 1)  # Blue color for the third button
            elif i == 4:
                button.background_color = (0.5, 0.5, 0, 1)  # Yellow color for the fourth button
            elif i == 5:
                button.background_color = (0, 0.5, 0.5, 1)  # Teal color for the fifth button
            elif i == 6:
                button.background_color = (0.5, 0, 0.5, 1)  # Purple color for the sixth button

            button.border_radius = [30,]
            button_container.add_widget(button)

            self.box.add_widget(button_container)

            # Add spacer widget for space between button containers
            spacer = Widget(size_hint=(1, None), height=20)
            self.box.add_widget(spacer)

        self.add_widget(self.box)

    def on_back_button(self):
        app = App.get_running_app()
        app.root.current = 'front_page'


class SecondPage(Screen):
    def on_enter(self):
        self.box = BoxLayout(orientation='vertical', size_hint=(1, 1))

        # Instructions label
        instructions = Label(text='Please input the parameters!', size_hint=(1, 0.15))
        self.box.add_widget(instructions)

        # Container for input boxes
        input_box = BoxLayout(orientation='vertical', size_hint=(1, .3))

        # Input box for N
        self.N_input = TextInput(hint_text='N', size_hint=(1, None), height=90, font_size=50, halign="center",
                                 foreground_color=(1, 0, 0, 1))
        input_box.add_widget(self.N_input)

        # Another BoxLayout for the mean and std_dev inputs
        input_box_row2 = BoxLayout(orientation='horizontal', size_hint=(1, None), height=90)

        # Input box for mean
        self.mean_input = TextInput(hint_text='Mean', size_hint=(0.5, None), height=90, font_size=50,
                                    halign="center", foreground_color=(1, 0, 0, 1))
        self.mean_input.bind(text=self.on_mean_input)
        input_box_row2.add_widget(self.mean_input)

        # Input box for std_dev
        self.std_dev_input = TextInput(hint_text='Standard Deviation', size_hint=(0.5, None), height=90,
                                       disabled=True, font_size=50, halign="center", foreground_color=(1, 0, 0, 1))
        input_box_row2.add_widget(self.std_dev_input)

        input_box.add_widget(input_box_row2)
        self.box.add_widget(input_box)

        # Create Plot button
        button = Button(text='Create Plot', size_hint=(1, 0.25), font_size=50)
        button.bind(on_release=self.create_plot)
        self.box.add_widget(button)

        self.add_widget(self.box)

    def on_mean_input(self, instance, value):
        # Enable/disable the std_dev input based on the mean input
        if value:
            self.std_dev_input.disabled = False
        else:
            self.std_dev_input.disabled = False
            self.std_dev_input.text = ''  # Clear the std_dev input

    def create_plot(self, instance):
        nn = int(self.N_input.text) if self.N_input.text else None
        mean = float(self.mean_input.text) if self.mean_input.text else None
        std_dev = float(self.std_dev_input.text) if self.std_dev_input.text else None

        if mean is None:
            print('Please enter the mean.')
            return

        if std_dev is None:
            print('Please enter the standard deviation.')
            return
        elif std_dev < 0:
            print('Standard deviation must be non-negative.')
            return

        # Clear the existing plot
        for child in self.box.children[:]:
            if isinstance(child, FigureCanvasKivyAgg):
                self.box.remove_widget(child)

        data = np.random.normal(mean, std_dev, size=nn)

        fig, axs = plt.subplots(2, 1)
        mpl.rcParams['font.size'] = 16
        label_font_size = 16

        # Plot the histogram
        axs[0].hist(data, bins='auto', alpha=0.7, rwidth=0.85)
        axs[0].set_ylabel('Frequency', fontsize=label_font_size)

        # Plot the line plot
        axs[1].plot(data)
        axs[1].set_ylabel('Values')

        mean_value = np.mean(data)  # Calculate the mean of the data

        # Add the dashed line at the mean
        axs[1].axhline(mean_value, color='r', linestyle='--', label='Mean')
        axs[1].legend(fontsize=label_font_size)
        axs[1].set_ylabel('Value', fontsize=label_font_size)

        # Add the plot to the BoxLayout
        canvas = FigureCanvasKivyAgg(fig)
        self.box.add_widget(canvas)

    def on_back_button(self):
        app = App.get_running_app()
        app.root.current = 'front_page'


class WindowManager(ScreenManager):
    pass


kv = """
WindowManager:
    FrontPage:
    SecondPage:

<TransparentBoxLayout>:
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 0.5
        Rectangle:
            pos: self.pos
            size: self.size

<RoundedButton>:
    background_color: 0, 0, 0, 0.5
    background_normal: ''
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: self.border_radius

<FrontPage>:
    name: 'front_page'

<SecondPage>:
    name: 'second_page'

"""

runTouchApp(Builder.load_string(kv))
