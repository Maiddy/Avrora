from time import sleep
import sys
from random import choice
import string
from os import get_terminal_size
from Avrora.utils import Twidth, Theight, to_mult




def ccinput(text, margin=7):

    print("\n" * (Theight() // 2 - 1))
    return cinput(text, margin=margin)


def cinput(text, margin=7):

    print(" "*(Twidth() // 2 - len(text) - margin), end="")
    return input(text)


def ccprint(text, fill=" ", speed=1, end="\n"):

    print("\n" * (Theight // 2 - 1))
    cprint(text, fill=fill, speed=speed, end=end)


def cprint(text, fill=" ", wrap=None, speed=-1, end="\n"):

    if wrap is None:
        wrap = len(text)
    elif type(wrap) is str:
        wrap = norm(wrap)

    # TODO: print ignoring escape chars
    #text = text.replace("\\", "\\\\")
    parts = [text[x:x+wrap] for x in range(0, len(text), wrap)]
    
    for i, part in enumerate(parts):

        part = part.strip()
        if i != len(parts)-1:
            part = part.ljust(wrap, " ")
        
        ln = len(part)
        cols = Twidth()
        
        left_margin = cols//2-ln//2
        if i == len(parts)-1:
            left_margin = left_margin - wrap//2 + ln//2
        right_margin = cols-ln-left_margin

        tleft = left_margin*fill
        tright = right_margin*fill

        print(tleft, end="")
        sprint(part, speed=speed)
        print(end=end)

# simulates typing
def sprint(text, speed=1):

    delay = 0.05/speed
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if speed <= 0:
            continue
        sleep(delay)

# same as cprint, but at the wrap inserts [char]
def dcprint(text, fill=" ", wrap="50%", speed=1, char="-"):

    wrap = to_mult(wrap)

    #text = text.replace("\n", "")
    chars = [i for i in text]
    for x in range(wrap-1, len(text), wrap):
        if (chars[x] != " ") and (chars[x+1] != " ") and (chars[x-1] != " "):
            chars.insert(x, char)
        elif (chars[x-1] == " "):
            chars.insert(x, " ")
        else:
            chars.pop(x+1)
    cprint("".join(chars), wrap=wrap, fill=fill, speed=speed)
