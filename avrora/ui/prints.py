from time import sleep
import sys
from avrora.utils import Twidth, Theight, to_mult




def minput(text="", text_margin=0, vmargin=0, hmargin=0):

    if type(vmargin) is str:
        print("\n" * int(Theight() * to_mult(vmargin)), end="")
    else:
        print("\n" * vmargin, end="")

    if type(hmargin) is str:
        print(" " * (int(to_mult(hmargin) * Twidth()) - text_margin), end="")
    else:
        print(" " * (hmargin - text_margin), end="")
    
    return input(text)


#def ccprint(text, fill=" ", speed=1, end="\n"):

    #print("\n" * (Theight // 2 - 1))
    #cprint(text, fill=fill, speed=speed, end=end)


def mprint(text, vmargin=0, hmargin=0, fill=" ", wrap=None, speed=-1, char="",  _end="\n"):

    if wrap is None:
        wrap = len(text)
    elif type(wrap) is str:
        wrap = int(Twidth() * to_mult(wrap))
    
    chars = [i for i in text]

    text_ln = len(text)

    if wrap > text_ln:
        wrap = text_ln
    #if char:
        #for x in range(wrap-1, len(text), wrap):
            #if
            #next_ = (chars[x+1] != " ") if (x+1 >= text_ln) else False
            #if (chars[x] != " ") and (next_) and (chars[x-1] != " "):
                #chars.insert(x, char)
            #elif (chars[x-1] == " "):
                #chars.insert(x, " ")
            #else:
                #chars.pop(x+1)
        #text = "".join(chars)
    
    parts = [text[x:x+wrap] for x in range(0, len(text), wrap)]
    #print(parts)
    
    if type(vmargin) is str:
        vmargin = int(Theight() * to_mult(vmargin)) - len(parts) // 2

    print("\n" * vmargin, end="")

    if type(hmargin) is str:
        hmargin = int(Twidth() * to_mult(hmargin))
    
    for i, part in enumerate(parts):

        part = part.strip()
        if i != len(parts)-1:
            part = part.ljust(wrap, " ")
        
        ln = len(part)

        left_margin = hmargin - ln // 2
        if i == len(parts)-1:
            left_margin = left_margin - wrap//2 + ln//2
        #right_margin = cols-ln-left_margin

        tleft = left_margin*fill
        #tright = right_margin*fill

        
        print(tleft, end="")
        
        delay = 0.05/speed
        for char in part:
            sys.stdout.write(char)
            sys.stdout.flush()
            if speed <= 0:
                continue
            sleep(delay)
            
        print(end=_end)








