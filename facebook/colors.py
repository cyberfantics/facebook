# ANSI colors (FG & BG)
RED = "\033[31m"       # Red #
GREEN = "\033[32m"     # Green #
ORANGE = "\033[33m"    # Orange #
BLUE = "\033[34m"       # BLUE #
YELLOW = "\033[1;33m"
MAGENTA = "\033[35m"    # Magenta #
CYAN = "\033[36m"       # Cyan #
WHITE = "\033[37m"      # White #
BLACK = "\033[30m"      # Black #
REDBG = "\033[41m"      # Red Background #
GREENBG = "\033[42m"    # Green Background #
ORANGEBG = "\033[43m"   # Orange Background #
BLUEBG = "\033[44m"     # Blue Background #
MAGENTABG = "\033[45m"  # Magenta Background #
CYANBG = "\033[46m"     # Cyan Background #
WHITEBG = "\033[47m"    # White Background #
BLACKBG = "\033[40m"    # Black Background #
RESETBG = "\e[0m\n"     # Reset Background and move to a new line #


# Reset terminal colors
def reset_color():
    print("\033[m", end="")
    return
