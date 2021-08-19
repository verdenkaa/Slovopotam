import random

from kivy.app import App
from kivy.uix.behaviors import focus
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


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
    def build(self):
        layout = FloatLayout(size=(300, 300))

        layout.add_widget(Image(source='fon.gif', anim_delay= 0.1, mipmap= True, allow_stretch= True,
                    size_hint=(1, 1),
                    pos_hint={'center_x':0.5, 'center_y':0.5}))

        button = Button(text='Начать',
                        size_hint=(.5, .1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.on_press_button)

        layout.add_widget(button)
 
        return layout
 
    def on_press_button(self, instance):
        Menu().stop()
        Game().run()


class Game(App):
    global findword, defin, localscore
    

    print(findword)
    print(defin)


    def build(self):
        layout = FloatLayout(size=(300, 300))

        layout.add_widget(Image(source='fon.gif', anim_delay= 0.1, mipmap= True, allow_stretch= True,
                    size_hint=(1, 1),
                    pos_hint={'center_x':0.2, 'center_y':0.5}))

        layout.add_widget(Image(source='black.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x':0.8, 'center_y':0.5}))

        layout.add_widget(Label(text=defin,
                      size_hint=(0.5, 0.5),
                      pos_hint={'center_x': 0.7, 'center_y': 0.8}))

        textinput = TextInput(text='', multiline=False, size_hint=(0.5, 0.05),
                      pos_hint={'center_x': 0.7, 'center_y': 0.7})

        def on_focus(value):
            global localscore
            if findword.lower() == value.text.lower():
                print("ok")
                localscore += 1
                score = open('score.txt', 'r', encoding="utf-8")
                score2 = int(score.readline())
                if localscore > score2:
                    scorew = open('score.txt', 'w+', encoding="utf-8")
                    scorew.write(str(localscore))
                score.close()
                setword()
                print(findword)
                Game().stop()
                Menu().run()
            else:
                print("nonono", findword)
            value.text = ''
        textinput.bind(on_text_validate=on_focus)
        layout.add_widget(textinput)
        return layout


class Win(App):
    pass
 



Menu().run()