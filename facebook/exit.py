from reset import clear
from colors import *
from banner import banner_small
def msg_exit():
    clear()
    banner_small()
    print("\n")
    print(f"\t[#] {GREENBG}{BLACK}Thank you for using this tool. \n")
    reset_color()
    exit(0)
