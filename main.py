import random
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

Window.fullscreen = True
elserandom = 1


def sizer(defin):
    deflist = defin.split()
    definsize = ""
    definsize_nontime = deflist[0]
    for i in range(len(deflist[1:])):
        if len(definsize_nontime) + 1 + len(deflist[i + 1]) <= 60:
            definsize_nontime += " " + deflist[i + 1]
        else:
            definsize += definsize_nontime + "\n"
            definsize_nontime = ""
    definsize += definsize_nontime
    return definsize


def word():
    base = open('base.txt', 'r', encoding="utf-8")
    line = random.choice(base.readlines())
    return line[:line.find("  ")], line[line.find("  ") + 2:]

findword, defin = word()


def setword():
    global findword, defin
    findword, defin = word()

localscore = 0


class Menu(App):
    global localscore

    localscore = 0

    def build(self):
        layout = FloatLayout(size=(300, 300))

        layout.add_widget(Image(source="black.png", size_hint=(4, 4),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Image(source='fon.gif', anim_delay=0.1, mipmap=True,
                                allow_stretch=True, size_hint=(1, 1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Image(source='score.gif', anim_delay=0.1,
                                mipmap=True,
                                allow_stretch=True, size_hint=(0.2, 0.2),
                                pos_hint={'center_x': 0.9, 'center_y': 0.1}))

        score = open('score.txt', 'r', encoding="utf-8")

        layout.add_widget(Label(text="Счет: " + score.readline(),
                                size_hint=(0.5, 0.5),
                                pos_hint={'center_x': 0.9, 'center_y': 0.185}))

        score.close()

        button = Button(text='Начать',
                        size_hint=(0.5, 0.1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.on_press_button)

        layout.add_widget(button)

        button = Button(text='Как играть?',
                        size_hint=(0.5, 0.1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button.bind(on_press=self.on_press_button2)

        layout.add_widget(button)

        button = Button(text='Об игре',
                        size_hint=(0.5, 0.1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.3})
        button.bind(on_press=self.on_press_button3)

        layout.add_widget(button)
        return layout

    def on_press_button(self, instance):
        Menu().stop()
        Game().run()

    def on_press_button2(self, instance):
        Menu().stop()
        Rule().run()

    def on_press_button3(self, instance):
        Menu().stop()
        Lise().run()


class Rule(App):
    def build(self):
        layout = FloatLayout(size=(300, 300))

        layout.add_widget(Image(source="black.png",
                                size_hint=(4, 4),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Label(text="Ну есть определение, а вам нужно угадать слово с одной попытки.\
                                      \nА кто говорил что будет легко?",
                                size_hint=(0.2, 1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.7}))

        button = Button(text='Меню',
                        size_hint=(0.3, 0.1),
                        pos_hint={'center_x': 0.2, 'center_y': 0.2})
        button.bind(on_press=self.on_press_button)

        layout.add_widget(button)
        return layout

    def on_press_button(self, instance):
        Rule().stop()
        Menu().run()


class Lise(App):
    def build(self):
        layout = FloatLayout(size=(300, 300))

        layout.add_widget(Image(source="black.png",
                                size_hint=(4, 4),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Label(text="Написана на коленке verdenkaa\
                                    \n\nЗа идею была взята настольная игра виселица\
                                    \n\nИ да, мне не лень было прописывать красивый фон,просто стиль такой. Мне нравится\
                                    \n\nЧто-бы выйти из это чуда, нажмите Esc.\
                                    \n\n Ну или можете использовать Alt+F4",
                                size_hint=(0.2, 1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.7}))

        button = Button(text='Меню',
                        size_hint=(0.3, 0.1),
                        pos_hint={'center_x': 0.2, 'center_y': 0.2})
        button.bind(on_press=self.on_press_button)

        layout.add_widget(button)
        return layout

    def on_press_button(self, instance):
        Lise().stop()
        Menu().run()


class Game(App):
    global findword, defin, localscore

    def build(self):
        global defin

        if len(defin) > 60:
            defin = sizer(defin)

        layout = FloatLayout(size=(300, 300))

        layout.add_widget(Image(source="black.png",
                                size_hint=(4, 4),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Image(source='fon.gif', anim_delay=0.1, mipmap=True,
                                allow_stretch=True, size_hint=(1, 1),
                                pos_hint={'center_x': 0.2, 'center_y': 0.5}))

        layout.add_widget(Image(source='black.png',
                                size_hint=(1, 1),
                                pos_hint={'center_x': 0.8, 'center_y': 0.5}))

        layout.add_widget(Label(text=defin, halign='center',
                                size_hint=(0.5, 0.5),
                                pos_hint={'center_x': 0.6, 'center_y': 0.8}))

        textinput = TextInput(text='', multiline=False, size_hint=(0.5, 0.05),
                              pos_hint={'center_x': 0.6, 'center_y': 0.7})

        def on_focus(value):
            global localscore
            if findword.lower() == value.text.lower():
                localscore += 1
                score = open('score.txt', 'r', encoding="utf-8")
                score2 = int(score.readline())
                score.close()
                if localscore > score2:
                    scorew = open('score.txt', 'w+', encoding="utf-8")
                    scorew.write(str(localscore))
                    scorew.close()
                Game().stop()
                Win().run()
            else:
                Game().stop()
                Loose().run()
            value.text = ''
        textinput.bind(on_text_validate=on_focus)
        layout.add_widget(textinput)
        return layout


class Win(App):
    def build(self):
        global elserandom
        layout = FloatLayout(size=(300, 300))
        layout.add_widget(Image(source="black.png",
                                size_hint=(4, 4),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Label(text="Правильно!",
                                size_hint=(0.5, 0.5),
                                pos_hint={'center_x': 0.5, 'center_y': 0.8}))

        x = "win" + str(elserandom) + ".gif"
        elserandom += 1
        if elserandom == 11:
            elserandom = 1
        layout.add_widget(Image(source=x, anim_delay=0.1, mipmap=True,
                                allow_stretch=True, size_hint=(0.5, 0.5),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        button = Button(text='Продолжить',
                        size_hint=(.5, .1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})

        button.bind(on_press=self.on_press_button)

        layout.add_widget(button)
        return layout

    def on_press_button(self, instance):
        Win().stop()
        setword()
        Game().run()


class Loose(App):
    def build(self):
        global elserandom
        layout = FloatLayout(size=(300, 300))
        layout.add_widget(Image(source="black.png",
                                size_hint=(4, 4),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        layout.add_widget(Label(text="На этом все...",
                                size_hint=(0.5, 0.5),
                                pos_hint={'center_x': 0.5, 'center_y': 0.8}))

        x = "loose" + str(elserandom) + ".gif"
        elserandom += 1
        if elserandom == 11:
            elserandom = 1
        layout.add_widget(Image(source=x, anim_delay=0.1, mipmap=True,
                                allow_stretch=True, size_hint=(0.5, 0.5),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        button = Button(text='Меню',
                        size_hint=(.5, .1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})

        button.bind(on_press=self.on_press_button)
        layout.add_widget(button)
        return layout

    def on_press_button(self, instance):
        Loose().stop()
        setword()
        Menu().run()
Menu().run()
