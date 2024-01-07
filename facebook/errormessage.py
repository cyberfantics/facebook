from colors import *
import sys
def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()
errMsg = lambda msg: write(RED+"\n["+YELLOW+"!"+RED+"] Error: "+BLUE+msg+RED+ " !!!\n"+WHITE)
