from os import get_terminal_size, system
import sys
from random import randint, choice
from time import sleep
import string




def norm(procent: str):

    return int(get_terminal_size().columns*(int(procent[:-1])/100))


def ccinput(text, margin=7):

    print("\n"*(get_terminal_size().lines//2-1))
    return cinput(text, margin=margin)


def ccprint(text, fill=" ", speed=1, end="\n"):

    print("\n"*(get_terminal_size().lines//2-1))
    cprint(text, fill=fill, speed=speed, end=end)


def cprint(text, fill=" ", wrap=None, speed=-1, end="\n"):

    if wrap is None:
        wrap = len(text)
    elif type(wrap) is str:
        wrap = norm(wrap)

    text = text.replace("\n", "")
    parts = [text[x:x+wrap] for x in range(0, len(text), wrap)]
    
    for i, part in enumerate(parts):

        part = part.strip()
        if i != len(parts)-1:
            part = part.ljust(wrap, " ")
        
        ln = len(part)
        cols = get_terminal_size().columns
        
        left_margin = cols//2-ln//2
        if i == len(parts)-1:
            left_margin = left_margin - wrap//2 + ln//2
        right_margin = cols-ln-left_margin

        tleft = left_margin*fill
        tright = right_margin*fill

        print(tleft, end="")
        sprint(part, spd=speed)
        print(end=end)


def sprint(text, spd=1):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if spd <= 0:
            continue
        sleep(0.05*(1/spd))


def dcprint(text, fill=" ", wrap=None, speed=1):

    if wrap is None:
        wrap = len(text)
    elif type(wrap) is str:
        wrap = norm(wrap)

    text = text.replace("\n", "")
    spl = [i for i in text]
    for x in range(wrap-1, len(text), wrap):
        if (spl[x] != " ") and (spl[x+1] != " "):
            spl.insert(x, "-")
        else:
            spl.pop(x+1)
    cprint("".join(spl), wrap=wrap, fill=fill, speed=speed)


def cinput(text, margin=7):

    print(" "*(get_terminal_size().columns//2-len(text)-margin), end="")
    return input(text)


def hack_effect(seconds=3, speed=1, set_=string.ascii_letters,
                length=get_terminal_size().columns, align="left",
                fill=" "):
    #even loops is output amount of rows(some magick calculations that I dont understand)
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
        else: #center
            cprint(text, wrap=length, fill=fill)

        sleep(delay)
