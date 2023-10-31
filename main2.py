
import numpy as np
import matplotlib

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
import numpy as np
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib as mpl
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown


class SpinnerOptions(SpinnerOption):

    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = [0, 0, 1, 1]    # blue colour
        self.height = 26


class SpinnerDropdown(DropDown):

    def __init__(self, **kwargs):
        super(SpinnerDropdown, self).__init__(**kwargs)
        self.auto_width = False
        self.width = 150
class SpinnerWidget(Spinner):
    def __init__(self, **kwargs):
        super(SpinnerWidget, self).__init__(**kwargs)
        self.dropdown_cls = SpinnerDropdown
        self.option_cls = SpinnerOptions

Window.clearcolor = (.1,.1,.1,1)
current_type = 0

def go_to_previous_screen(self, instance):
    app = App.get_running_app()
    app.root.current = 'home_page'  # Assuming the previous screen's name is 'home_page'



global language_type
language_type = 'en'

class LanguagePage(Screen):
    global language_type
    def on_enter(self):
        with self.canvas.before:
            Color(119/256, 187/256, 63/256, 1)  # Set the background color (in this example, red)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        kivy_defaulttheme_color = np.array([88, 88, 88, 256]) / 256
        desired_button_color = np.array([247, 247, 246, 256]) / 256
        tintshade_color = desired_button_color / kivy_defaulttheme_color

        self.box_a1 = BoxLayout(orientation='vertical', padding=80, spacing=20)

        self.box_b1 = BoxLayout(orientation='vertical', size_hint=(1, 0.75))
        self.box_b2 = BoxLayout(orientation='horizontal', spacing=90, size_hint=(1, 0.25))

        b1_image_1 = Image(source='bscstudioslogo.png')
        b2_image_1 = Image(source='bscstudioslogo.png')
        b1_text_1 = Label(text="", font_size=16, color=(0.1, 0.1, 0.1), size_hint=(0.4, 0.05),
                          halign='center', valign='center', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.b2_button_1 = Button(text='Welcome', font_size=70, color=(0.1, 0.6, 0.1), size_hint=(0.5, 1),
                             background_color=tintshade_color)
        self.b2_button_2 = Button(text='Willkommen', font_size=70, color=(0.1, 0.6, 0.1), size_hint=(0.5, 1),
                             background_color=tintshade_color)

        #b2_button_1.bind(on_press=self.go_to_scan_page)
        #b2_button_2.bind(on_press=self.go_to_list_page)

        self.b2_button_1.bind(on_press=self.switch_language_en)
        self.b2_button_2.bind(on_press=self.switch_language_de)

        self.b2_button_1.bind(on_press=self.go_to_home_page)
        self.b2_button_2.bind(on_press=self.go_to_home_page)

        self.box_b1.add_widget(b1_image_1)
        #self.box_b2.add_widget(b2_image_1)
        self.box_b1.add_widget(b1_text_1)
        self.box_b2.add_widget(self.b2_button_1)
        self.box_b2.add_widget(self.b2_button_2)

        self.box_a1.add_widget(self.box_b1)
        self.box_a1.add_widget(self.box_b2)

        self.add_widget(self.box_a1)

    def update_language(self, instance):
        print('test')
        if language_type == 'en':
            self.b2_button_1.text = 'Welcome'
            self.b2_button_2.text = 'Willkommen'
        elif language_type == 'de':
            self.b2_button_1.text = 'Welcome'
            self.b2_button_2.text = 'Willkommen'


    def switch_language_en(self, instance):
        global language_type
        language_type = language_type
        language_type = 'en'
        self.update_language(1)

    def switch_language_de(self, instance):
        global language_type
        language_type = language_type
        language_type = 'de'
        self.update_language(1)


    def go_to_home_page(self, instance):
        self.manager.current = 'home_page'

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_leave(self, *args):
        self.clear_widgets()

Window.clearcolor = (.1,.1,.1,1)
current_type = 0

def go_to_previous_screen(self, instance):
    app = App.get_running_app()
    app.root.current = 'home_page'  # Assuming the previous screen's name is 'home_page'

class HomePage(Screen):
    def on_enter(self):
        global language_type
        # self.box = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.box = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, padding=30)
        self.scroll_box = ScrollView()
        self.box.bind(minimum_height=self.box.setter('height'))
        button1 = Button(text=('Normal' if language_type == 'en' else
                               'Normal' if language_type == 'de' else None),
                         size_hint=(0.95, None),
                         size=(100, 160),
                         pos_hint={'center_x': 0.5},
                         font_size=80)
        button1.background_color = (1, 0, 0, 1)
        button2 = Button(text=('Poisson' if language_type == 'en' else
                               'Poisson' if language_type == 'de' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button2.background_color = (1, 0.7, 0, 1)
        button3 = Button(text='Binomial', size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button3.background_color = (0.7, 1, 0, 1)
        button4 = Button(text='Beta', size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button4.background_color = (0, 1, 0, 1)
        button5 = Button(text='Neg. Binomial', size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button5.background_color = (0, 1, 0.7, 1)
        button6 = Button(text='Uniform', size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button6.background_color = (0, 0.7, 1, 1)
        button7 = Button(text=('Chi-squared' if language_type == 'en' else
                               'Chi-quadrat' if language_type == 'de' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button7.background_color = (0, 0, 1, 1)
        button8 = Button(text=('Exponential' if language_type == 'en' else
                               'Exponentiell' if language_type == 'de' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button8.background_color = (0.7, 0, 1, 1)
        button9 = Button(text=('Student\'s t' if language_type == 'en' else
                               'Student\'s t' if language_type == 'de' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},
                         font_size=80)
        button9.background_color = (1, 0, 0.7, 1)

        welcome_text = Label(text='DistSim', size_hint=(None, None), size=(100, 180),
                             pos_hint={'center_x': 0.5},
                             font_size=75, color=(0.2, 0.8, 0.2))

        provide_text = Label(text=('Made possible by Banana Shaped Cow Studios' if language_type == 'en' else
                             'Ermöglicht durch Banana Shaped Cow Studios' if language_type == 'de' else None),                            size_hint=(1, None), size=(100, 100),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.5, 0.8, 0.5))
        welcome_description = Label(text=('The app offers visualizations of various important probability '
                                         'distributions, making it a convenient and engaging way to utilize a '
                                         'two-minute break.' if language_type == 'en' else
                               'Die App bietet Visualisierungen verschiedener wichtiger '
                                         'Wahrscheinlichkeitsverteilungen und ist damit eine bequeme und '
                                         'ansprechende Möglichkeit, eine zweiminütige Pause zu nutzen.'
                               if language_type == 'de' else None),
                                size_hint=(0.9, None), size=(100, 350),
                                pos_hint={'center_x': 0.5, 'center_y': 0.0},
                                font_size=50, color=(0.7, 0.8, .8), halign='center')

        welcome_description.bind(
            width=lambda *x: welcome_description.setter('text_size')(welcome_description, (welcome_description.width,
                                                                                           None)))
        provide_text.bind(
            height=lambda *x: provide_text.setter('text_size')(provide_text, (provide_text.height, None)))

        button1.bind(on_press=lambda instance: self.on_button_press(instance, 1))
        button2.bind(on_press=lambda instance: self.on_button_press(instance, 2))
        button3.bind(on_press=lambda instance: self.on_button_press(instance, 3))
        button4.bind(on_press=lambda instance: self.on_button_press(instance, 4))
        button5.bind(on_press=lambda instance: self.on_button_press(instance, 5))
        button6.bind(on_press=lambda instance: self.on_button_press(instance, 6))
        button7.bind(on_press=lambda instance: self.on_button_press(instance, 7))
        button8.bind(on_press=lambda instance: self.on_button_press(instance, 8))
        button9.bind(on_press=lambda instance: self.on_button_press(instance, 9))
        self.box.add_widget(welcome_text)
        self.box.add_widget(welcome_description)
        self.box.add_widget(button1)
        self.box.add_widget(button2)
        self.box.add_widget(button3)
        self.box.add_widget(button4)
        self.box.add_widget(button5)
        self.box.add_widget(button6)
        self.box.add_widget(button7)
        self.box.add_widget(button8)
        self.box.add_widget(button9)
        self.scroll_box.add_widget(self.box)
        self.add_widget(self.scroll_box)

        self.box.add_widget(provide_text)


    def show_previous_screen(self, instance):
        self.manager.current = 'languagepage'


    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'homepage':
            # do what you want, return True for stopping the propagation
            self.show_previous_screen(1)
            return True
    def on_button_press(self, instance, page_number):
        global current_type
        current_type = page_number
        self.manager.current = 'first_page'


    def on_leave(self):
        # Clear previous content
        self.clear_widgets()



class FirstPage(Screen):
    def on_enter(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        global current_type
        global current_type_name
        current_type_name = 'empty'
        global needed_inputs
        needed_inputs = 0
        global first_input_name
        first_input_name = 'empty'
        global second_input_name
        second_input_name = 'empty'
        global first_input_needs_int
        first_input_needs_int = False
        global second_input_needs_int
        second_input_needs_int = False
        if current_type == 1:
            current_type_name = 'Normal'
            needed_inputs = 2
            first_input_name = ('Mean (μ)' if language_type == 'en' else
                               'Bedeuten (μ)' if language_type == 'de' else None)
            second_input_name = ('Standard Deviation (σ)' if language_type == 'en' else
                               'Standardabteilung (σ)' if language_type == 'de' else None)
        elif current_type == 2:
            current_type_name = 'Poisson'
            needed_inputs = 1
            first_input_name = 'Rate (λ)'
        elif current_type == 3:
            current_type_name = 'Binomial'
            needed_inputs = 2
            first_input_name = ('Experiment Count (n)' if language_type == 'en' else
                               'Anzahl der Experimente (n)' if language_type == 'de' else None)
            first_input_needs_int = True
            second_input_name = ('Success Rate (p)' if language_type == 'en' else
                               'Erfolgsrate (p)' if language_type == 'de' else None)
        elif current_type == 4:
            current_type_name = 'Beta'
            needed_inputs = 2
            first_input_name = ('Shape 1 (α)' if language_type == 'en' else
                               'Form 1 (α)' if language_type == 'de' else None)
            #first_input_needs_int = True
            second_input_name = ('Shape 2 (β)' if language_type == 'en' else
                               'Form 2 (β)' if language_type == 'de' else None)
            #second_input_needs_int = True
        elif current_type == 5:
            current_type_name = 'Neg. Binomial'
            needed_inputs = 2
            first_input_name = ('Success Count (r)' if language_type == 'en' else
                               'Erfolgszählung (r)' if language_type == 'de' else None)
            first_input_needs_int = True
            second_input_name = ('Success Rate (p)' if language_type == 'en' else
                               'Erfolgsrate (p)' if language_type == 'de' else None)
        elif current_type == 6:
            current_type_name = 'Uniform'
            needed_inputs = 2
            first_input_name = ('Lower Bound (a)' if language_type == 'en' else
                               'Untergrenze (a)' if language_type == 'de' else None)
            second_input_name = ('Upper Bound (b)' if language_type == 'en' else
                               'Obere Grenze (b)' if language_type == 'de' else None)
        elif current_type == 7:
            current_type_name = ('Chi-squared' if language_type == 'en' else
                               'Chi-quadrat' if language_type == 'de' else None)
            needed_inputs = 1
            first_input_name = ('Degree of freedom (κ)' if language_type == 'en' else
                               'Freiheitsgrad (κ)' if language_type == 'de' else None)
            first_input_needs_int = True
        elif current_type == 8:
            current_type_name = ('Exponential' if language_type == 'en' else
                               'Exponentiell' if language_type == 'de' else None)
            needed_inputs = 1
            first_input_name = 'Scale (λ)'
        elif current_type == 9:
            current_type_name = 'Student\'s t'
            needed_inputs = 1
            first_input_name = ('Degree of freedom (ν)' if language_type == 'en' else
                               'Freiheitsgrad (ν)' if language_type == 'de' else None)
            first_input_needs_int = True

        self.box = BoxLayout(orientation='vertical', spacing=10, padding=30)
        #self.box.height = 100  # Adjust the height value as desired

        # Instructions label
        self.Apptitle = Label(text=(f'{current_type_name} Distribution' if language_type == 'en' else
                               f'{current_type_name} Verteilung' if language_type == 'de' else None),
                             size_hint=(1, 0.1), font_size=50, color=(0, 1, 0),
                         pos_hint={'center_x':0.5, 'center_y': 1})

        # possible description label
        self.description = Button(text=('Show Description' if language_type == 'en' else
                               'Beschreibung Anzeigen' if language_type == 'de' else None),
        size_hint=(1, 0.1),  pos_hint={
            'center_x': 0.5}, color=(1, 1, 1), font_size=50)
        self.description.background_color = (1, 0, 0, 1)
        self.description.bind(on_press=self.show_popup)
        self.box.add_widget(self.Apptitle)
        self.box.add_widget(self.description)

        #input_box = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, .25))
        #self.box.add_widget(input_box)

        # Add the label widget
        self.simulations_text = Label(text=('Number of Simulations' if language_type == 'en' else
                               'Anzahl der Simulationen' if language_type == 'de' else None),
                                      size_hint=(1, 0.1),
                                      font_size=50,
                                      halign='center',
                                      valign='center',
                                      text_size=(self.width, None),
                                      color=(0, 1, 0),
                                      pos_hint={'center_x': 0.5, 'center_y': 1})
        self.simulations_text.bind(
            texture_size=lambda instance, value: setattr(self.simulations_text, 'height', value[1]))
        self.N_input = 10000
        self.N_input = Spinner(
            # default value shown
            text='Default is 10000. Click to change',
            halign='center',
            # available values
            values=('100', '1000', '5000', '10000', '100000'),
            # just for positioning in our example
            size_hint=(0.5, 0.1),
            height=50,
            font_size=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.N_input.background_color = (1, 0.7, 0, 1)
        self.N_input.size_hint_x = 1

        self.box.add_widget(self.simulations_text)
        self.box.add_widget(self.N_input)

        self.errors = ''
        self.dist_text = Label(
            text=(f' \nInput distribution parameters' if language_type == 'en' else
                f' \nEingabeverteilungsparameter' if language_type == 'de' else None),
            size_hint=(1, 0.05),
            font_size=39,
            halign='center',
            valign='center',
            color=(0, 1, 0))

        self.dist_text.bind(
            texture_size=lambda instance, value: setattr(self.dist_text, 'height', value[1]))
        self.box.add_widget(self.dist_text)

        if needed_inputs == 1:
            self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))
            self.sub_box_1 = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 1))

            self.first_input_1 =  Label(text=f'{first_input_name}',
                                                size_hint=(0.5, 1), font_size=39, color=(1, 0, 1),
                                                pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),
                                          font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                            foreground_color=(0, 0, 1))
            self.first_input_2.background_color=(0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

        elif needed_inputs == 2:
            self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))
            self.sub_box_1 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))

            self.first_input_1 =  Label(text=f'{first_input_name}',
                                                size_hint=(0.5, 1), font_size=39, color=(1, 0, 1),
                                                pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),
                                          font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                            foreground_color=(0, 0, 1))
            self.first_input_2.background_color=(0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

            self.sub_box_2 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))
            self.second_input_1 = Label(text=f'{second_input_name}',
                                                size_hint=(0.5, 1), font_size=39, color=(1, 0, 1),
                                                pos_hint={'center_x': 0.5, 'center_y': 1})
            self.second_input_2 = TextInput(hint_text=second_input_name, size_hint=(1, 1),
                                          font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                            foreground_color=(0, 0, 1))
            self.second_input_2.background_color=(0.7, 1, 0, 1)
            self.sub_box_2.add_widget(self.second_input_1)
            self.sub_box_2.add_widget(self.second_input_2)
            self.sub_box.add_widget(self.sub_box_2)

        self.box.add_widget(self.sub_box)

        empty_text = Label(text=' ', size_hint=(1, .1), size=(100, 200),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.2, 0.8, 0.2))
        empty_text.bind(
            height=lambda *x: empty_text.setter('text_size')(empty_text, (empty_text.height, None)))
        self.box.add_widget(empty_text)
        # Create Plot button
        button = Button(text=' ', size_hint=(1, 0.3),
                        font_size=50, halign='center',
                        background_normal='CreatPlot.png',
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.background_color = (1, 1, 1, 1)

        button.bind(on_press=self.create_plot)

        button_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15), pos_hint={
            'center_x': 0.5, 'center_y': 0.5})

        button_box.background_color = (0, 1, 0.7, 1)

        self.box.add_widget(button)
        newBox = BoxLayout(orientation='vertical', size_hint=(1, 0.1))
        self.box.add_widget(newBox)
        self.box.add_widget(button_box)

        logo = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, .3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        empty_text = Label(text=' ', size_hint=(1, .1),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.2, 0.8, 0.2))
        empty_text.bind(
            height=lambda *x: empty_text.setter('text_size')(empty_text, (empty_text.height, None)))
        self.box.add_widget(empty_text)

        provide_text = Label(text=('Made possible by Banana Shaped Cow Studios' if language_type == 'en' else
                             'Ermöglicht durch Banana Shaped Cow Studios' if language_type == 'de' else None),
                             size_hint=(1, None),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.5, 0.8, 0.5))

        provide_text.bind(
            height=lambda *x: provide_text.setter('text_size')(provide_text, (provide_text.height, None)))
        self.box.add_widget(provide_text)

        global audio_1
        global audio_2
        audio_1 = SoundLoader.load('CLT_easy.wav')
        audio_2 = SoundLoader.load('CLT_difficult.wav')
        self.audio_1 = audio_1
        self.audio_2 = audio_2


        button_box_1 = Button(text=('Central Limit Theorem\n(CLT) Demo' if language_type == 'en' else
                             'Zentraler Grenzwertsatz\n(ZGWS) Demo' if language_type == 'de' else None),
                              font_size=40, halign='center',
                              size_hint=(0.5, 1),
                              pos_hint={'center_y': 0.5}, on_press=self.show_second_page)
        button_box_1.background_color = (0, 1, 0.7, 1)
        global button_box_2
        global button_box_3
        button_box_2 = Button(text=('Explanation\nAudio 1' if language_type == 'en' else
                             'Erläuterung\nAudio 1' if language_type == 'de' else None),
                              font_size=40, halign='center', size_hint=(0.25, 1),
                              pos_hint={'center_y': 0.5}, on_press=self.play_audio_1)
        button_box_2.background_color = (0, .8, 0.5, 1)
        button_box_3 = Button(text=('Explanation\nAudio 2' if language_type == 'en' else
                             'Erläuterung\nAudio 2' if language_type == 'de' else None),
                              font_size=40, halign='center', size_hint=(0.25, 1),
                              pos_hint={'center_y': 0.5}, on_press=self.play_audio_2)
        button_box_3.background_color = (0, .8, 0.5, 1)

        button_box.add_widget(button_box_1)
        button_box.add_widget(button_box_2)
        button_box.add_widget(button_box_3)

        self.add_widget(self.box)

    def show_second_page(self, instance):
        self.manager.current = 'second_page'

    def play_audio_1(self, instance):
        if audio_1.state != 'play':
            audio_1.play()
            button_box_3.disabled = True
            button_box_2.text = ('Stop\nAudio' if language_type == 'en' else
                             'stoppen' if language_type == 'de' else None)
            audio_2.stop()
        else:
            audio_1.stop()
            button_box_3.disabled = False
            button_box_2.text =('Explanation\nAudio 1' if language_type == 'en' else
                             'Erläuterung\nAudio 1' if language_type == 'de' else None)

    def play_audio_2(self, instance):
        if audio_2.state != 'play':
            audio_2.play()
            button_box_2.disabled = True
            button_box_3.text = ('Stop\nAudio' if language_type == 'en' else
                             'stoppen' if language_type == 'de' else None)
            audio_1.stop()
        else:
            audio_2.stop()
            button_box_2.disabled = False
            button_box_3.text = ('Explanation\nAudio 2' if language_type == 'en' else
                             'Erläuterung\nAudio 2' if language_type == 'de' else None)

    def show_error_popup(self, instance):
        popup_x_size = 350 * 2.2
        popup_y_size = 230 * 2.2

        message_label = Label(text=self.errors, size_hint=(1, None), pos_hint={'center_y': 0.6}, halign='left',
                              font_size = 50, color=(1, 0, 0))

        message_label.bind(
            width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width,
                                                                               None)))

        # Create the popup and set its content
        popup = Popup(title=('Error' if language_type == 'en' else
                             'Fehler' if language_type == 'de' else None),
                            content=message_label, size_hint=(None, None), size=(popup_x_size, popup_y_size))
        # Open the popup
        popup.open()

    def show_popup(self, instance):
        popup_x_size = 400 * 2.2
        popup_y_size = 350 * 3.9
        # Create a label with the message
        message_label = Label(text='', size_hint=(1, None), pos_hint={'center_y': 0.6}, halign='center', font_size=50)

        if current_type == 1:
            message_label.text = ('A normal (or Gaussian; named after Carl Friedrich Gauss) distribution is a ' \
                                 'continuous probability distribution for a real-valued random variable. Normal  ' \
                                 'distribution has two parameters, which are the mean and the standard deviation,  ' \
                                 'respectively. It is the most important distribution in statistical data analysis.'
                                  if language_type == 'en' else
                                 'Eine Normalverteilung (oder Gaußverteilung; benannt nach Carl Friedrich Gauß) ist ' \
                                 'eine kontinuierliche Wahrscheinlichkeitsverteilung für eine reellwertige ' \
                                 'Zufallsvariable. Die Normalverteilung hat zwei Parameter, nämlich den Mittelwert ' \
                                 'und die Standardabweichung. Es ist die wichtigste Verteilung in der statistischen ' \
                                 'Datenanalyse.' if language_type == 'de' else None)
        elif current_type == 2:
            message_label.text = ('The Poisson (Siméon Denis Poisson) distribution is a discrete probability ' \
                                 'distribution that describes the probability of a given number of events occurring ' \
                                 'in a fixed interval of time. The Poisson distribution has only one parameter, ' \
                                 'which is the rate. The Poisson distribution is often used to model rare events. ' \
                                 'The parameter of a Poisson distribution represents both its expectation (mean) and ' \
                                 'variance.'
                                  if language_type == 'en' else
                                 'Die Poisson-Verteilung (Siméon Denis Poisson) ist eine diskrete ' \
                                 'Wahrscheinlichkeitsverteilung, die die Wahrscheinlichkeit beschreibt, mit der eine ' \
                                 'bestimmte Anzahl von Ereignissen in einem festen Zeitintervall auftritt. Die ' \
                                 'Poisson-Verteilung hat nur einen Parameter, nämlich die Rate. Die Poisson-Verteilung ' \
                                 'wird häufig zur Modellierung seltener Ereignisse verwendet. Der Parameter einer ' \
                                 'Poisson-Verteilung repräsentiert sowohl ihren Erwartungswert (Mittelwert) als auch ' \
                                 'ihre Varianz.' if language_type == 'de' else None)
        elif current_type == 3:
            message_label.text = ('The binomial distribution is the discrete probability distribution of the number ' \
                                 'of successes in a sequence of n independent experiments. For a single experiment, ' \
                                 'i.e., n = 1, the binomial distribution is a Bernoulli (Jacob Bernoulli) ' \
                                 'distribution. The binomial distribution has two parameters, including n (number of ' \
                                 ' experiments) and p (success rate).'
                                  if language_type == 'en' else
                                 'Die Binomialverteilung ist die diskrete Wahrscheinlichkeitsverteilung der Anzahl der ' \
                                 'Erfolge in einer Folge von n unabhängigen Experimenten. Für ein einzelnes Experiment, ' \
                                 'd. h. n = 1, ist die Binomialverteilung eine Bernoulli-Verteilung (Jacob Bernoulli). ' \
                                 'Die Binomialverteilung hat zwei Parameter, darunter n (Anzahl der Experimente) und p ' \
                                 '(Erfolgsrate).' if language_type == 'de' else None)
        elif current_type == 4:
            message_label.text = ('The beta distribution is a family of continuous probability distributions defined ' \
                                 'on the interval of 0 and 1. The beta distribution has two parameters, denoted by ' \
                                 'alpha (α) and beta (β), respectively, which control the shape of the distribution. ' \
                                 'It is widely used as a prior distribution in Bayesian data analysis.'
                                  if language_type == 'en' else
                                 'Die Beta-Verteilung ist eine Familie kontinuierlicher Wahrscheinlichkeitsverteilungen,' \
                                 ' die im Intervall von 0 und 1 definiert sind. Die Beta-Verteilung verfügt über zwei ' \
                                 'Parameter, die mit Alpha (α) bzw. Beta (β) bezeichnet werden und die Form der ' \
                                 'Verteilung steuern. Sie wird häufig als Prior-Verteilung in der Bayesschen ' \
                                 'Datenanalyse verwendet.' if language_type == 'de' else None)
        elif current_type == 5:
            message_label.text = ('The negative binomial distribution is a discrete probability distribution that ' \
                                 'models the number of failures in a sequence of independent and identically ' \
                                 'distributed Bernoulli trials before a specified number of successes occurs. The ' \
                                 'negative binomial distribution has two parameters, which are the number of ' \
                                 'successes required (r) and the probability of success in a single trial (p). The ' \
                                 'negative binomial distribution offers more flexibility than the Poisson ' \
                                 'distribution for modeling count or event data because it does not require the mean ' \
                                 'to be equal to the variance.'
                                  if language_type == 'en' else
                                 'Die negative Binomialverteilung ist eine diskrete Wahrscheinlichkeitsverteilung, ' \
                                 'die die Anzahl der Fehlschläge in einer Folge unabhängiger und identisch verteilter ' \
                                 'Bernoulli-Versuche modelliert, bevor eine bestimmte Anzahl von Erfolgen eintritt. ' \
                                 'Die negative Binomialverteilung hat zwei Parameter: die Anzahl der erforderlichen ' \
                                 'Erfolge (r) und die Erfolgswahrscheinlichkeit in einem einzelnen Versuch (p). ' \
                                 'Die negative Binomialverteilung bietet mehr Flexibilität als die Poisson-Verteilung ' \
                                 'für die Modellierung von Zähl- oder Ereignisdaten, da sie nicht erfordert, dass der ' \
                                 'Mittelwert gleich der Varianz ist.' if language_type == 'de' else None)
        elif current_type == 6:
            message_label.text = ('The continuous uniform distribution is a symmetric probability distribution that ' \
                                 'describes an experiment where there is an equally likely outcome within a certain ' \
                                 'lower and upper bounds of the interval. It is often used as a non-informative ' \
                                 'prior in Bayesian data analysis, as it does not impose any prior knowledge. ' \
                                 'However, it is still informative in the sense that its mean is the average of ' \
                                 'lower and upper bounds.'
                                  if language_type == 'en' else
                                 'Die kontinuierliche Gleichverteilung ist eine symmetrische ' \
                                 'Wahrscheinlichkeitsverteilung, die ein Experiment beschreibt, bei dem es innerhalb ' \
                                 'einer bestimmten Unter- und Obergrenze des Intervalls ein gleich wahrscheinliches ' \
                                 'Ergebnis gibt. In der Bayesschen Datenanalyse wird es oft als nicht informativer ' \
                                 'Prior verwendet, da es kein Vorwissen erfordert. Es ist jedoch immer noch informativ ' \
                                 'in dem Sinne, dass sein Mittelwert der Durchschnitt der unteren und oberen Grenzen '
                                 'ist.' if language_type == 'de' else None)
        elif current_type == 7:
            message_label.text = ('The chi-squared distribution with k degrees of freedom is the distribution of a ' \
                                 'sum of the squares of k independent standard normal random variables. The ' \
                                 'chi-squared distribution is a special case of the gamma distribution and is one of ' \
                                 'the most widely used probability distributions in inferential statistics.'
                                  if language_type == 'en' else
                                 'Die Chi-Quadrat-Verteilung mit k Freiheitsgraden ist die Verteilung einer Summe der ' \
                                 'Quadrate von k unabhängigen Standardnormal-Zufallsvariablen. Die ' \
                                 'Chi-Quadrat-Verteilung ist ein Sonderfall der Gammaverteilung und eine der am ' \
                                 'häufigsten verwendeten Wahrscheinlichkeitsverteilungen in der Inferenzstatistik.'
                                 if language_type == 'de' else None)
        elif current_type == 8:
            message_label.text = ('The exponential distribution is the probability distribution of the time between ' \
                                 'events in a Poisson point process. It is a special case of the gamma distribution, ' \
                                 'characterized by the rate parameter. The exponential distribution is often ' \
                                 'described as memory-less because the probability of an event occurring within a ' \
                                 'certain time interval does not depend on the elapsed time.'
                                  if language_type == 'en' else
                                 'Die Exponentialverteilung ist die Wahrscheinlichkeitsverteilung der Zeit zwischen ' \
                                 'Ereignissen in einem Poisson-Punkt-Prozess. Es handelt sich um einen Sonderfall der ' \
                                 'Gammaverteilung, der durch den Geschwindigkeitsparameter charakterisiert wird. Die ' \
                                 'Exponentialverteilung wird oft als gedächtnislos beschrieben, da die ' \
                                 'Wahrscheinlichkeit, dass ein Ereignis innerhalb eines bestimmten Zeitintervalls ' \
                                 'eintritt, nicht von der verstrichenen Zeit abhängt.'
                                 if language_type == 'de' else None)
        elif current_type == 9:
            message_label.text = ('Student (named after William Sealy Gosset) t-distribution is a continuous ' \
                                 'probability distribution that generalizes the standard normal distribution. For a ' \
                                 'degree of freedom equal to 1, the Student t distribution becomes the standard ' \
                                 'Cauchy distribution, whereas for degrees of freedom approaching infinity, ' \
                                 'the t-distribution converges to the standard normal distribution. The two-sample ' \
                                 't-test is commonly used and is based on the t-distribution. It allows for unequal ' \
                                 'variances between the two groups being compared.'
                                  if language_type == 'en' else
                                 'Die Student-T-Verteilung (benannt nach William Sealy Gosset) ist eine kontinuierliche ' \
                                 'Wahrscheinlichkeitsverteilung, die die Standardnormalverteilung verallgemeinert. ' \
                                 'Für einen Freiheitsgrad gleich 1 wird die Student-t-Verteilung zur ' \
                                 'Standard-Cauchy-Verteilung, während für Freiheitsgrade gegen Unendlich die ' \
                                 't-Verteilung zur Standardnormalverteilung konvergiert. Der t-Test mit zwei ' \
                                 'Stichproben wird häufig verwendet und basiert auf der t-Verteilung. Es ermöglicht ' \
                                 'ungleiche Varianzen zwischen den beiden verglichenen Gruppen.'
                                 if language_type == 'de' else None)

        message_label.bind(
            width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width,
                                                                               None)))

        # Create the popup and set its content
        popup = Popup(title='', separator_height = 0, content=message_label, size_hint=(None, None), size=(popup_x_size,
                                                                                                popup_y_size))
        # Open the popup
        popup.open()

    def show_home_screen(self, instance):
        self.manager.current = 'home_page'

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'first_page':
            # do what you want, return True for stopping the propagation
            self.show_home_screen(1)
            return True

    # noinspection PyGlobalUndefined
    def create_plot(self, instance):
        global current_type
        global current_type_name
        global needed_inputs
        global first_input_name
        global second_input_name
        global first_input_needs_int
        global second_input_needs_int
        first_value = None
        second_value = None
        data = None
        self.errors = ''

        if not first_input_needs_int:
            try:
                first_value = float(self.first_input_2.text)
            except ValueError:
                self.errors = (f'{first_input_name} must be a number.'
                                  if language_type == 'en' else
                                 f'{first_input_name} muss eine Nummer sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
        elif first_input_needs_int:
            try:
                first_value = int(self.first_input_2.text)
            except ValueError:
                self.errors = (f'{first_input_name} must be an integer.'
                                  if language_type == 'en' else
                                 f'{first_input_name} muss eine ganze Zahl sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
        if needed_inputs >= 2:
            if not second_input_needs_int:
                try:
                    second_value = float(self.second_input_2.text)
                except ValueError:
                    self.errors = (f'{second_input_name} must be a number.'
                                  if language_type == 'en' else
                                 f'{second_input_name} muss eine Nummer sein.'
                                 if language_type == 'de' else None)
                    self.show_error_popup(1)
                    return
            elif second_input_needs_int:
                try:
                    second_value = int(self.second_input_2.text)
                except ValueError:
                    self.errors = (f'{second_input_name} must be an integer.'
                                  if language_type == 'en' else
                                 f'{second_input_name} muss eine ganze Zahl sein.'
                                 if language_type == 'de' else None)
                    self.show_error_popup(1)
                    return

        if self.N_input.text != 'Default is 10000. Click to change':
            try:
                size = int(self.N_input.text) if self.N_input.text else None
            except ValueError:
                self.errors = 'Number of iterations (N) must be an integer.'
                self.show_error_popup(1)
                return
        else:
            size = 10000

        if current_type == 1:
            if second_value <= 0:
                self.errors = ('Standard deviation (σ) must be greater than 0.'
                                  if language_type == 'en' else
                                 'Die Standardabweichung (σ) muss größer als 0 sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.normal(first_value, second_value, size=size)
        elif current_type == 2:
            if first_value <= 0:
                self.errors = ('Rate (λ) must be positive.'
                                  if language_type == 'en' else
                                 'Rate (λ) muss positiv sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.poisson(first_value, size=size)
        elif current_type == 3:
            if not 0 <= second_value <= 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                                  if language_type == 'en' else
                                 'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                                  if language_type == 'en' else
                                 'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.binomial(first_value, second_value, size=size)
        elif current_type == 4:
            if not first_value > 0:
                self.errors = ('Shape (α) must be greater than 0.'
                                  if language_type == 'en' else
                                 'Form (α) muss größer als 0 sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            if not second_value > 0:
                self.errors = ('Shape (β) must be greater than 0.'
                                  if language_type == 'en' else
                                 'Form (β) muss größer als 0 sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.beta(first_value, second_value, size=size)
        elif current_type == 5:
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                                  if language_type == 'en' else
                                 'Experiment Count (n) muss eine ganze Zahl größer als 0 sein'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            if not 0 < second_value < 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                                  if language_type == 'en' else
                                 'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.negative_binomial(first_value, second_value, size=size)
        elif current_type == 6:
            data = np.random.uniform(first_value, second_value, size=size)
        elif current_type == 7:
            if first_value < 0:
                self.errors = ('Degree of freedom (κ) must be positive.'
                                  if language_type == 'en' else
                                 'Der Freiheitsgrad (κ) muss positiv sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.chisquare(first_value, size=size)
        elif current_type == 8:
            if first_value < 0:
                self.errors = ('Scale parameter (λ) must be positive.'
                                  if language_type == 'en' else
                                 'Skalenparameter (λ) muss positiv sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.exponential(first_value, size=size)
        elif current_type == 9:
            if first_value < 0:
                self.errors = ('Degree of freedom (v) must be positive.'
                                  if language_type == 'en' else
                                 'Der Freiheitsgrad (v) muss positiv sein.'
                                 if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            data = np.random.standard_t(first_value, size=size)

        # Clear the existing plot
        for child in self.box.children[:]:
            if isinstance(child, FigureCanvasKivyAgg):
                self.box.remove_widget(child)

        subplot_width = 0.5
        subplot_height = 0.7

        # Create subplots with defined sizes
        fig, axs = plt.subplots(2, 1, figsize=(8, 16), gridspec_kw={"width_ratios": [subplot_width],
                                                                   "height_ratios": [subplot_height, subplot_height]})


        #fig, axs = plt.subplots(2, 1, figsize=(8, 15))
        mpl.rcParams['font.size'] = 16
        label_font_size = 16

        # Plot the histogram
        axs[0].hist(data, bins='auto', alpha=0.7, rwidth=0.85)
        axs[0].set_title((f'Histogram of a {current_type_name} distribution'
                                  if language_type == 'en' else
                                 'Histogramm von a {current_type_name} Verteilung'
                                 if language_type == 'de' else None))
        axs[0].set_ylabel(('Frequency' if language_type == 'en' else
                                 'Frequenz'
                                 if language_type == 'de' else None), fontsize=label_font_size)

        # Plot the line plot
        axs[1].plot(data)
        axs[1].set_ylabel(('Value' if language_type == 'en' else
                                 'Wert'
                                 if language_type == 'de' else None))

        mean_value = np.mean(data)  # Calculate the mean of the data

        # Add the dashed line at the mean
        axs[1].axhline(mean_value, color='r', linestyle='--', label=('Mean' if language_type == 'en' else
                                 'Bedeuten' if language_type == 'de' else None))
        axs[1].legend(fontsize=label_font_size)
        axs[1].set_ylabel(('Value' if language_type == 'en' else
                                 'Wert'
                                 if language_type == 'de' else None), fontsize=label_font_size)

        # Create a FigureCanvasKivyAgg and add it to the box layout
        canvas = FigureCanvasKivyAgg(fig)
        self.box.add_widget(canvas)

        plt.close(fig)  # Close the figure to release resources

        self.errors = ''

    def go_to_start_screen(self, instance, touch):
        if touch.is_double_tap:
            self.clear_widgets()  # Clear all widgets in the box layout
            self.manager.current = 'home_page'

    def on_leave(self):
        # Clear previous content
        self.clear_widgets()



class SecondPage(Screen):

    def on_enter(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        self.errors = ''
        self.popups = []
        global current_type
        global current_type_name
        global needed_inputs
        global first_inputs
        global second_inputs
        global first_input_name
        global second_input_name
        global first_input_needs_int
        global second_input_needs_int

        self.box = BoxLayout(orientation='vertical', spacing=10, padding=30)
        # self.box.height = 100  # Adjust the height value as desired

        # Instructions label
        self.CLT_title = Label(text=(f'{current_type_name} CLT' if language_type == 'en' else
                                 f'{current_type_name} ZGWS'
                                 if language_type == 'de' else None),
                               size_hint=(1, 0.1), font_size=50, color=(0, 1, 0),
                               pos_hint={'center_x': 0.5, 'center_y': 1})

        # possible description label
        self.CLT_description = Button(text=('Visualization Described' if language_type == 'en' else
                                 'Visualisierung beschrieben'
                                 if language_type == 'de' else None), size_hint=(1, 0.1), pos_hint={
            'center_x': 0.5}, color=(1, 1, 1), font_size=50)
        self.CLT_description.background_color = (1, 0, 0, 1)
        self.CLT_description.bind(on_press=self.CLT_popup)
        self.box.add_widget(self.CLT_title)

        self.iterations_slider = Slider(min=2, max=30, value=10, value_track=True, value_track_color=[0.5, 0.7, 0.8, 1],
                                   height=50, size_hint=(0.95, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.iterations_text = Label(text=(f'Slide to input the number of i.i.d. distributions' if language_type == 'en' else
                                 'Schieben Sie, um die Anzahl der i.i.d. einzugeben. Verteilungen'
                                 if language_type == 'de' else None), height=100,
                                     size_hint=(0.9, None), font_size=39, halign='center', valign = 'bottom',
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.iterations_slider.bind(value=lambda instance, value: (setattr(self.iterations_text, 'text',
                f'Number of sample i.i.d. distributions:  '
                f'{round(self.iterations_slider.value)}') if language_type == 'en' else
                                 setattr(self.iterations_text, 'text',
                f'Anzahl der Proben i.i.d. Verteilungen:  '
                f'{round(self.iterations_slider.value)}')))

        self.iterations_slider.bind(value=self.create_plot)

        self.box.add_widget(self.CLT_description)
        self.box.add_widget(self.iterations_text)
        self.box.add_widget(self.iterations_slider)

        # Add the label widget
        self.simulations_text = Label(text=('Number of Simulations' if language_type == 'en' else
                                 'Anzahl der Simulationen'
                                 if language_type == 'de' else None),
                                      size_hint=(1, 0.1),
                                      font_size=50,
                                      halign='center',
                                      valign='center',
                                      text_size=(self.width, None),
                                      color=(0, 1, 0),
                                      pos_hint={'center_x': 0.5, 'center_y': 1})
        self.simulations_text.bind(
            texture_size=lambda instance, value: setattr(self.simulations_text, 'height', value[1]))
        self.N_input = 1000
        self.N_input = Spinner(
            # default value shown
            text=('Default is 1000. Press to change.' if language_type == 'en' else
                                 'Der Standardwert ist 1000.'
                                 if language_type == 'de' else None),
            halign='center',
            # available values
            values=('100', '1000', '5000', '10000', '100000'),
            # just for positioning in our example
            size_hint=(0.5, 0.1),
            height=50,
            font_size=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.N_input.background_color = (1, 0.7, 0, 1)
        self.N_input.size_hint_x = 1

        self.box.add_widget(self.simulations_text)
        self.box.add_widget(self.N_input)

        self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(0.95, 0.2), height=20, pos_hint={
            'center_x': 0.5})

        self.sub_box_1 = BoxLayout(orientation='horizontal', spacing=10, size_hint=(0.95, 0.2), height=20, pos_hint={
            'center_x': 0.5})

        self.errors = ''
        self.dist_text = Label(
            text=(f' \nInput distribution parameters' if language_type == 'en' else
                                 ' \nEingabeverteilungsparameter'
                                 if language_type == 'de' else None),
            size_hint=(1, 0.05),
            font_size=39,
            halign='center',
            valign='center',
            color=(0, 1, 0))

        self.dist_text.bind(
            texture_size=lambda instance, value: setattr(self.dist_text, 'height', value[1]))
        self.box.add_widget(self.dist_text)

        if needed_inputs == 1:
            self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))
            self.sub_box_1 = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 1))

            self.first_input_1 = Label(text=f'{first_input_name}',
                                       size_hint=(0.5, 1), font_size=39, color=(1, 0, 1),
                                       pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),
                                           font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                           foreground_color=(0, 0, 1))
            self.first_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

        elif needed_inputs == 2:
            self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.15))
            self.sub_box_1 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))

            self.first_input_1 = Label(text=f'{first_input_name}',
                                       size_hint=(0.5, 1), font_size=39, color=(1, 0, 1),
                                       pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),
                                           font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                           foreground_color=(0, 0, 1))
            self.first_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

            self.sub_box_2 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))
            self.second_input_1 = Label(text=f'{second_input_name}',
                                        size_hint=(0.5, 1), font_size=39, color=(1, 0, 1),
                                        pos_hint={'center_x': 0.5, 'center_y': 1})
            self.second_input_2 = TextInput(hint_text=second_input_name, size_hint=(1, 1),
                                            font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                            foreground_color=(0, 0, 1))
            self.second_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_2.add_widget(self.second_input_1)
            self.sub_box_2.add_widget(self.second_input_2)
            self.sub_box.add_widget(self.sub_box_2)

        self.box.add_widget(self.sub_box)

        empty_text = Label(text=' ', size_hint=(1, .1), size=(100, 200),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.2, 0.8, 0.2))
        empty_text.bind(
            height=lambda *x: empty_text.setter('text_size')(empty_text, (empty_text.height, None)))
        self.box.add_widget(empty_text)

        provide_text = Label(text=('Made possible by Banana Shaped Cow Studios' if language_type == 'en' else
                             'Ermöglicht durch Banana Shaped Cow Studios' if language_type == 'de' else None),
                             size_hint=(1, None), size=(100, 100),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.5, 0.8, 0.5))

        provide_text.bind(
            height=lambda *x: provide_text.setter('text_size')(provide_text, (provide_text.height, None)))
        self.box.add_widget(provide_text)

        #self.box.add_widget(self.sub_box_1)
        self.add_widget(self.box)

    def CLT_popup(self, instance):
        popup_x_size = 400 * 2.2
        popup_y_size = 350 * 2.9
        # Create a label with the message
        message_label = Label(text='', size_hint=(1, None), pos_hint={'center_y': 0.6}, halign='center',
                                  font_size=50)

        message_label.text =(f'First set the number (N) of independent identical distributed  (i.i.d.) samples to be ' \
                                 f'created by using the slider below. Then,  set the number (S) of simulated values for ' \
                                 f'each of the distributions. The program will calculate the average of the N ' \
                                 f'distributions for each of the S simulations and generate a histogram. For comparison ' \
                                 f'purpose, the histogram of one of the i.i.d. distributions will also be generated.'
                             if language_type == 'en' else
                             f'Legen Sie zunächst die Anzahl (N) der unabhängigen, identisch verteilten (i.i.d.) ' \
                             f'Stichproben fest, die erstellt werden sollen, indem Sie den Schieberegler unten ' \
                             f'verwenden. Legen Sie dann die Anzahl (S) der simulierten Werte für jede der ' \
                             f'Verteilungen fest. Das Programm berechnet den Durchschnitt der N Verteilungen für ' \
                             f'jede der S Simulationen und erstellt ein Histogramm. Zu Vergleichszwecken das ' \
                             f'Histogramm eines der i.i.d. Es werden auch Ausschüttungen generiert.'
                             if language_type == 'de' else None)

        message_label.bind(width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width,
                                                                                                  None)))

        # Create the popup and set its content
        popup = Popup(title='', separator_height=0, content=message_label, size_hint=(None, None),
                          size=(popup_x_size, popup_y_size))
        # Open the popup
        popup.open()

    def create_plot(self, instance, idk):
        global current_type
        global current_type_name
        global needed_inputs
        global first_input_name
        global second_input_name
        global first_input_needs_int
        global second_input_needs_int
        global data1
        first_value = None
        second_value = None
        data = None
        self.errors = ''

        if not first_input_needs_int:
            try:
                first_value = float(self.first_input_2.text)
            except ValueError:
                self.errors = (f'{first_input_name} must be a number.'
                             if language_type == 'en' else
                              f'{first_input_name} muss eine Nummer sein.'
                             if language_type == 'de' else None)

                self.show_error_popup(1)
                return
        elif first_input_needs_int:
            try:
                first_value = int(self.first_input_2.text)
            except ValueError:
                self.errors = (f'{first_input_name} must be an integer.'
                             if language_type == 'en' else
                              f'{first_input_name} muss eine ganze Zahl sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
        if needed_inputs >= 2:
            if not second_input_needs_int:
                try:
                    second_value = float(self.second_input_2.text)
                except ValueError:
                    self.errors = (f'{second_input_name} must be a number.'
                             if language_type == 'en' else
                              f'{second_input_name} muss eine Nummer sein.'
                             if language_type == 'de' else None)
                    self.show_error_popup(1)
                    return
            elif second_input_needs_int:
                try:
                    second_value = int(self.second_input_2.text)
                except ValueError:
                    self.errors = (f'{second_input_name} must be an integer.'
                             if language_type == 'en' else
                              f'{second_input_name} muss eine ganze Zahl sein.'
                             if language_type == 'de' else None)
                    self.show_error_popup(1)
                    return

        try:
            size = int(self.N_input.text)
        except ValueError:
            size = 1000

        if current_type == 1:
            if second_value <= 0:
                self.errors = ('Standard deviation (σ) must be greater than 0.'
                             if language_type == 'en' else
                              'Die Standardabweichung (σ) muss größer als 0 sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.normal(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)

        elif current_type == 2:
            if first_value <= 0:
                self.errors = ('Rate (λ) must be greater than 0.'
                             if language_type == 'en' else
                              'Rate (λ) muss größer als 0 sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.poisson(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)

        elif current_type == 3:
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                             if language_type == 'en' else
                              'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            if not 0 <= second_value <= 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                             if language_type == 'en' else
                              'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.binomial(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)
        elif current_type == 4:
            if not first_value >0:
                self.errors = ('Shape (α) must be greater than 0.'
                             if language_type == 'en' else
                              'Form (α) muss größer als 0 sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            if not second_value > 0:
                self.errors = ('Shape (β) must be greater than 0.'
                             if language_type == 'en' else
                              'Form (β) muss größer als 0 sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.beta(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)
        elif current_type == 5:
            if not 0 < second_value < 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                             if language_type == 'en' else
                              'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                             if language_type == 'en' else
                              'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.negative_binomial(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)
        elif current_type == 6:
            vector = np.random.uniform(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)
        elif current_type == 7:
            if first_value < 0:
                self.errors = ('Degree of freedom (κ) must be positive.'
                             if language_type == 'en' else
                              'Der Freiheitsgrad (κ) muss positiv sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.chisquare(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)
        elif current_type == 8:
            if first_value < 0:
                self.errors = ('Scale parameter (λ) must be positive.'
                             if language_type == 'en' else
                              'Skalenparameter (λ) muss positiv sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.exponential(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)
        elif current_type == 9:
            if first_value < 0:
                self.errors = ('Degree of freedom (v) must be positive.'
                             if language_type == 'en' else
                              'Der Freiheitsgrad (v) muss positiv sein.'
                             if language_type == 'de' else None)
                self.show_error_popup(1)
                return
            vector = np.random.standard_t(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1)/round(self.iterations_slider.value)

        plt.cla()
        self.fig, self.axs = plt.subplots(2, 1, figsize=(8, 22))
        matplotlib.pyplot.close('all')

        # Clear the existing plot
        for child in self.box.children[:]:
            if isinstance(child, FigureCanvasKivyAgg):
                self.box.remove_widget(child)

        mpl.rcParams['font.size'] = 16
        label_font_size = 16

        # Plot the histogram
        # Plot the histograms
        # Determine the common x-axis limits
        min_value = min(min(averaged_data), min(data1))
        max_value = max(max(averaged_data), max(data1))

        # Determine the number of bins
        num_bins = 'auto'  # You can choose any method mentioned earlier to determine the number of bins
        bar_width = 0.4  # Adjust the width of the bars
        offset = 0.2  # Adjust the spacing between histograms

        # Plot the histograms with consistent bar width
        self.axs[0].hist(averaged_data, bins=num_bins, alpha=0.7, rwidth=1, range=(min_value, max_value))
        self.axs[0].set_title((f'Histogram of the average of  {round(self.iterations_slider.value)}'
                              f'\ni.i.d. {current_type_name} distributions'
                             if language_type == 'en' else
                              f'Histogramm des Durchschnitts von  {round(self.iterations_slider.value)}'
                              f'\ni.i.d. {current_type_name} Verteilungen'
                             if language_type == 'de' else None), fontsize=20)
        self.axs[1].hist(data1, bins=num_bins, alpha=0.7, rwidth=1, range=(min_value, max_value))
        self.axs[1].set_title((f'Histogram of one {current_type_name} distribution'
                             if language_type == 'en' else
                              f'Histogramm von einem {current_type_name} Verteilungen'
                             if language_type == 'de' else None), fontsize=16)

        # Set y-axis labels
        label_font_size = 12
        self.axs[0].set_ylabel(('Frequency'
                             if language_type == 'en' else
                              f'Frequenz' if language_type == 'de' else None), fontsize=label_font_size)
        self.axs[1].set_ylabel(('Frequency'
                             if language_type == 'en' else
                              f'Frequenz' if language_type == 'de' else None), fontsize=label_font_size)

        # Create a FigureCanvasKivyAgg and add it to the box layout
        canvas = FigureCanvasKivyAgg(self.fig)
        self.box.add_widget(canvas)

        plt.close(self.fig)  # Close the figure to release resources
        matplotlib.pyplot.close(self.fig)

        self.errors = ''

    def on_leave(self):
        # Clear previous content
        self.clear_widgets()

    def show_previous_screen(self, instance):
        self.manager.current = 'second_page'

        self.errors = ''

    def go_to_start_screen(self, instance, touch):
        if touch.is_double_tap:
            self.clear_widgets()  # Clear all widgets in the box layout
            self.manager.current = 'home_page'

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'second_page':
            # do what you want, return True for stopping the propagation
            self.show_previous_screen(1)
            return True

    def show_error_popup(self, instance):
        popup_x_size = 350 * 2.2
        popup_y_size = 230 * 2.2

        message_label = Label(text=self.errors, size_hint=(1, None), pos_hint={'center_y': 0.6}, halign='center',
                        font_size = 50, color=(1, 0, 0))

        message_label.bind(
            width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width,
                                                                               None)))

        for popup1 in self.popups:
            popup1.dismiss()

        # Create the popup and set its content
        popup = Popup(title=('Error'
                             if language_type == 'en' else
                              f'Fehler' if language_type == 'de' else None), content=message_label,
                      size_hint=(None, None), size=(popup_x_size, popup_y_size))
        self.popups.append(popup)
        # Open the popup
        popup.open()

    def on_leave(self):
        # Clear previous content
        self.clear_widgets()

    def show_previous_screen(self, instance):
        self.manager.current = 'first_page'

class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        language_page = LanguagePage(name='language_page')
        self.screen_manager.add_widget(language_page)

        home_page = HomePage(name='home_page')
        self.screen_manager.add_widget(home_page)

        first_page = FirstPage(name='first_page')
        self.screen_manager.add_widget(first_page)

        second_page = SecondPage(name='second_page')
        self.screen_manager.add_widget(second_page)

        return self.screen_manager


if __name__ == '__main__':
    MainApp().run()


