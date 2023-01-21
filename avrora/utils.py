from os import get_terminal_size, system
from platform import system as os_name




def clear():
    # TODO: support for MacOS
    name = os_name().lower()
    if "linux" in name:
        system("clear")
    elif "windows" in name:
        system("cls")
    else:
        print("\n" * Theight())


def Twidth():

    return get_terminal_size().columns


def Theight():

    return get_terminal_size().lines


def to_mult(n):
    # :|
    type_ = type(n)
    if type_ is str:
        if n.endswith("%"):
            return int(n[:-1]) / 100
        raise ValueError("Percentage must ends with '%' char.")

    return n
