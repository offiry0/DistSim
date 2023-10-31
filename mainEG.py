from kivy.app import App

from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, shader, Rectangle

import numpy as np


class HomePage(Screen):
    def on_enter(self):
        with self.canvas.before:
            Color(119/256, 187/256, 63/256, 1)  # Set the background color (in this example, red)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        kivy_defaulttheme_color = np.array([88, 88, 88, 256]) / 256
        desired_button_color = np.array([247, 247, 246, 256]) / 256
        tintshade_color = desired_button_color / kivy_defaulttheme_color

        self.box_a1 = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.box_b1 = BoxLayout(orientation='vertical', size_hint=(1, 0.75))
        self.box_b2 = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.25))

        b1_image_1 = Image(source='plot2logo1024circle.png', fit_mode='contain', size_hint=(1, 0.95))
        b1_text_1 = Label(text='By BSC Studios', font_size=16, color=(0.1, 0.1, 0.1), size_hint=(0.4, 0.05),
                          halign='center', valign='center', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        b2_button_1 = Button(text='Scan Receipt', font_size=40, color=(0.1, 0.1, 0.1), size_hint=(0.5, 1),
                             background_color=tintshade_color)
        b2_button_2 = Button(text='View List', font_size=40, color=(0.1, 0.1, 0.1), size_hint=(0.5, 1),
                             background_color=tintshade_color)

        b2_button_1.bind(on_press=self.go_to_scan_page)
        b2_button_2.bind(on_press=self.go_to_list_page)

        self.box_b1.add_widget(b1_image_1)
        self.box_b1.add_widget(b1_text_1)
        self.box_b2.add_widget(b2_button_1)
        self.box_b2.add_widget(b2_button_2)

        self.box_a1.add_widget(self.box_b1)
        self.box_a1.add_widget(self.box_b2)

        self.add_widget(self.box_a1)

    def go_to_scan_page(self, instance):
        self.manager.current = 'scan_page'

    def go_to_list_page(self, instance):
        self.manager.current = 'list_page'

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_leave(self, *args):
        self.clear_widgets()


class ScanPage(Screen):
    def on_enter(self, *args):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'scan_page':
            self.go_to_home_screen(1)
            return True

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_page'


class ListPage(Screen):
    def on_enter(self, *args):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27 and self.manager.current == 'list_page':
            self.go_to_home_screen(1)
            return True

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_page'


class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        home_page = HomePage(name='home_page')
        self.screen_manager.add_widget(home_page)

        scan_page = ScanPage(name='scan_page')
        self.screen_manager.add_widget(scan_page)

        list_page = ListPage(name='list_page')
        self.screen_manager.add_widget(list_page)

        # More screens here

        return self.screen_manager


if __name__ == '__main__':
    MainApp().run()
