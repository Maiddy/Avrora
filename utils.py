from os import get_terminal_size




def Twidth():

    return get_terminal_size().columns


def Theight():

    return get_terminal_size().lines


#converts to multiplier
def to_mult(n):

    type_ = type(n)
    
    if type_ is str:
        if n.endswith("%"):
            return int(Twidth() * (int(n[:-1]) / 100))
        raise ValueError("Percentage must ends with '%' char.")

    return n
