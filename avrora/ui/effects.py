from avrora.ui.prints import mprint
from avrora.utils import Twidth, Theight, clear, to_mult
from random import choice, randint
from time import sleep
import string




def hack(seconds=3, speed=1, set_=string.ascii_letters,
            wrap=Twidth(), hmargin=0,
            fill=" "):
    # loops = rows to print
    if type(wrap) is str:
        wrap = int(Twidth() * to_mult(wrap))

    loops = 20*seconds*speed
    delay = seconds/loops
    
    for i in range(int(loops)):

        text = ""
    
        for j in range(wrap):

            text += choice(set_)
        
        mprint(text, wrap=wrap, fill=fill, hmargin=hmargin)

        sleep(delay)


def noise(seconds=3, speed=1, char="~", chance=20):

    loops = Theight()*seconds*speed

    screens = int(loops / Theight())
    delay = seconds / screens

    for x in range(screens):
        for i in range(int(loops)):
            line = ""
            for j in range(Twidth()):
                num = randint(0, 100)
                line += " " if num >= chance else char
            print(line)        
        sleep(delay)
        clear()
    clear()
