from functools import partial
from kivy.app import App
from kivy.config import Config
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
import math

List = []
type_id = []


class SpinnerOptions(SpinnerOption):

    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)

        self.font_size = Window.size[0] * 0.05


class MainScrean(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScrean, self).__init__(**kwargs)
        mat = {'СЧ': 7.2, 'Сталь': 7.8, 'БрАЖ': 7.5, 'БрОФ': 8.9, 'Медь': 8.9, 'Алюминий': 2.7, 'Грфит': 1.7,
               'Песок кварцовый': 1.7}

        height, wight = Window.size[1], Window.size[0]
        self.size = (wight, height)

        self.orientation = "vertical"
        self.size_hint = (None, None)

        height, wight = Window.size[1], Window.size[0]

        header_box = BoxLayout(size=(wight, height * 0.11), size_hint=(None, None))

        with header_box.canvas.before:
            Color(1, 1, 1, .97)
            Rectangle(pos=(0, height * 0.9), size=(wight, height * 0.10))

        logo_box = AnchorLayout(anchor_x="left", anchor_y="top")
        logo = Image(source='logo.jpg', size=(height * 0.1, height * 0.1), size_hint=(None, None))
        logo_box.add_widget(logo)

        logo_name_box = AnchorLayout(anchor_x="center", anchor_y="top")
        logo_name = Image(source='logo_name.jpg', size=(height * 0.8, height * 0.1), size_hint=(None, None))
        logo_name_box.add_widget(logo_name)

        bookmarks_box = AnchorLayout(anchor_x="right", anchor_y="top")
        header_box.add_widget(logo_box)
        header_box.add_widget(logo_name_box)
        header_box.add_widget(bookmarks_box)
        body_box = BoxLayout(size=(wight, height * 0.89), size_hint=(None, None), orientation="vertical",
                             spacing=height * 0.01)

        screan_box = BoxLayout(size=(body_box.size[0], body_box.size[1]), size_hint=(None, None))
        screan_manager = ScreenManager()

        class Parallelepiped(Screen):
            def __init__(self, **kwargs):
                super(Parallelepiped, self).__init__(**kwargs)

                def my_callback(len, wight, deep, material, price, weight, full_price, self):
                    try:
                        weight.text = str(round(
                            (((float(len.text) * float(wight.text) * float(deep.text)) / 1000) * mat[
                                material.text]) / 1000,
                            3))
                        full_price.text = str(round(float(weight.text) * float(price.text), 3))
                        print(len.text)
                        print(wight.text)
                        print(deep.text)
                        print(material.text)
                        print(price.text)
                        print(weight.text)
                        print(full_price.text)
                        print(self)
                    except:
                        full_price.text = 'Не ввели материал'
                    try:
                        len = int(len.text)
                    except:
                        full_price.text = 'Не ввели длинну'
                    try:
                        wight = int(wight.text)
                    except:
                        full_price.text = 'Не ввели ширину'
                    try:
                        deep = int(deep.text)
                    except:
                        full_price.text = 'Не ввели глубину'
                    try:
                        price = int(price.text)
                    except:
                        full_price.text = 'Не ввели цену за кг'

                def button_event(self):
                    screan_manager.transition.direction = 'left'
                    screan_manager.current = "Втулка"

                self.name = "Параллелепипед"

                box = BoxLayout(orientation="vertical", spacing=body_box.size[1] * 0.01,
                                padding=(wight * 0.01, 0, wight * 0.01, 0))
                self.add_widget(box)

                button_slide_box = AnchorLayout(size=(body_box.size[0], body_box.size[1] * 0.095),
                                                size_hint=(None, None),
                                                anchor_x='center')
                button_slide = Button(text='Параллелепипед',
                                      size_hint=(None, None),
                                      size=(body_box.size[0] * 0.9, body_box.size[1] * 0.1), font_size=body_box.size[0] * 0.05)
                button_slide.bind(on_press=button_event)

                button_slide_box.add_widget(button_slide)
                box.add_widget(button_slide_box)

                len_box = BoxLayout()
                len_box.add_widget(Label(text="Длинна, мм", font_size=body_box.size[0] * 0.05))
                len_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(len_box)
                print(len_box.children[1].color)
                wight_box = BoxLayout()
                wight_box.add_widget(Label(text="Ширина, мм", font_size=body_box.size[0] * 0.05))
                wight_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(wight_box)
                deep_box = BoxLayout()
                deep_box.add_widget(Label(text="Глубина, мм", font_size=body_box.size[0] * 0.05))
                deep_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(deep_box)
                material_box = BoxLayout()
                material_box.add_widget(Label(text="Материал", font_size=body_box.size[0] * 0.05))
                S = Spinner(text="СЧ", values=(
                    'СЧ', 'Сталь', 'БрАЖ', 'БрОФ', 'Медь', 'Алюминий', 'Грфит', 'Песок кварцовый'),
                            font_size=body_box.size[0] * 0.05)
                S.option_cls = SpinnerOptions
                material_box.add_widget(S)
                box.add_widget(material_box)
                price_box = BoxLayout()
                price_box.add_widget(Label(text="Цена за кг, руб", font_size=body_box.size[0] * 0.05))
                price_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(price_box)
                weight_box = BoxLayout()
                weight_box.add_widget(Label(text="Вес, кг", font_size=body_box.size[0] * 0.05))
                weight_box.add_widget(Label(font_size=body_box.size[0] * 0.05))
                box.add_widget(weight_box)
                full_price_box = BoxLayout()
                full_price_box.add_widget(Label(text="Итог, руб", font_size=body_box.size[0] * 0.05))
                full_price_box.add_widget(Label(font_size=body_box.size[0] * 0.05))
                box.add_widget(full_price_box)
                event_button_box = BoxLayout()
                event_button = Button(text="Вычислить", size_hint=(1, 0.9), pos_hint={'center_x': .5, 'center_y': .5}, font_size=body_box.size[0] * 0.05)
                event_button.bind(
                    on_press=partial(my_callback, box.children[6].children[0], box.children[5].children[0],
                                     box.children[4].children[0], box.children[3].children[0],
                                     box.children[2].children[0], box.children[1].children[0],
                                     box.children[0].children[0]))
                event_button_box.add_widget(event_button)
                box.add_widget(event_button_box)

        class Bushing(Screen):
            def __init__(self, **kwargs):
                super(Bushing, self).__init__(**kwargs)

                def my_callback(d_out, d_in, len, material, price, weight, full_price, self):
                    try:
                        weight.text = str(round((math.pi * ((float(d_out.text) / 2) ** 2) * float(
                            len.text) - math.pi * ((float(d_in.text) / 2) ** 2) * float(len.text)) * mat[material.text] / 10**6, 3))
                        full_price.text = str(round(float(weight.text) * float(price.text), 3))
                    except:
                        full_price.text = 'Не ввели материал'
                    try:
                        len = int(len.text)
                    except:
                        full_price.text = 'Не ввели длинну'
                    try:
                        d_out = int(d_out.text)
                    except:
                        full_price.text = 'Не ввели D внешний'
                    try:
                        price = int(price.text)
                    except:
                        full_price.text = 'Не ввели цену за кг'
                    try:
                        d_in = int(d_in.text)
                    except:
                        weight.text = str(round((math.pi * ((float(d_out) / 2) ** 2) * float(
                            len) * mat[material.text]) / 10 ** 6, 3))
                        full_price.text = str(round(float(weight.text) * float(price), 3))

                def button_event(self):
                    screan_manager.transition.direction = 'right'
                    screan_manager.current = "Параллелепипед"

                self.name = "Втулка"

                box = BoxLayout(orientation="vertical", spacing=body_box.size[1] * 0.01,
                                padding=(wight * 0.01, 0, wight * 0.01, 0))
                self.add_widget(box)

                button_slide_box = AnchorLayout(size=(body_box.size[0], body_box.size[1] * 0.095),
                                                size_hint=(None, None),
                                                anchor_x='center')
                button_slide = Button(text='Втулка',
                                      size_hint=(None, None),
                                      size=(body_box.size[0] * 0.9, body_box.size[1] * 0.1), font_size=body_box.size[0] * 0.05)
                button_slide.bind(on_press=button_event)

                button_slide_box.add_widget(button_slide)
                box.add_widget(button_slide_box)

                d_out_box = BoxLayout()
                d_out_box.add_widget(Label(text="D внешний, мм", font_size=body_box.size[0] * 0.05))
                d_out_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(d_out_box)
                d_in_box = BoxLayout()
                d_in_box.add_widget(Label(text="D внутренний, мм", font_size=body_box.size[0] * 0.05))
                d_in_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(d_in_box)
                len_box = BoxLayout()
                len_box.add_widget(Label(text="Длинна, мм", font_size=body_box.size[0] * 0.05))
                len_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(len_box)
                material_box = BoxLayout()
                material_box.add_widget(Label(text="Материал", font_size=body_box.size[0] * 0.05))
                S = Spinner(text="СЧ", values=(
                    'СЧ', 'Сталь', 'БрАЖ', 'БрОФ', 'Медь', 'Алюминий', 'Грфит', 'Песок кварцовый'), font_size=body_box.size[0] * 0.05)
                S.option_cls = SpinnerOptions
                material_box.add_widget(S)
                box.add_widget(material_box)
                price_box = BoxLayout()
                price_box.add_widget(Label(text="Цена за кг, руб", font_size=body_box.size[0] * 0.05))
                price_box.add_widget(TextInput(input_filter="int", font_size=body_box.size[0] * 0.07))
                box.add_widget(price_box)
                weight_box = BoxLayout()
                weight_box.add_widget(Label(text="Вес, кг", font_size=body_box.size[0] * 0.05))
                weight_box.add_widget(Label(font_size=body_box.size[0] * 0.05))
                box.add_widget(weight_box)
                full_price_box = BoxLayout()
                full_price_box.add_widget(Label(text="Итог, руб", font_size=body_box.size[0] * 0.05))
                full_price_box.add_widget(Label(font_size=body_box.size[0] * 0.05))
                box.add_widget(full_price_box)
                event_button_box = BoxLayout()
                event_button = Button(text="Вычислить", size_hint=(1, 0.9), pos_hint={'center_x': .5, 'center_y': .5}, font_size=body_box.size[0] * 0.05)
                event_button.bind(
                    on_press=partial(my_callback, box.children[6].children[0], box.children[5].children[0],
                                     box.children[4].children[0], box.children[3].children[0],
                                     box.children[2].children[0], box.children[1].children[0],
                                     box.children[0].children[0]))
                event_button_box.add_widget(event_button)
                box.add_widget(event_button_box)

        screan_manager.add_widget(Parallelepiped())
        screan_manager.add_widget(Bushing())
        screan_box.add_widget(screan_manager)
        body_box.add_widget(screan_box)

        self.add_widget(header_box)
        self.add_widget(body_box)


class TestApp(App):
    def build(self):
        self.icon = 'logo.jpg'

        # Create the screen manager
        box_main = MainScrean()

        return box_main


if __name__ == '__main__':
    TestApp().run()
