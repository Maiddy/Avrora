from Avrora.ui.prints import cprint
from Avrora.utils import Twidth
from random import choice




def hack(seconds=3, speed=1, set_=string.ascii_letters,
            length=Twidth(), align="left",
            fill=" "):
    # loops = rows to print
    loops = 20*seconds*speed
    delay = seconds/loops
    
    for i in range(int(loops)):

        text = ""
    
        for j in range(length):

            text += choice(set_)
        
        if align == "left":
            print(text)
        elif align == "right":
            pass
        else: # center as default
            cprint(text, wrap=length, fill=fill)

        sleep(delay)


def matrix():

    pass


def noise():

    pass
