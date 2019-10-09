import sys

# Color
R = '\033[1;31m'
T = '\033[1;33m'
B = '\033[1;34m'
G = '\033[1;32m'
W = '\033[1;37m'
U = '\033[1;4m'
F = '\033[1;7m'
N = '\033[0m'

def index():
    sp = ' '*3
    sm = f"""
{sp}____ ___  ____ ____ ____ ___   ___  ____ ___
{sp}[__  |__] |__/ |___ |__| |  \  |__] |  |  |
{sp}___] |    |  \ |___ |  | |__/  |__] |__|  |


"""
    return sm 

def help():
    doce = "Spread Bot is a postman designed to send a specific message to a large number of sites"
    print(f"{G}{index()}{N}\nWORK: {doce}\n\nUSAGE: {sys.argv[0]} [options]\n\nOptions: \n{' '*3+'-n NAME,   --name':<25} Name in the content of the message default [ anonymous ]\n{' '*3+'-e EMAIL,  --email':<25} Email content in message default [ anonymous@gmail.com ]\n{' '*3+'-m MESSAGE,--message':<25} Text in message content ** Mandatory **\n{' '*3+'-p file,   --file':<25} File contains the target site links default [ target.txt ] \n\n\nExample:\n\tpython3 {sys.argv[0]} -n <name> -e <email> -m <text> -f <file_targets_list>\n\tOR\n\tpython3 {sys.argv[0]}")
