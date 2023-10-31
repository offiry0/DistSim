import numpy as np
import matplotlib
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib as mpl
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
from kivy.core.text import LabelBase
#import os
import matplotlib.font_manager as fm
from kivy.graphics import Color, Rectangle
from kivy.config import Config
#Config.set('kivy', 'simfang', 'simfang')
from kivy.uix.label import Label
from kivy.core.text import FontContextManager as FCM

LabelBase.register(name="cn", fn_regular="csongl.ttf")
LabelBase.register(name="eng", fn_regular="hnfsasr.ttf")
LabelBase.register(name="abc", fn_regular="BRUSHSCI.ttf")


class SpinnerOptions(SpinnerOption):

    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = [0, 0, 1, 1]  # blue colour
        self.height = 26

class SpinnerDropdown(DropDown):

    def __init__(self, **kwargs):
        super(SpinnerDropdown, self).__init__(**kwargs)
        self.auto_width = False
        self.width = 100

class SpinnerWidget(Spinner):
    def __init__(self, **kwargs):
        super(SpinnerWidget, self).__init__(**kwargs)
        self.dropdown_cls = SpinnerDropdown
        self.option_cls = SpinnerOptions


Window.clearcolor = (0, 0, 0, 1)
current_type = 0

global language_type
language_type = 'en'

class LanguagePage(Screen):
    global language_type

    def on_enter(self):
        with self.canvas.before:
            Color( 9 / 256,  7 / 256,  1 / 256, 1)  # Set the background color (in this example, red)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        kivy_defaulttheme_color = np.array([88, 88, 88, 256]) / 256
        desired_button_color = np.array([247, 247, 246, 256]) / 256
        tintshade_color = desired_button_color# / kivy_defaulttheme_color*0

        self.box_a1 = BoxLayout(orientation='vertical', padding=130, spacing=20)

        self.box_b1 = BoxLayout(orientation='vertical', size_hint=(1, 0.60))
        self.sub_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.60))
        self.sub_box_b1 = BoxLayout(orientation='horizontal', spacing=120, size_hint=(1, 0.20))

        b1_image_1 = Image(source='Dist2.png')
        b1_text_1 = Label(text="", font_size=16, color=(0.1, 0.1, 0.1), size_hint=(0.4, 0.05),
                          halign='center', valign='center', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # Create Plot button
        screen_width, screen_height = Window.size
        button_width = screen_width * 0.28
        button_height = screen_height * 0.18
        wh_size=(button_width+ button_height)/2

        # Create a button with the calculated size
        self.sub_b1_button_1 = Button(text='Welcome to\nDistSim', font_size=5, color=(0, 0.5, 0.3),
                                      size_hint=(None, None), size=(wh_size, wh_size),
                                      background_normal='LAN_American.png',
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                   background_color=tintshade_color, halign = 'center')
        self.sub_b1_button_2 = Button(text='Willkommen zu\nDistSim', font_size=5, color=(0, 0.6, 0.1),
                                  size_hint=(None, None), size=(wh_size, wh_size),
                                      background_normal='LAN_German.png',
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                  background_color=tintshade_color, halign = 'center')
        self.sub_box_b2 = BoxLayout(orientation='horizontal', spacing=120, size_hint=(1, 0.20))
        self.sub_b2_button_1 = Button(text='Bienvenue à\nDistSim', font_size=5, color=(0.6, 0, 0.6),
                                      size_hint=(None, None), size=(wh_size, wh_size),
                                      background_normal='LAN_French.png',pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                  background_color=tintshade_color, halign = 'center')
        self.sub_b2_button_2 = Button(text='欢迎', font_name=('cn' if language_type == 'cn' else 'eng'),
                                      font_size=5, color=(0.0, 0.3, 0.5),pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                  size_hint=(None, None), size=(wh_size, wh_size),
                                      background_normal='LAN_China.png',
                                  background_color=tintshade_color, halign = 'center')
        self.sub_b1_button_1.bind(on_press=self.switch_language_en)
        self.sub_b1_button_2.bind(on_press=self.switch_language_de)
        self.sub_b2_button_1.bind(on_press=self.switch_language_fr)
        self.sub_b2_button_2.bind(on_press=self.switch_language_cn)

        self.sub_b1_button_1.bind(on_press=self.go_to_home_page)
        self.sub_b1_button_2.bind(on_press=self.go_to_home_page)
        self.sub_b2_button_1.bind(on_press=self.go_to_home_page)
        self.sub_b2_button_2.bind(on_press=self.go_to_home_page)

        self.box_b1.add_widget(b1_image_1)
        self.box_b1.add_widget(b1_text_1)
        self.sub_box_b1.add_widget(self.sub_b1_button_1)
        self.sub_box_b1.add_widget(self.sub_b1_button_2)
        self.sub_box_b2.add_widget(self.sub_b2_button_1)
        self.sub_box_b2.add_widget(self.sub_b2_button_2)

        self.box_a1.add_widget(self.box_b1)
        self.box_a1.add_widget(self.sub_box_b1)
        self.box_a1.add_widget(self.sub_box_b2)
        self.add_widget(self.box_a1)

    def update_language(self, instance):
        if language_type == 'en':
            self.sub_b1_button_1.text = 'Welcome'
            self.sub_b1_button_2.text = 'Willkommen'
            self.sub_b2_button_1.text = 'Bienvenu'
            self.sub_b2_button_2.text = 'Willkommen'
        elif language_type == 'de':
            self.sub_b2_button_1.text = 'Welcome'
            self.sub_b2_button_2.text = 'Willkommen'

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

    def switch_language_fr(self, instance):
        global language_type
        language_type = language_type
        language_type = 'fr'
        self.update_language(1)

    def switch_language_cn(self, instance):
        global language_type
        language_type = language_type
        language_type = 'cn'
        self.update_language(1)

    def go_to_home_page(self, instance):
        self.manager.current = 'home_page'

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_leave(self, *args):
        self.clear_widgets()

Window.clearcolor = (.1, .1, .1, 1)
current_type = 0

class HomePage(Screen):
    def on_enter(self):
        global language_type
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        self.box = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, padding=30)
        self.scroll_box = ScrollView()
        self.box.bind(minimum_height=self.box.setter('height'))
        button1 = Button(text=('Normal' if language_type == 'en' else
                               'Normal' if language_type == 'de' else
                               'Normal' if language_type == 'fr' else
                               '正态分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), font_name=('cn' if language_type == 'cn' else 'eng'),
                         pos_hint={'center_x': 0.5},
                         font_size=80)
        button1.background_color = (1, 0, 0, 1)
        button2 = Button(text=('Poisson' if language_type == 'en' else
                               'Poisson' if language_type == 'de' else
                               'Poisson' if language_type == 'fr' else
                               '泊松分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160),font_name=('cn' if language_type == 'cn' else 'eng'),
                         pos_hint={'center_x': 0.5},
                         font_size=80)
        button2.background_color = (1, 0.7, 0, 1)
        button3 = Button(text=('Binomial' if language_type == 'en' else
                               'Binomial' if language_type == 'de' else
                               'Binomial' if language_type == 'fr' else
                               '二项分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button3.background_color = (0.7, 1, 0, 1)
        button4 = Button(text=('Beta' if language_type == 'en' else
                               'Beta' if language_type == 'de' else
                               'Beta' if language_type == 'fr' else
                               '贝塔分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button4.background_color = (0, 1, 0, 1)
        button5 = Button(text=('Negative Binomial' if language_type == 'en' else
                               'Negatives Binomial' if language_type == 'de' else
                               'Binôme négatif' if language_type == 'fr' else
                               '负二项式分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button5.background_color = (0, 1, 0.7, 1)
        button6 = Button(text=('Continuous Uniform' if language_type == 'en' else
                               'Kontinuierliche Uniform' if language_type == 'de' else
                               'Uniforme continu' if language_type == 'fr' else
                               '连续均匀分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button6.background_color = (0, 0.7, 1, 1)
        button7 = Button(text=('Chi-squared' if language_type == 'en' else
                               'Chi-quadrat' if language_type == 'de' else
                               'Chi-carré' if language_type == 'fr' else
                               '卡方分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button7.background_color = (0, 0, 1, 1)
        button8 = Button(text=('Exponential' if language_type == 'en' else
                               'Exponentiell' if language_type == 'de' else
                               'Exponentiel' if language_type == 'fr' else
                               '指数分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button8.background_color = (0.7, 0, 1, 1)
        button9 = Button(text=('Student\'s t' if language_type == 'en' else
                               'Student\'s t' if language_type == 'de' else
                               't de Student' if language_type == 'fr' else
                               '学生t分布' if language_type == 'cn' else None),
                         size_hint=(0.95, None), size=(100, 160), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                         font_size=80)
        button9.background_color = (1, 0, 0.7, 1)

        welcome_text = Label(text='DistSim', size_hint=(None, None), size=(100, 180),font_name=('abc'),
                             pos_hint={'center_x': 0.5},
                             font_size=75, color=(0.65, 0.65, 0))

        provide_text = Label(text=('Made possible by Banana Shaped Cow Studios' if language_type == 'en' else
                                   'Ermöglicht durch Banana Shaped Cow Studios' if language_type == 'de' else
                                   'Rendu possible par Banana Shaped Cow Studios' if language_type == 'fr' else
                                   'Banana Shaped Cow Studios 制作' if language_type == 'cn' else None),
                             size_hint=(1, None), size=(100, 100),font_name=('cn' if language_type == 'cn' else 'eng'),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.8, 0.8, 0))
        welcome_description = Label(text=('The app offers visualizations of various important probability '
                                          'distributions, making it a convenient and engaging way to utilize a '
                                          'two-minute break.' if language_type == 'en' else
                                          'Die App bietet Visualisierungen verschiedener wichtiger '
                                          'Wahrscheinlichkeitsverteilungen und ist damit eine bequeme und '
                                          'ansprechende Möglichkeit, eine zweiminütige Pause zu nutzen.'
                                          if language_type == 'de' else
                                          'L\'application offre des visualisations de diverses distributions de '
                                          'probabilité importantes, ce qui en fait un moyen pratique et attrayant d'
                                          'utiliser une pause de deux minutes.'
                                          if language_type == 'fr' else
                                          '该应用程序提供各种重要概率分布的可视化，使其成为利用休息时间进行的一种轻松的休闲和学习的方式。'
                                          if language_type == 'cn' else None),
                                    size_hint=(0.9, None), size=(100, 350),font_name=('cn' if language_type == 'cn' else 'eng'),
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

    def on_button_press(self, instance, page_number):
        global current_type
        current_type = page_number
        self.manager.current = 'first_page'

    def show_language_screen(self, instance):
        self.manager.current = 'language_page'

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'home_page':
            # do what you want, return True for stopping the propagation
            self.show_language_screen(1)
            return True

    def on_leave(self):
        # Clear previous content
        self.clear_widgets()


class FirstPage(Screen):
    def on_enter(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        global current_type
        global current_type_name
        global current_type_nameG
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
            current_type_name = ('Normal' if language_type == 'en' else
                                 'Normal' if language_type == 'de' else
                                 'Normal' if language_type == 'fr' else
                                 '正态分布' if language_type == 'cn' else None)
            current_type_nameG = ('Normal Distribution' if language_type == 'en' else
                                  'Normalverteilung' if language_type == 'de' else
                                  'Distribution normale' if language_type == 'fr' else
                                  '正态分布' if language_type == 'cn' else None)
            needed_inputs = 2
            first_input_name = ('Mean (μ)' if language_type == 'en' else
                                'Bedeuten (μ)' if language_type == 'de' else
                                'Moyenne (μ)' if language_type == 'fr' else
                                '平均值(μ)' if language_type == 'cn' else None)
            second_input_name = ('Standard Deviation (σ)' if language_type == 'en' else
                                 'Standardabteilung (σ)' if language_type == 'de' else
                                 'Écart type (σ)' if language_type == 'fr' else
                                 '标准偏差(σ)' if language_type == 'cn' else None)
        elif current_type == 2:
            current_type_name = ('Poisson' if language_type == 'en' else
                                 'Poisson' if language_type == 'de' else
                                 'Poisson' if language_type == 'fr' else
                                 '泊松分布' if language_type == 'cn' else None)
            current_type_nameG = ('Poisson Distribution' if language_type == 'en' else
                                  'Poisson-Verteilung' if language_type == 'de' else
                                  'Loi de Poisson' if language_type == 'fr' else
                                  '泊松分布' if language_type == 'cn' else None)
            needed_inputs = 1
            first_input_name = ('Rate (λ)' if language_type == 'en' else
                                'Rate (λ)' if language_type == 'de' else
                                'Taux (l)' if language_type == 'fr' else
                                '比率(l)' if language_type == 'cn' else None)
        elif current_type == 3:
            current_type_name = ('Binomial' if language_type == 'en' else
                                 'Binomial' if language_type == 'de' else
                                 'Binôme' if language_type == 'fr' else
                                 '二项分布' if language_type == 'cn' else None)
            current_type_nameG = ('Binomial Distribution' if language_type == 'en' else
                                  'Binomialverteilung' if language_type == 'de' else
                                  'Distribution binomiale' if language_type == 'fr' else
                                  '二项分布' if language_type == 'cn' else None)
            needed_inputs = 2
            first_input_name = ('Experiment Count (n)' if language_type == 'en' else
                                'Anzahl der Experimente (n)' if language_type == 'de' else
                                'Nombre d\'expériences (n)' if language_type == 'fr' else
                                '试验次数(n)' if language_type == 'cn' else None)
            first_input_needs_int = True
            second_input_name = ('Success Rate (p)' if language_type == 'en' else
                                 'Erfolgsrate (p)' if language_type == 'de' else
                                 'Taux de réussite (p)' if language_type == 'fr' else
                                 '成功概率(p)' if language_type == 'cn' else None)
        elif current_type == 4:
            current_type_name = ('Beta' if language_type == 'en' else
                                 'Beta' if language_type == 'de' else
                                 'Bêta' if language_type == 'fr' else
                                 '贝塔分布' if language_type == 'cn' else None)
            current_type_nameG = ('Beta Distribution' if language_type == 'en' else
                                  'Beta-Verteilung' if language_type == 'de' else
                                  'Distribution bêta' if language_type == 'fr' else
                                  '贝塔分布' if language_type == 'cn' else None)
            needed_inputs = 2
            first_input_name = ('Shape 1 (α)' if language_type == 'en' else
                            'Form 1 (α)' if language_type == 'de' else
                            'Forme 1 (α)' if language_type == 'fr' else
                            '形状参数1(α)' if language_type == 'cn' else None)
            second_input_name = ('Shape 2 (β)' if language_type == 'en' else
                             'Form 2 (β)' if language_type == 'de' else
                             'Forme 2 (β)' if language_type == 'fr' else
                             '形状参数2(β)' if language_type == 'cn' else None)

        elif current_type == 5:
            current_type_name = ('Negative Binomial' if language_type == 'en' else
                         'Negatives Binomial' if language_type == 'de' else
                         'Binôme négatif' if language_type == 'fr' else
                         '负二项分布' if language_type == 'cn' else None)
            current_type_nameG = ('Negative Binomial Distribution' if language_type == 'en' else
                          'Negative Binomialverteilung' if language_type == 'de' else
                          'Distribution binomiale négative' if language_type == 'fr' else
                          '负二项分布' if language_type == 'cn' else None)
            needed_inputs = 2
            first_input_name = ('Success Count (r)' if language_type == 'en' else
                    'Erfolgszählung (r)' if language_type == 'de' else
                    'Nombre de succès (r)' if language_type == 'fr' else
                    '成功次数(r)' if language_type == 'cn' else None)
            first_input_needs_int = True
            second_input_name = ('Success Rate (p)' if language_type == 'en' else
                     'Erfolgsrate (p)' if language_type == 'de' else
                     'Taux de réussite (p)' if language_type == 'fr' else
                     '成功率(p)' if language_type == 'cn' else None)
        elif current_type == 6:
            current_type_name = ('Continuous Uniform' if language_type == 'en' else
                     'Kontinuierliche Uniform' if language_type == 'de' else
                     'Uniforme continu' if language_type == 'fr' else
                     '连续均匀分布' if language_type == 'cn' else None)
            current_type_nameG = ('Continuous Uniform Distribution' if language_type == 'en' else
                      'Kontinuierliche Uniform' if language_type == 'de' else
                      'Distribution Uniforme Continue' if language_type == 'fr' else
                      '连续均匀分布' if language_type == 'cn' else None)
            needed_inputs = 2
            first_input_name = ('Lower Bound (a)' if language_type == 'en' else
                    'Untergrenze (a)' if language_type == 'de' else
                    'Borne inférieure (a)' if language_type == 'fr' else
                    '下限(a)' if language_type == 'cn' else None)
            second_input_name = ('Upper Bound (b)' if language_type == 'en' else
                     'Obere Grenze (b)' if language_type == 'de' else
                     'Limite supérieure (b)' if language_type == 'fr' else
                     '上限(b)' if language_type == 'cn' else None)
        elif current_type == 7:
            current_type_name = ('Chi-squared' if language_type == 'en' else
                     'Chi-quadrat' if language_type == 'de' else
                     'Chi-carré' if language_type == 'fr' else
                     '卡方分布' if language_type == 'cn' else None)
            current_type_nameG = ('Chi-squared Distribution' if language_type == 'en' else
                      'Chi-Quadrat-Verteilung' if language_type == 'de' else
                      'Distribution du chi carré' if language_type == 'fr' else
                      '卡方分布' if language_type == 'cn' else None)
            needed_inputs = 1
            first_input_name = ('Degree of freedom (κ)' if language_type == 'en' else
                    'Freiheitsgrad (κ)' if language_type == 'de' else
                    'Degré de liberté (κ)' if language_type == 'fr' else
                    '自由度(κ)' if language_type == 'cn' else None)
            first_input_needs_int = True
        elif current_type == 8:
            current_type_name = ('Exponential' if language_type == 'en' else
                     'Exponentiell' if language_type == 'de' else
                     'Exponentiel' if language_type == 'fr' else
                     '指数分布' if language_type == 'cn' else None)
            current_type_nameG = ('Exponential Distribution' if language_type == 'en' else
                      'Exponentialverteilung' if language_type == 'de' else
                      'Distribution exponentielle' if language_type == 'fr' else
                      '指数分布' if language_type == 'cn' else None)
            needed_inputs = 1
            first_input_name = ('Scale (λ)' if language_type == 'en' else
                    'Scale (λ)' if language_type == 'de' else
                    'Échelle (λ)' if language_type == 'fr' else
                    '速率参数(λ)' if language_type == 'cn' else None)
        elif current_type == 9:
            current_type_name = ('Student\'s t' if language_type == 'en' else
                      'Schüler t' if language_type == 'de' else
                      't de l\'étudiant' if language_type == 'fr' else
                      '学生t分布' if language_type == 'cn' else None)
            current_type_nameG = ('Student\'s t Distribution' if language_type == 'en' else
                      'Student\'s t-Verteilung' if language_type == 'de' else
                      'Distribution t de Student' if language_type == 'fr' else
                      '学生t分布' if language_type == 'cn' else None)
            needed_inputs = 1
            first_input_name = ('Degree of freedom (ν)' if language_type == 'en' else
                    'Freiheitsgrad (ν)' if language_type == 'de' else
                    'Degré de liberté (ν)' if language_type == 'fr' else
                    '自由度(ν)' if language_type == 'cn' else None)
            first_input_needs_int = True

        self.box = BoxLayout(orientation='vertical', spacing=10, padding=30)

        # Instructions label
        self.Apptitle = Label(text=f'{current_type_nameG}',font_name=('cn' if language_type == 'cn' else 'eng'),
                              size_hint=(1, 0.1), font_size=50, color=(0, 1, 0),
                              pos_hint={'center_x': 0.5, 'center_y': 1})

        # possible description label
        self.description = Button(text=('Show Description' if language_type == 'en' else
                                        'Beschreibung Anzeigen' if language_type == 'de' else
                                        'Montrer la description' if language_type == 'fr' else
                                        '显示说明' if language_type == 'cn' else None),
                                  size_hint=(1, 0.1), pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                                  color=(1, 1, 1), font_size=50)
        self.description.background_color = (1, 0, 0, 1)
        self.description.bind(on_press=self.show_popup)
        self.box.add_widget(self.Apptitle)
        self.box.add_widget(self.description)

        # Add the label widget
        self.simulations_text = Label(text=('Number of Simulations' if language_type == 'en' else
                                            'Anzahl der Simulationen' if language_type == 'de' else
                                            'Nombre de simulations' if language_type == 'fr' else
                                            '模拟次数' if language_type == 'cn' else None),
                                      size_hint=(1, 0.1),
                                      font_size=50,font_name=('cn' if language_type == 'cn' else 'eng'),
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
            text=('Default is 10000. Click to change.' if language_type == 'en' else
                  'Der Standardwert ist 10000.' if language_type == 'de' else
                  'La valeur par défaut est 10000.' if language_type == 'fr' else
                  '默认值为10000，单击以更改。' if language_type == 'cn' else None),
            halign='center',
            # available values
            values=('100', '1000', '5000', '10000', '100000'),
            # just for positioning in our example
            size_hint=(0.5, 0.1),font_name=('cn' if language_type == 'cn' else 'eng'),
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
                  f' \nEingabeverteilungsparameter' if language_type == 'de' else
                  f' \nParamètres de distribution d\'entrée' if language_type == 'fr' else
                  f' \n输入分布参数' if language_type == 'cn' else None),
        size_hint = (1, 0.05),
        font_size = 43,font_name=('cn' if language_type == 'cn' else 'eng'),
        halign = 'center',
        valign = 'center',
        color = (0, 1, 0))

        self.dist_text.bind(
            texture_size=lambda instance, value: setattr(self.dist_text, 'height', value[1]))
        self.box.add_widget(self.dist_text)

        if needed_inputs == 1:
            self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.25))
            self.sub_box_1 = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 1))

            self.first_input_1 = Label(text=f'{first_input_name}',
                                       size_hint=(0.5, 1), font_size=30, color=(1, 0, 1),font_name=('cn' if
                                                                                                    language_type == 'cn' else 'eng'),
                                       pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                           font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                           foreground_color=(0, 0, 1))
            self.first_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

        elif needed_inputs == 2:
            self.sub_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.25))
            self.sub_box_1 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))

            self.first_input_1 = Label(text=f'{first_input_name}',font_name=('cn' if language_type == 'cn' else 'eng'),
                                       size_hint=(0.5, 1), font_size=33, color=(1, 0, 1),
                                       pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                           font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                           foreground_color=(0, 0, 1))
            self.first_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

            self.sub_box_2 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))
            self.second_input_1 = Label(text=f'{second_input_name}',font_name=('cn' if language_type == 'cn' else 'eng'),
                                        size_hint=(0.5, 1), font_size=33, color=(1, 0, 1),
                                        pos_hint={'center_x': 0.5, 'center_y': 1})
            self.second_input_2 = TextInput(hint_text=second_input_name, size_hint=(1, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                            font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                            foreground_color=(0, 0, 1))
            self.second_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_2.add_widget(self.second_input_1)
            self.sub_box_2.add_widget(self.second_input_2)
            self.sub_box.add_widget(self.sub_box_2)

        self.box.add_widget(self.sub_box)

        empty_text = Label(text=' ', size_hint=(1, .1), size=(100, 200),
                           pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                           font_size=30, color=(0.2, 0.8, 0.2))
        empty_text.bind(
            height=lambda *x: empty_text.setter('text_size')(empty_text, (empty_text.height, None)))
        self.box.add_widget(empty_text)
        # Create Plot button
        screen_width, screen_height = Window.size

        # Calculate the desired button size based on a fraction of the screen size
        button_width = screen_width * 0.28
        button_height = screen_height * 0.18
        wh_size=(button_width+ button_height)/1.5

        # Create a button with the calculated size
        button = Button(text=' ', size_hint=(None, None), size=(wh_size, wh_size),
                        font_size=50, halign='center',
                        background_normal='RUN.png',
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.background_color = (1, 1, 1, 1)
        button.bind(on_press=self.create_plot)
        button_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.18), pos_hint={
            'center_x': 0.5, 'center_y': 0.5})
        button_box.background_color = (0,0,0,0)

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
                                   'Ermöglicht durch Banana Shaped Cow Studios' if language_type == 'de' else
                                   'Rendu possible par Banana Shaped Cow Studios' if language_type == 'fr' else
                                   'Banana Shaped Cow Studios 制作' if language_type == 'cn' else None),
                             size_hint=(1, None),
                             pos_hint={'center_x': 0.5},font_name=('cn' if language_type == 'cn' else 'eng'),
                             font_size=30, color=(0.8, 0.8, 0))

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
                                    'Demo zum zentralen\nGrenzwertsatz (ZGWS)' if language_type == 'de' else
                                    'Démonstration du théorème\ncentral limite (TLC)' if language_type == 'fr' else
                                    '中心极限定理' if language_type == 'cn' else None),
                              font_size=40, halign='center',
                              size_hint=(0.5, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                              pos_hint={'center_y': 0.5}, on_press=self.show_second_page)
        button_box_1.background_color = (0, 1, 0.7, 1)
        global button_box_2
        global button_box_3
        button_box_2 = Button(text=('Explanation\nAudio 1' if language_type == 'en' else
                                    'Erklärung\nAudio 1' if language_type == 'de' else
                                    'Explication\nl\'audio 1' if language_type == 'fr' else
                                    '音频讲解 1' if language_type == 'cn' else None),
                              font_size=40, halign='center', size_hint=(0.25, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                              pos_hint={'center_y': 0.5}, on_press=self.play_audio_1)
        button_box_2.background_color = (0, .7, 0.39, 1)
        button_box_3 = Button(text=('Explanation\nAudio 2' if language_type == 'en' else
                                    'Erklärung\nAudio 2' if language_type == 'de' else
                                    'Explication\nl\'audio 2' if language_type == 'fr' else
                                    '音频讲解 2' if language_type == 'cn' else None),
                              font_size=40, halign='center', size_hint=(0.25, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                              pos_hint={'center_y': 0.5}, on_press=self.play_audio_2)
        button_box_3.background_color = (0, .7, 0.39, 1)

        button_box.add_widget(button_box_1)
        button_box.add_widget(button_box_2)
        button_box.add_widget(button_box_3)

        self.add_widget(self.box)


    def play_audio_1(self, instance):
        if audio_1.state != 'play':
            audio_1.play()
            button_box_3.disabled = True
            button_box_2.text = ('Stop\nAudio' if language_type == 'en' else
                                 'Stoppen' if language_type == 'de' else
                                 'Arrêt\nl\'audio' if language_type == 'fr' else
                                 '停止音频' if language_type == 'cn' else None)
            audio_2.stop()
        else:
            audio_1.stop()
            button_box_3.disabled = False
            button_box_2.text = ('Explanation\nAudio 1' if language_type == 'en' else
                                 'Erläuterung\nAudio 1' if language_type == 'de' else
                                 'Explication\nl\'audio 1' if language_type == 'fr' else
                                 '音频讲解 1' if language_type == 'cn' else None)


    def play_audio_2(self, instance):
        if audio_2.state != 'play':
            audio_2.play()
            button_box_2.disabled = True
            button_box_3.text = ('Stop\nAudio' if language_type == 'en' else
                                 'Stoppen' if language_type == 'de' else
                                 'Arrêt\nl\'audio' if language_type == 'fr' else
                                 '停止音频' if language_type == 'cn' else None)
            audio_1.stop()
        else:
            audio_2.stop()
            button_box_2.disabled = False
            button_box_3.text = ('Explanation\nAudio 2' if language_type == 'en' else
                                 'Erläuterung\nAudio 2' if language_type == 'de' else
                                 'Explication\nl\'audio 2' if language_type == 'fr' else
                                 '音频讲解 2' if language_type == 'cn' else None)

    def show_error_popup(self, instance):
        popup_x_size = 350 * 2.2
        popup_y_size = 230 * 2.2

        message_label = Label(text=self.errors, size_hint=(1, None), pos_hint={'center_y': 0.6},
                              halign='left',font_name=('cn' if language_type == 'cn' else 'eng'),
                              font_size=50, color=(1, 0, 0))

        message_label.bind(
            width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width, None)))

        # Create the popup and set its content
        popup = Popup(title=('Error' if language_type == 'en' else
                             'Fehler' if language_type == 'de' else
                             'Erreur' if language_type == 'fr' else
                             '错误' if language_type == 'cn' else None),
                      content=message_label, size_hint=(None, None), size=(popup_x_size, popup_y_size))
        # Open the popup
        popup.open()


    def show_popup(self, instance):
        popup_x_size = 400 * 2.2
        popup_y_size = 380 * 3.9
        # Create a label with the message
        message_label = Label(text='', size_hint=(1, None), pos_hint={'center_y': 0.55},
                              font_name=('cn' if language_type == 'cn' else 'eng'), halign='center', font_size=50)

        if current_type == 1:
            message_label.text = ('A normal (or Gaussian; named after Carl Friedrich Gauss) distribution is a '
                                  'continuous probability distribution for a real-valued random variable. Normal  '
                                  'distribution has two parameters, which are the mean and the standard deviation,  '
                                  'respectively. It is the most important distribution in statistical data analysis.'
                                  if language_type == 'en' else
                                  'Eine Normalverteilung (oder Gaußverteilung; benannt nach Carl Friedrich Gauß) ist '
                                  'eine kontinuierliche Wahrscheinlichkeitsverteilung für eine reellwertige '
                                  'Zufallsvariable. Die Normalverteilung hat zwei Parameter, nämlich den Mittelwert '
                                  'und die Standardabweichung. Es ist die wichtigste Verteilung in der statistischen '
                                  'Datenanalyse.' if language_type == 'de' else
                                  'Une distribution normale (ou gaussienne ; du nom de Carl Friedrich Gauss) est une '
                                  'distribution de probabilité continue pour une variable aléatoire à valeur réelle. '
                                  'La distribution normale a deux paramètres, qui sont respectivement la moyenne '
                                  'et l\'écart type. C\'est la distribution la plus importante dans l\'analyse des '
                                  'données statistiques' if language_type == 'fr' else
                                  '正态（或高斯分布；以Carl Friedrich Gauss命名）分布是实值随机变量的连续概率分布。正态分布有两个参数，'
                                  '分别是均值和标准差。它是统计数据分析中最重要的分布。'  if language_type == 'cn' else None)
        elif current_type == 2:
            message_label.text = ('The Poisson (Siméon Denis Poisson) distribution is a discrete probability '
                                  'distribution that describes the probability of a given number of events occurring '
                                  'in a fixed interval of time. The Poisson distribution has only one parameter, '
                                  'which is the rate. The Poisson distribution is often used to model rare events. '
                                  'The parameter of a Poisson distribution represents both its expectation (mean) and '
                                  'variance.'
                                  if language_type == 'en' else
                                  'Die Poisson-Verteilung (Siméon Denis Poisson) ist eine diskrete '
                                  'Wahrscheinlichkeitsverteilung, die die Wahrscheinlichkeit beschreibt, mit der eine '
                                  'bestimmte Anzahl von Ereignissen in einem festen Zeitintervall auftritt. Die '
                                  'Poisson-Verteilung hat nur einen Parameter, nämlich die Rate. Die Poisson-Verteilung '
                                  'wird häufig zur Modellierung seltener Ereignisse verwendet. Der Parameter einer '
                                  'Poisson-Verteilung repräsentiert sowohl ihren Erwartungswert (Mittelwert) als auch '
                                  'ihre Varianz.' if language_type == 'de' else
                                  'La distribution de Poisson (Siméon Denis Poisson) est une distribution de probabilité '
                                  'discrète qui décrit la probabilité qu\'un nombre donné d\'événements se produisent '
                                  'dans un intervalle de temps fixe. La distribution de Poisson n\'a qu\'un seul paramètre, '
                                  'qui est le taux. La distribution de Poisson est souvent utilisée pour modéliser des '
                                  'événements rares. Le paramètre d\'une distribution de Poisson représente à la fois son '
                                  'espérance (moyenne) et sa variance.' if language_type == 'fr' else
                                  '泊松(Siméon Denis Poisson)分布是一种离散概率分布，它描述了给定数量的事件在固定时间间隔内发生的概率。'
                                  '泊松分布只有一个参数，即比率。泊松分布通常用于对罕见事件建模。泊松分布的参数表示其期望(均值)'
                                  '和方差' if language_type == 'cn' else None)
        elif current_type == 3:
            message_label.text = ('The binomial distribution is the discrete probability distribution of the number '
                                  'of successes in a sequence of n independent experiments. For a single experiment, '
                                  'i.e., n = 1, the binomial distribution is a Bernoulli (Jacob Bernoulli) '
                                  'distribution. The binomial distribution has two parameters, including n (number of '
                                  ' experiments) and p (success rate).'
                                  if language_type == 'en' else
                                  'Die Binomialverteilung ist die diskrete Wahrscheinlichkeitsverteilung der Anzahl der '
                                  'Erfolge in einer Folge von n unabhängigen Experimenten. Für ein einzelnes Experiment, '
                                  'd. h. n = 1, ist die Binomialverteilung eine Bernoulli-Verteilung (Jacob Bernoulli). '
                                  'Die Binomialverteilung hat zwei Parameter, darunter n (Anzahl der Experimente) und p '
                                  '(Erfolgsrate).' if language_type == 'de' else
                                  'La distribution binomiale est la distribution de probabilité discrète du nombre de '
                                  'succès dans une séquence de n expériences indépendantes. Pour une seule expérience, '
                                  'c\'est-à-dire n = 1, la distribution binomiale est une distribution de Bernoulli '
                                  '(Jacob Bernoulli). La distribution binomiale a deux paramètres, dont n (nombre '
                                  'd\'expériences) et p (taux de réussite).' if language_type == 'fr' else
                                  '二项分布是n个独立实验序列中成功次数的离散概率分布。对于单个实验，即n=1，二项分布是伯努利('
                                  'Jacob Bernoulli)分布。二项分布有两个参数，包括n实验次数)和p成功率）。'
                                  if language_type == 'cn' else None)
        elif current_type == 4:
            message_label.text = ('The beta distribution is a family of continuous probability distributions defined '
                                  'on the interval of 0 and 1. The beta distribution has two parameters, denoted by '
                                  'alpha (α) and beta (β), respectively, which control the shape of the distribution. '
                                  'It is widely used as a prior distribution in Bayesian data analysis.'
                                  if language_type == 'en' else
                                  'Die Beta-Verteilung ist eine Familie kontinuierlicher Wahrscheinlichkeitsverteilungen,'
                                  ' die im Intervall von 0 und 1 definiert sind. Die Beta-Verteilung verfügt über zwei '
                                  'Parameter, die mit Alpha (α) bzw. Beta (β) bezeichnet werden und die Form der '
                                  'Verteilung steuern. Sie wird häufig als Prior-Verteilung in der Bayesschen '
                                  'Datenanalyse verwendet.' if language_type == 'de' else
                                  'La distribution bêta est une famille de distributions de probabilité continues définies '
                                  'sur l\'intervalle de 0 et 1. La distribution bêta a deux paramètres, notés '
                                  'respectivement alpha (α) et bêta (β), qui contrôlent la forme de la distribution. '
                                  'Il est largement utilisé comme distribution a priori dans l\'analyse de données '
                                  'bayésienne.' if language_type == 'fr' else
                                  '贝塔分布是定义在0和1区间上的一族连续概率分布。贝塔分布有两个参数，分别用形状参数α和β'
                                  '表示，它们控制分布的形状。它被广泛用作贝叶斯数据分析中的先验分布。'
                                  if language_type == 'cn' else None)
        elif current_type == 5:
            message_label.text = ('The negative binomial distribution is a discrete probability distribution that '
                                  'models the number of failures in a sequence of independent and identically '
                                  'distributed Bernoulli trials before a specified number of successes occurs. The '
                                  'negative binomial distribution has two parameters, which are the number of '
                                  'successes required (r) and the probability of success in a single trial (p). The '
                                  'negative binomial distribution offers more flexibility than the Poisson '
                                  'distribution for modeling count or event data because it does not require the mean '
                                  'to be equal to the variance.'
                                  if language_type == 'en' else
                                  'Die negative Binomialverteilung ist eine diskrete Wahrscheinlichkeitsverteilung, '
                                  'die die Anzahl der Fehlschläge in einer Folge unabhängiger und identisch verteilter '
                                  'Bernoulli-Versuche modelliert, bevor eine bestimmte Anzahl von Erfolgen eintritt. '
                                  'Die negative Binomialverteilung hat zwei Parameter: die Anzahl der erforderlichen '
                                  'Erfolge (r) und die Erfolgswahrscheinlichkeit in einem einzelnen Versuch (p). '
                                  'Die negative Binomialverteilung bietet mehr Flexibilität als die Poisson-Verteilung '
                                  'für die Modellierung von Zähl- oder Ereignisdaten, da sie nicht erfordert, dass der '
                                  'Mittelwert gleich der Varianz ist.' if language_type == 'de' else
                                  'La distribution binomiale négative est une distribution de probabilité discrète qui '
                                  'modélise le nombre d\'échecs dans une séquence d\'essais de Bernoulli indépendants et '
                                  'distribués de manière identique avant qu\'un nombre spécifié de succès ne se produise. '
                                  'La distribution binomiale négative a deux paramètres, qui sont le nombre de succès '
                                  'requis (r) et la probabilité de succès dans un seul essai (p). La distribution '
                                  'binomiale négative offre plus de flexibilité que la distribution de Poisson pour '
                                  'modéliser les données de comptage ou d\'événement, car elle ne nécessite pas que la '
                                  'moyenne soit égale à la variance.' if language_type == 'fr' else
                                  '负二项分布是一种离散概率分布，它模拟在发生指定数量的成功之前一系列独立且同分布的伯努利试验中的失败次数。'
                                  '负二项分布有两个参数，分别是所需的成功次数(r)和单次试验成功的概率(p)。对于计数或事件数据建模，负二'
                                  '项分布比泊松分布提供了更大的灵活性，因为它不需要均值等于方差。' if language_type == 'cn' else None)
        elif current_type == 6:
            message_label.text = ('The continuous uniform distribution is a symmetric probability distribution that '
                                  'describes an experiment where there is an equally likely outcome within a certain '
                                  'lower and upper bounds of the interval. It is often used as a non-informative '
                                  'prior in Bayesian data analysis, as it does not impose any prior knowledge. '
                                  'However, it is still informative in the sense that its mean is the average of '
                                  'lower and upper bounds.'
                                  if language_type == 'en' else
                                  'Die kontinuierliche Gleichverteilung ist eine symmetrische '
                                  'Wahrscheinlichkeitsverteilung, die ein Experiment beschreibt, bei dem es innerhalb '
                                  'einer bestimmten Unter- und Obergrenze des Intervalls ein gleich wahrscheinliches '
                                  'Ergebnis gibt. In der Bayesschen Datenanalyse wird es oft als nicht informativer '
                                  'Prior verwendet, da es kein Vorwissen erfordert. Es ist jedoch immer noch informativ '
                                  'in dem Sinne, dass sein Mittelwert der Durchschnitt der unteren und oberen Grenzen '
                                  'ist.' if language_type == 'de' else
                                  'La distribution uniforme continue est une distribution de probabilité symétrique qui '
                                  'décrit une expérience où il y a un résultat également probable dans certaines limites '
                                  'inférieure et supérieure de l\'intervalle. Il est souvent utilisé comme a priori non '
                                  'informatif dans l\'analyse de données bayésienne, car il n\'impose aucune connaissance '
                                  'préalable. Cependant, il est toujours informatif dans le sens où sa moyenne est la '
                                  'moyenne des bornes inférieure et supérieure.' if language_type == 'fr' else
                                  '连续均匀分布是一种对称概率分布，它描述了一个实验，在该实验中，在区间的某个下限和上限内存在同样可能的结果。'
                                  '它通常用作贝叶斯数据分析中的非信息先验，因为它不强加任何先验知识。然而，它仍然具有丰富的信息，因为它的均'
                                  '值是下限和上限的平均值。' if language_type == 'cn' else None)
        elif current_type == 7:
            message_label.text = ('The Chi-squared distribution with k degrees of freedom is the distribution of a '
                                  'sum of the squares of k independent standard normal random variables. The '
                                  'chi-squared distribution is a special case of the gamma distribution and is one of '
                                  'the most widely used probability distributions in inferential statistics.'
                                  if language_type == 'en' else
                                  'Die Chi-Quadrat-Verteilung mit k Freiheitsgraden ist die Verteilung einer Summe der '
                                  'Quadrate von k unabhängigen Standardnormal-Zufallsvariablen. Die '
                                  'Chi-Quadrat-Verteilung ist ein Sonderfall der Gammaverteilung und eine der am '
                                  'häufigsten verwendeten Wahrscheinlichkeitsverteilungen in der Inferenzstatistik.'
                                  if language_type == 'de' else
                                  'La distribution du chi carré avec k degrés de liberté est la distribution d\'une somme '
                                  'des carrés de k variables aléatoires normales standard indépendantes. La distribution '
                                  'chi carré est un cas particulier de la distribution gamma et est l\'une des '
                                  'distributions de probabilité les plus largement utilisées dans les statistiques inférentielles.'
                                  if language_type == 'fr' else
                                  '自由度为k的卡方分布是k个独立标准正态随机变量的平方和的分布。卡方分布是伽玛分布的特例，是推论统计中'
                                  '使用最广泛的概率分布之一。'
                                  if language_type == 'cn' else None)
        elif current_type == 8:
            message_label.text = ('The exponential distribution is the probability distribution of the time between '
                                  'events in a Poisson point process. It is a special case of the gamma distribution, '
                                  'characterized by the rate parameter. The exponential distribution is often '
                                  'described as memory-less because the probability of an event occurring within a '
                                  'certain time interval does not depend on the elapsed time.'
                                  if language_type == 'en' else
                                  'Die Exponentialverteilung ist die Wahrscheinlichkeitsverteilung der Zeit zwischen '
                                  'Ereignissen in einem Poisson-Punkt-Prozess. Es handelt sich um einen Sonderfall der '
                                  'Gammaverteilung, der durch den Geschwindigkeitsparameter charakterisiert wird. Die '
                                  'Exponentialverteilung wird oft als gedächtnislos beschrieben, da die '
                                  'Wahrscheinlichkeit, dass ein Ereignis innerhalb eines bestimmten Zeitintervalls '
                                  'eintritt, nicht von der verstrichenen Zeit abhängt.'
                                  if language_type == 'de'else
                                  'La distribution exponentielle est la distribution de probabilité du temps entre les '
                                  'événements dans un processus ponctuel de Poisson. C\'est un cas particulier de la '
                                  'distribution gamma, caractérisé par le paramètre taux. La distribution exponentielle '
                                  'est souvent décrite comme sans mémoire car la probabilité qu\'un événement se '
                                  'produise dans un certain intervalle de temps ne dépend pas du temps écoulé.'
                                  if language_type == 'fr'else
                                  '指数分布是泊松点过程中事件之间时间的概率分布。它是伽玛分布的一个特例，以速率参数为特征。指数分布通常'
                                  '被描述为无记忆的，因为在特定时间间隔内发生事件的概率不依赖于已经经过的时间。'
                                  if language_type == 'cn' else None)
        elif current_type == 9:
            message_label.text = ('Student (named after William Sealy Gosset) t-distribution is a continuous '
                                  'probability distribution that generalizes the standard normal distribution. For a '
                                  'degree of freedom equal to 1, the Student t distribution becomes the standard '
                                  'Cauchy distribution, whereas for degrees of freedom approaching infinity, '
                                  'the t-distribution converges to the standard normal distribution. The two-sample '
                                  't-test is commonly used and is based on the t-distribution. It allows for unequal '
                                  'variances between the two groups being compared.'
                                  if language_type == 'en' else
                                  'Die Student-T-Verteilung (benannt nach William Sealy Gosset) ist eine kontinuierliche '
                                  'Wahrscheinlichkeitsverteilung, die die Standardnormalverteilung verallgemeinert. '
                                  'Für einen Freiheitsgrad gleich 1 wird die Student-t-Verteilung zur '
                                  'Standard-Cauchy-Verteilung, während für Freiheitsgrade gegen Unendlich die '
                                  't-Verteilung zur Standardnormalverteilung konvergiert. Der t-Test mit zwei '
                                  'Stichproben wird häufig verwendet und basiert auf der t-Verteilung. Es ermöglicht '
                                  'ungleiche Varianzen zwischen den beiden verglichenen Gruppen.'
                                  if language_type == 'de' else
                                  'La distribution t de Student (du nom de William Sealy Gosset) est une distribution de '
                                  'probabilité continue qui généralise la distribution normale standard. Pour un degré de '
                                  'liberté égal à 1, la distribution t de Student devient la distribution de Cauchy '
                                  'standard, tandis que pour les degrés de liberté s\'approchant de l\'infini, la '
                                  'distribution t converge vers la distribution normale standard. Le test t à deux '
                                  'échantillons est couramment utilisé et est basé sur la distribution t. Il permet '
                                  'des variances inégales entre les deux groupes comparés.'
                                  if language_type == 'fr' else
                                  '学生（以 William Sealy Gosset 的名字命名）t分布是一种对标准正态分布延伸的连续概率分布。对于等于'
                                  '1的自由度，学生t分布成为标准柯西分布，而对于接近无穷大的自由度，t分布收敛于标准正态分布。我们经常的使用'
                                  '双样本t检验就是基于t分布。t检验允许被比较的两组之间存在不相等的方差。'
                                  if language_type == 'cn' else None)

        message_label.bind(
            width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width,
                                                                               None)))

        # Create the popup and set its content
        popup = Popup(title='', separator_height=0, content=message_label, size_hint=(None, None), size=(popup_x_size,
                                                                                                         popup_y_size))
        # Open the popup
        popup.open()

    def show_second_page(self, instance):
        self.manager.current = 'second_page'


    def show_home_screen(self, instance):
        self.manager.current = 'home_page'


    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'first_page':
            # do what you want, return True for stopping the propagation
            self.show_home_screen(1)
            self.clear_widgets()  # Clear all widgets in the box layout
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
                               if language_type == 'de' else
                               f'{first_input_name} doit être un nombre.'
                               if language_type == 'fr' else
                               f'{first_input_name} 必须是数字。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
        elif first_input_needs_int:
            try:
                first_value = int(self.first_input_2.text)
            except ValueError:
                self.errors = (f'{first_input_name} must be an integer.'
                               if language_type == 'en' else
                               f'{first_input_name} muss eine ganze Zahl sein.'
                               if language_type == 'de' else
                               f'{first_input_name} Doit être un entier.'
                               if language_type == 'fr' else
                               f'{first_input_name} 必须是整数。'
                               if language_type == 'cn' else None)
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
                                   if language_type == 'de' else
                                   f'{second_input_name} doit être un nombre.'
                                   if language_type == 'fr' else
                                   f'{second_input_name} 必须是数字。'
                                   if language_type == 'cn' else None)
                    self.show_error_popup(1)
                    return
            elif second_input_needs_int:
                try:
                    second_value = int(self.second_input_2.text)
                except ValueError:
                    self.errors = (f'{second_input_name} must be an integer.'
                                   if language_type == 'en' else
                                   f'{second_input_name} muss eine ganze Zahl sein.'
                                   if language_type == 'de' else
                                   f'{second_input_name} Doit être un entier.'
                                   if language_type == 'fr' else
                                   f'{second_input_name} 必须是整数。'
                                   if language_type == 'cn' else None)
                    self.show_error_popup(1)
                    return

        if self.N_input.text != ('Default is 10000. Click to change.' if language_type == 'en' else
                                'Der Standardwert ist 10000.' if language_type == 'de' else
                                'La valeur par défaut est 10000.' if language_type == 'fr' else
                                '默认值为10000，单击以更改。' if language_type == 'cn' else None):
            try:
                size = int(self.N_input.text) if self.N_input.text else None
            except ValueError:
                self.errors = ('Number of simulation (N) must be an integer.'
                               if language_type == 'en' else
                               'Die Anzahl der Simulationen (N) muss eine ganze Zahl sein.'
                               if language_type == 'de' else
                               'Le nombre de simulations (N) doit être un nombre entier.'
                               if language_type == 'fr' else
                               '模拟次数（N）必须是整数。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
        else:
            size = 10000

        if current_type == 1:
            if second_value <= 0:
                self.errors = ('Standard deviation (σ) must be greater than 0.'
                               if language_type == 'en' else
                               'Die Standardabweichung (σ) muss größer als 0 sein.'
                               if language_type == 'de' else
                               'L\'écart type (σ) doit être supérieur à 0.'
                               if language_type == 'fr' else
                               '标准差 (σ) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.normal(first_value, second_value, size=size)
        elif current_type == 2:
            if first_value <= 0:
                self.errors = ('Rate (λ) must be positive.'
                               if language_type == 'en' else
                               'Rate (λ) muss positiv sein.'
                               if language_type == 'de' else
                               'Le taux (λ) doit être positif.'
                               if language_type == 'fr' else
                               '比率 (λ) 必须为正。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.poisson(first_value, size=size)
        elif current_type == 3:
            if not 0 <= second_value <= 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                               if language_type == 'en' else
                               'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                               if language_type == 'de' else
                               'Le taux de réussite (p) doit être compris entre 0 et 1.'
                               if language_type == 'fr' else
                               '成功率 (p) 必须介于 0 和 1 之间。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                               if language_type == 'en' else
                               'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                               if language_type == 'de' else
                               'Le nombre d\'expériences (n) doit être un nombre entier supérieur à 0.'
                               if language_type == 'fr' else
                               '试验次数 (n) 必须是大于 0 的整数。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.binomial(first_value, second_value, size=size)
        elif current_type == 4:
            if not first_value > 0:
                self.errors = ('Shape (α) must be greater than 0.'
                               if language_type == 'en' else
                               'Form (α) muss größer als 0 sein.'
                               if language_type == 'de' else
                               'La forme (α) doit être supérieure à 0.'
                               if language_type == 'fr' else
                               '形状 (α) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            if not second_value > 0:
                self.errors = ('Shape (β) must be greater than 0.'
                               if language_type == 'en' else
                               'Form (β) muss größer als 0 sein.'
                               if language_type == 'de' else
                               'La forme (β) doit être supérieure à 0.'
                               if language_type == 'fr' else
                               '形状 (β) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.beta(first_value, second_value, size=size)
        elif current_type == 5:
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                               if language_type == 'en' else
                               'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                               if language_type == 'de' else
                               'Le nombre d\'expériences (n) doit être un nombre entier supérieur à 0.'
                               if language_type == 'fr' else
                               '试验次数 (n) 必须是大于 0 的整数。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            if not 0 < second_value < 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                               if language_type == 'en' else
                               'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                               if language_type == 'de' else
                               'Le taux de réussite (p) doit être compris entre 0 et 1.'
                               if language_type == 'fr' else
                               '成功率 (p) 必须介于 0 和 1 之间。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.negative_binomial(first_value, second_value, size=size)
        elif current_type == 6:
            if first_value==second_value:
                self.errors = ('The lower bound (a) cannot be equal to the upper bound (b).'
                               if language_type == 'en' else
                               'Die Untergrenze (a) darf nicht gleich der Obergrenze (b) sein.'
                               if language_type == 'de' else
                               'La borne inférieure (a) ne peut pas être égale à la borne supérieure (b).'
                               if language_type == 'fr' else
                               '下限 （a） 不能等于上限 （b）。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.uniform(first_value, second_value, size=size)
        elif current_type == 7:
            if first_value < 0:
                self.errors = ('Degree of freedom (κ) must be positive.'
                               if language_type == 'en' else
                               'Der Freiheitsgrad (κ) muss positiv sein.'
                               if language_type == 'de' else
                               'Le degré de liberté (κ) doit être positif.'
                               if language_type == 'fr' else
                               '自由度 (κ) 必须为正。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.chisquare(first_value, size=size)
        elif current_type == 8:
            if first_value < 0:
                self.errors = ('Scale parameter (λ) must be positive.'
                               if language_type == 'en' else
                               'Skalenparameter (λ) muss positiv sein.'
                               if language_type == 'de' else
                               'Le paramètre d\'échelle (λ) doit être positif.'
                               if language_type == 'fr' else
                               '速率参数 (λ) 必须为正。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            data = np.random.exponential(first_value, size=size)
        elif current_type == 9:
            if first_value < 0:
                self.errors = ('Degree of freedom (v) must be positive.'
                               if language_type == 'en' else
                               'Der Freiheitsgrad (v) muss positiv sein.'
                               if language_type == 'de' else
                               'Le degré de liberté (v) doit être positif.'
                               if language_type == 'fr' else
                               '自由度 (v) 必须为正。'
                               if language_type == 'cn' else None)
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
        fig, axs = plt.subplots(2, 1, figsize=(8, 26), gridspec_kw={"width_ratios": [subplot_width],
                                                                    "height_ratios": [subplot_height, subplot_height]})

        # fig, axs = plt.subplots(2, 1, figsize=(8, 15))
        mpl.rcParams['font.size'] = 26
        label_font_size = 26

        # Plot the histogram
        axs[0].hist(data, bins='auto', alpha=0.7, rwidth=0.85)
        axs[0].set_title((f'Histogram of a {current_type_nameG}'
                          if language_type == 'en' else
                          f'Histogramm von a {current_type_nameG}'
                          if language_type == 'de' else
                          f'Histogramme d\'un {current_type_nameG}'
                          if language_type == 'fr' else
                          f' {current_type_nameG}的直方图'
                          if language_type == 'cn' else None),
                            fontproperties=self.get_font_properties(f'{language_type}'))

        axs[0].set_ylabel(('Frequency' if language_type == 'en' else
                           'Frequenz' if language_type == 'de' else
                           'Fréquence' if language_type == 'fr' else
                           '频率' if language_type == 'cn' else None), fontsize=label_font_size,
                            fontproperties=self.get_font_properties(f'{language_type}'))

        # Plot the line plot
        axs[1].plot(data)
        axs[1].set_ylabel(('Value' if language_type == 'en' else
                           'Wert' if language_type == 'de' else
                           'Valeur' if language_type == 'fr' else
                           '数值' if language_type == 'cn' else None),
                            fontproperties=self.get_font_properties(f'{language_type}'))

        mean_value = np.mean(data)  # Calculate the mean of the data

        # Add the dashed line at the mean
        axs[1].axhline(mean_value, color='r', linestyle='--',
                                label=('Mean' if language_type == 'en' else
                                'Bedeuten' if language_type == 'de' else
                                'Moyenne' if language_type == 'fr' else
                                'Mean' if language_type == 'cn' else None) )
        axs[1].legend(fontsize=label_font_size)
        axs[1].set_ylabel(('Value' if language_type == 'en' else
                           'Wert' if language_type == 'de' else
                           'Valeur' if language_type == 'fr' else
                           '数值' if language_type == 'cn' else None), fontsize=label_font_size,
                            fontproperties=self.get_font_properties(f'{language_type}'))

        # Create a FigureCanvasKivyAgg and add it to the box layout
        canvas = FigureCanvasKivyAgg(fig)
        self.box.add_widget(canvas)

        plt.close(fig)  # Close the figure to release resources

        self.errors = ''

    def get_font_properties(self, language_type):
        #cwd = os.getcwd()
        #font_path = os.path.join(cwd, 'csongl.ttf' if language_type == 'cn' else 'hnfsasr.ttf')
        #font_path = os.path.join('csongl.ttf' if language_type == 'cn' else 'hnfsasr.ttf')
        font_properties = fm.FontProperties(fname='csongl.ttf')
        return font_properties

    def go_to_start_screen(self, instance, touch):
        if touch.is_double_tap:
            self.clear_widgets()  # Clear all widgets in the box layout
            self.manager.current = 'language_page'


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
                                     f'{current_type_name} ZGWS' if language_type == 'de' else
                                     f'{current_type_name} TLC' if language_type == 'fr' else
                                     f'{current_type_name}' if language_type == 'cn' else None),
                               size_hint=(1, 0.1), font_name=('cn' if language_type == 'cn' else 'eng'), font_size=50, color=(0, 1, 0),
                               pos_hint={'center_x': 0.5, 'center_y': 1})

        # possible description label
        self.CLT_description = Button(text=('How to illustrate CLT' if language_type == 'en' else
                                            'So veranschaulichen Sie ZGWS' if language_type == 'de' else
                                            'Comment illustrer le TLC' if language_type == 'fr' else
                                            '如何展示中心极限定理' if language_type == 'cn' else None),font_name=('cn' if language_type == 'cn' else 'eng'),
                                      size_hint=(1, 0.1), pos_hint={'center_x': 0.5}, color=(1, 1, 1), font_size=50)
        self.CLT_description.background_color = (1, 0, 0, 1)
        self.CLT_description.bind(on_press=self.CLT_popup)
        self.box.add_widget(self.CLT_title)

        self.iterations_slider = Slider(min=2, max=30, value=10, value_track=True, value_track_color=[0.5, 0.7, 0.8, 1],
                                        height=50, size_hint=(0.95, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.iterations_text = Label(
            text=('Slide to input the number of i.i.d. distributions.' if language_type == 'en' else
                  'Zum Eingeben der Anzahl i.i.d. Verteilungen schieben.' if language_type == 'de' else
                  'Glissez pour entrer le nombre d\'i.i.d. distributions.' if language_type == 'fr' else
                  '滑动输入独立同分布的数量。' if language_type == 'cn' else None), height=100,
            size_hint=(0.9, None), font_size=39, halign='center', valign='bottom', font_name=('cn' if language_type == 'cn' else 'eng'),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.iterations_slider.bind(value=lambda instance, value:
        (setattr(self.iterations_text, 'text',
                 f'Number of sample i.i.d. distributions:  '
                 f'{round(self.iterations_slider.value)}') if language_type == 'en' else
         setattr(self.iterations_text, 'text',
                 f'Anzahl der Proben i.i.d. Verteilungen:  '
                 f'{round(self.iterations_slider.value)}') if language_type == 'de' else
         setattr(self.iterations_text, 'text',
                 f'Nombre d\'échantillons i.i.d. distributions:  '
                 f'{round(self.iterations_slider.value)}') if language_type == 'fr' else
         setattr(self.iterations_text, 'text',
                 f'独立同分布的样本数量是： '
                 f'{round(self.iterations_slider.value)}') if language_type == 'cn' else None))

        self.iterations_slider.bind(value=self.create_plot)

        self.box.add_widget(self.CLT_description)
        self.box.add_widget(self.iterations_text)
        self.box.add_widget(self.iterations_slider)

        # Add the label widget
        self.simulations_text = Label(text=('Number of Simulations' if language_type == 'en' else
                                            'Anzahl der Simulationen' if language_type == 'de' else
                                            'Nombre de simulations' if language_type == 'fr' else
                                            '模拟次数' if language_type == 'cn' else None),
                                      size_hint=(1, 0.1), font_name=('cn' if language_type == 'cn' else 'eng'),
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
                  'Der Standardwert ist 1000.' if language_type == 'de' else
                  'La valeur par défaut est 1000.' if language_type == 'fr' else
                  '默认值为 1000。按钮进行更改。' if language_type == 'cn' else None),
            halign='center',
            # available values
            values=('100', '1000', '5000', '10000', '100000'),
            # just for positioning in our example
            size_hint=(0.5, 0.1),
            height=50,
            font_size=50,font_name=('cn' if language_type == 'cn' else 'eng'),
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
                  ' \nEingabeverteilungsparameter' if language_type == 'de' else
                  ' \nParamètres de distribution d\'entrée' if language_type == 'fr' else
                  ' \n输入分布参数' if language_type == 'cn' else None),
            size_hint=(1, 0.05),
            font_size=43,font_name=('cn' if language_type == 'cn' else 'eng'),
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
                                       size_hint=(0.5, 1), font_size=50, color=(1, 0, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                       pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
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
                                       size_hint=(0.5, 1), font_size=50, color=(1, 0, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                       pos_hint={'center_x': 0.5, 'center_y': 1})

            self.first_input_2 = TextInput(hint_text=first_input_name, size_hint=(1, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                           font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                           foreground_color=(0, 0, 1))
            self.first_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_1.add_widget(self.first_input_1)
            self.sub_box_1.add_widget(self.first_input_2)
            self.sub_box.add_widget(self.sub_box_1)

            self.sub_box_2 = BoxLayout(orientation='vertical', spacing=10, size_hint=(.5, 1))
            self.second_input_1 = Label(text=f'{second_input_name}',
                                        size_hint=(0.5, 1), font_size=50, color=(1, 0, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                        pos_hint={'center_x': 0.5, 'center_y': 1})
            self.second_input_2 = TextInput(hint_text=second_input_name, size_hint=(1, 1),font_name=('cn' if language_type == 'cn' else 'eng'),
                                            font_size=50, halign="center", pos_hint={'center_x': 0.5, 'center_y': .8},
                                            foreground_color=(0, 0, 1))
            self.second_input_2.background_color = (0.7, 1, 0, 1)
            self.sub_box_2.add_widget(self.second_input_1)
            self.sub_box_2.add_widget(self.second_input_2)
            self.sub_box.add_widget(self.sub_box_2)

        self.box.add_widget(self.sub_box)

        empty_text = Label(text=' ', size_hint=(1, .1), size=(100, 200),font_name=('cn' if language_type == 'cn' else 'eng'),
                           pos_hint={'center_x': 0.5},
                           font_size=30, color=(0.2, 0.8, 0.2))
        empty_text.bind(
            height=lambda *x: empty_text.setter('text_size')(empty_text, (empty_text.height, None)))
        self.box.add_widget(empty_text)

        provide_text = Label(text=('Made possible by Banana Shaped Cow Studios' if language_type == 'en' else
                                   'Ermöglicht durch Banana Shaped Cow Studios' if language_type == 'de' else
                                   'Rendu possible par Banana Shaped Cow Studios' if language_type == 'fr' else
                                   'Banana Shaped Cow Studios 制作' if language_type == 'cn' else None),
                             size_hint=(1, None), size=(100, 100),font_name=('cn' if language_type == 'cn' else 'eng'),
                             pos_hint={'center_x': 0.5},
                             font_size=30, color=(0.8, 0.8, 0))

        provide_text.bind(
            height=lambda *x: provide_text.setter('text_size')(provide_text, (provide_text.height, None)))
        self.box.add_widget(provide_text)

        # self.box.add_widget(self.sub_box_1)
        self.add_widget(self.box)

    def CLT_popup(self, instance):
        popup_x_size = 400 * 2.2
        popup_y_size = 350 * 2.9
        # Create a label with the message
        message_label = Label(text='', size_hint=(1, None), pos_hint={'center_y': 0.6}, halign='center',
                                font_name=('cn' if language_type == 'cn' else 'eng'), font_size=50)

        message_label.text = ('First set the number (N) of independent identical distributed  (i.i.d.) samples to be '
                              'created by using the slider below. Then,  set the number (S) of simulated values for '
                              'each of the distributions. The program will calculate the average of the N '
                              'distributions for each of the S simulations and generate a histogram. For comparison '
                              'purpose, the histogram of one of the i.i.d. distributions will also be generated.'
                              if language_type == 'en' else
                              'Legen Sie zunächst die Anzahl (N) der unabhängigen, identisch verteilten (i.i.d.) '
                              'Stichproben fest, die erstellt werden sollen, indem Sie den Schieberegler unten '
                              'verwenden. Legen Sie dann die Anzahl (S) der simulierten Werte für jede der '
                              'Verteilungen fest. Das Programm berechnet den Durchschnitt der N Verteilungen für '
                              'jede der S Simulationen und erstellt ein Histogramm. Zu Vergleichszwecken das '
                              'Histogramm eines der i.i.d. Es werden auch Ausschüttungen generiert.'
                              if language_type == 'de' else
                              'Définissez d\'abord le nombre (N) d\'échantillons distribués identiques indépendants '
                              '(i.i.d.) à créer en utilisant le curseur ci-dessous. Ensuite, définissez le nombre (S) '
                              'de valeurs simulées pour chacune des distributions. Le programme calculera la moyenne '
                              'des N distributions pour chacune des S simulations et générera un histogramme. À des '
                              'fins de comparaison, l\'histogramme de l\'un des i.i.d. des distributions seront '
                              'également générées.'
                              if language_type == 'fr' else
                              '首先使用下面的滑块设置要创建的独立同分布样本的数量(N)。然后，设置每个分布的模拟值的数量(S)。'
                              '该程序将计算每次模拟的N个分布的平均值，并用S次的模拟生成直方图。作为比较，下图还展示了用一个独立同分布'
                              '的模拟值生成的直方图。'
                              if language_type == 'cn' else None)

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
                               if language_type == 'de' else
                               f'{first_input_name} doit être un nombre.'
                               if language_type == 'fr' else
                               f'{first_input_name} 必须是一个数字。'
                               if language_type == 'cn' else None)

                self.show_error_popup(1)
                return
        elif first_input_needs_int:
            try:
                first_value = int(self.first_input_2.text)
            except ValueError:
                self.errors = (f'{first_input_name} must be an integer.'
                               if language_type == 'en' else
                               f'{first_input_name} muss eine ganze Zahl sein.'
                               if language_type == 'de' else
                               f'{first_input_name} Doit être un entier.'
                               if language_type == 'fr' else
                               f'{first_input_name} 必须是整数。'
                               if language_type == 'cn' else None)
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
                                   if language_type == 'de' else
                                   f'{second_input_name} doit être un nombre.'
                                   if language_type == 'fr' else
                                   f'{second_input_name} 必须是一个数字。'
                                   if language_type == 'cn' else None)
                    self.show_error_popup(1)
                    return
            elif second_input_needs_int:
                try:
                    second_value = int(self.second_input_2.text)
                except ValueError:
                    self.errors = (f'{second_input_name} must be an integer.'
                                   if language_type == 'en' else
                                   f'{second_input_name} muss eine ganze Zahl sein.'
                                   if language_type == 'de' else
                                   f'{second_input_name} Doit être un entier.'
                                   if language_type == 'fr' else
                                   f'{second_input_name} 必须是整数。'
                                   if language_type == 'cn' else None)
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
                               if language_type == 'de' else
                               'L\'écart type (σ) doit être supérieur à 0.'
                               if language_type == 'fr' else
                               '标准差 (σ) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.normal(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)

        elif current_type == 2:
            if first_value <= 0:
                self.errors = ('Rate (λ) must be greater than 0.'
                               if language_type == 'en' else
                               'Rate (λ) muss größer als 0 sein.'
                               if language_type == 'de' else
                               'Le taux (λ) doit être supérieur à 0'
                               if language_type == 'fr' else
                               '比率 (λ) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.poisson(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)

        elif current_type == 3:
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                               if language_type == 'en' else
                               'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                               if language_type == 'de' else
                               'Le nombre d\'expériences (n) doit être un nombre entier supérieur à 0.'
                               if language_type == 'fr' else
                               '试验次数 (n) 必须是大于 0 的整数。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            if not 0 <= second_value <= 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                               if language_type == 'en' else
                               'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                               if language_type == 'de' else
                               'Le taux de réussite (p) doit être compris entre 0 et 1.'
                               if language_type == 'fr' else
                               '成功率 (p) 必须介于 0 和 1 之间。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.binomial(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)
        elif current_type == 4:
            if not first_value > 0:
                self.errors = ('Shape (α) must be greater than 0.'
                               if language_type == 'en' else
                               'Form (α) muss größer als 0 sein.'
                               if language_type == 'de' else
                               'La forme (α) doit être supérieure à 0.'
                               if language_type == 'fr' else
                               '形状参数 (α) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            if not second_value > 0:
                self.errors = ('Shape (β) must be greater than 0.'
                               if language_type == 'en' else
                               'Form (β) muss größer als 0 sein.'
                               if language_type == 'de' else
                               'La forme (β) doit être supérieure à 0.'
                               if language_type == 'fr' else
                               '形状参数 (β) 必须大于 0。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.beta(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)
        elif current_type == 5:
            if not 0 < second_value < 1:
                self.errors = ('Success Rate (p) must be between 0 and 1.'
                               if language_type == 'en' else
                               'Die Erfolgsrate (p) muss zwischen 0 und 1 liegen.'
                               if language_type == 'de' else
                               'Le taux de réussite (p) doit être compris entre 0 et 1.'
                               if language_type == 'fr' else
                               '成功率 (p) 必须介于 0 和 1 之间。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Experiment Count (n) must be an integer greater than 0.'
                               if language_type == 'en' else
                               'Experiment Count (n) muss eine ganze Zahl größer als 0 sein.'
                               if language_type == 'de' else
                               'Le nombre d\'expériences (n) doit être un nombre entier supérieur à 0.'
                               if language_type == 'fr' else
                               '试验次数 (n) 必须是大于 0 的整数。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.negative_binomial(first_value, second_value,
                                                 size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)
        elif current_type == 6:
            if first_value == second_value:
                self.errors = ('The lower bound (a) cannot be equal to the upper bound (b).'
                               if language_type == 'en' else
                               'Die Untergrenze (a) darf nicht gleich der Obergrenze (b) sein.'
                               if language_type == 'de' else
                               'La borne inférieure (a) ne peut pas être égale à la borne supérieure (b).'
                               if language_type == 'fr' else
                               '下限 （a） 不能等于上限 （b）。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.uniform(first_value, second_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)
        elif current_type == 7:
            if not isinstance(first_value, int) or first_value <= 0:
                self.errors = ('Degree of freedom (κ) must be an integer greater than 0.'
                                if language_type == 'en' else
                                   'Der Freiheitsgrad (κ) muss eine ganze Zahl größer als 0 sein.'
                                if language_type == 'de' else
                                   'Le degré de liberté (κ) doit être un nombre entier supérieur à 0.'
                                if language_type == 'fr' else
                                   '自由度 (κ) 必须是大于 0 的整数。'
                                if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.chisquare(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)
        elif current_type == 8:
            if first_value < 0:
                self.errors = ('Scale parameter (λ) must be positive.'
                               if language_type == 'en' else
                               'Skalenparameter (λ) muss positiv sein.'
                               if language_type == 'de' else
                               'Le paramètre d\'échelle (λ) doit être positif.'
                               if language_type == 'fr' else
                               '速率参数 (λ) 必须为正。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.exponential(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)
        elif current_type == 9:
            if first_value < 0:
                self.errors = ('Degree of freedom (v) must be positive.'
                               if language_type == 'en' else
                               'Der Freiheitsgrad (v) muss positiv sein.'
                               if language_type == 'de' else
                               'Le degré de liberté (v) doit être positif.'
                               if language_type == 'fr' else
                               '自由度 (v) 必须为正。'
                               if language_type == 'cn' else None)
                self.show_error_popup(1)
                return
            vector = np.random.standard_t(first_value, size=size * round(self.iterations_slider.value))
            matrix = np.array(vector).reshape(size, round(self.iterations_slider.value))
            data1 = matrix[:, 1]
            averaged_data = np.sum(matrix, axis=1) / round(self.iterations_slider.value)

        plt.cla()
        self.fig, self.axs = plt.subplots(2, 1, figsize=(8, 22))
        matplotlib.pyplot.close('all')

        # Clear the existing plot
        for child in self.box.children[:]:
            if isinstance(child, FigureCanvasKivyAgg):
                self.box.remove_widget(child)

        mpl.rcParams['font.size'] = 26
        label_font_size = 26

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
                               f' i.i.d. {current_type_nameG}s'
                               if language_type == 'en' else
                               f'Histogramm des Durchschnitts von  {round(self.iterations_slider.value)}'
                               f' i.i.d. {current_type_nameG}en'
                               if language_type == 'de' else
                               f'Histogramme de la moyenne de  {round(self.iterations_slider.value)}'
                               f' i.i.d. {current_type_nameG}s'
                               if language_type == 'fr' else
                               f'{round(self.iterations_slider.value)}  个独立同'
                               f'{current_type_nameG}平均值的直方图'
                               if language_type == 'cn' else None), fontsize=20,
                                fontproperties=self.get_font_properties(f'{language_type}'))
        self.axs[1].hist(data1, bins=num_bins, alpha=0.7, rwidth=1, range=(min_value, max_value))
        self.axs[1].set_title((f'Histogram of one {current_type_nameG}'
                               if language_type == 'en' else
                               f'Histogramm von einem {current_type_nameG}'
                               if language_type == 'de' else
                               f'Histogramme d\'un {current_type_nameG}'
                               if language_type == 'fr' else
                               f'一个{current_type_nameG}的直方图'
                               if language_type == 'cn' else None), fontsize=18,
                                fontproperties=self.get_font_properties(f'{language_type}'))

        # Set y-axis labels
        label_font_size = 26
        self.axs[0].set_ylabel(('Frequency' if language_type == 'en' else
                                f'Frequenz' if language_type == 'de' else
                                f'Fréquence' if language_type == 'fr' else
                                f'频率' if language_type == 'cn' else None), fontsize=label_font_size,
                                fontproperties=self.get_font_properties(f'{language_type}'))
        self.axs[1].set_ylabel(('Frequency' if language_type == 'en' else
                                f'Frequenz' if language_type == 'de' else
                                f'Fréquence' if language_type == 'fr' else
                                f'频率' if language_type == 'cn' else None), fontsize=label_font_size,
                                fontproperties=self.get_font_properties(f'{language_type}'))

        # Create a FigureCanvasKivyAgg and add it to the box layout
        canvas = FigureCanvasKivyAgg(self.fig)
        self.box.add_widget(canvas)

        plt.close(self.fig)  # Close the figure to release resources
        matplotlib.pyplot.close(self.fig)

        self.errors = ''

    def get_font_properties(self, language_type):
        #cwd = os.getcwd()
        #font_path = os.path.join(cwd, 'csongl.ttf' if language_type == 'cn' else 'hnfsasr.ttf')
        #font_path = os.path.join('csongl.ttf' if language_type == 'cn' else 'hnfsasr.ttf')
        font_properties = fm.FontProperties(fname='csongl.ttf')
        return font_properties
    def show_previous_screen(self, instance):
        self.manager.current = 'first_page'

    def go_to_start_screen(self, instance, touch):
        if touch.is_double_tap:
            self.clear_widgets()  # Clear all widgets in the box layout
            self.manager.current = 'language_page'

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'second_page':
            # do what you want, return True for stopping the propagation
            self.show_previous_screen(1)
            self.clear_widgets()  # Clear all widgets in the box layout
            return True

    def show_error_popup(self, instance):
        popup_x_size = 350 * 2.2
        popup_y_size = 230 * 2.2

        message_label = Label(text=self.errors, size_hint=(1, None), pos_hint={'center_y': 0.6},
                              font_name=('cn' if language_type == 'cn' else 'eng'),halign='center',
                              font_size=50, color=(1, 0, 0))

        message_label.bind(
            width=lambda *x: message_label.setter('text_size')(message_label, (message_label.width,
                                                                               None)))

        for popup1 in self.popups:
            popup1.dismiss()

        # Create the popup and set its content
        popup = Popup(title=('Error' if language_type == 'en' else
                             f'Fehler' if language_type == 'de' else
                             f'Erreur' if language_type == 'fr' else
                             f'错误' if language_type == 'cn' else None), content=message_label,
                      size_hint=(None, None), size=(popup_x_size, popup_y_size))
        self.popups.append(popup)
        # Open the popup
        popup.open()

    def on_leave(self):
        # Clear previous content
        self.clear_widgets()


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


