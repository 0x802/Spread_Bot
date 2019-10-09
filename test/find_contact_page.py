#!/usr/bin/python3
import os
import sys
import time

# Color
R = '\033[1;31m'
T = '\033[1;33m'
B = '\033[1;34m'
G = '\033[1;32m'
W = '\033[1;37m'
U = '\033[1;4m'
F = '\033[1;7m'
N = '\033[0m'

try:
    import requests
except ImportError:
    print(f"[{R}!!!{N}] Error import 'requests' model ")
    exit()

try:
    import concurrent.futures
except ImportError:
    print(f"[{R}!!!{N}] Error import 'concurrent' model ")
    exit()
    

try:
    from interruptingcow import timeout
except ImportError:
    print(f"[{R}!!!{N}] Error import 'interruptingcow' model ")
    exit()


try: 
    from bs4 import BeautifulSoup
except ImportError:
    print(f"[{R}!!!{N}] Error import 'bs4' model ")
    exit()


SIS = requests.Session()
SIS.headers['User-Agent'] = ""

_URL_ = URL  = []


_LIST_ = [
    'Contact',
    'contact',
    'ContactUs',
    'contactus',
    'ContactUs.php',
    'contactus.php',
    'contact.php',
    'Contact.php',
    'CONTACT',
    'contact',
    'contact-details',
    'contact-en',
    'contact-form',
    'contact-info',
    'contact-lenses',
    'contact-me',
    'contact-off',
    'contact-tables',
    'contact-us',
    'Contact-Us',
    'Contact Us',
    'ContactUs.aspx',
    'contactus.aspx',
    'contact.aspx',
    'Contact.aspx',
    'contact us',
    'contact_a',
    'contact_address',
    'Contact_AddressBook',
    'Contact_Blog',
    'contact_button',
    'contact_call',
    'contact_details',
    'contact_e',
    'contact_editor',
    'contact_en',
    'contact_form',
    'contact_forms',
    'ContactUs.asp',
    'contactus.asp',
    'contact.asp',
    'Contact.asp',
    'contact_head',
    'contact_icon',
    'contact_index',
    'contact_info',
    'contact_information',
    'contact_list',
    'contact_main',
    'Contact_Management',
    'contact_new',
    'contact_off',
    'Contact_OffLine',
    'contact_on',
    'contact_osdl',
    'contact_pair',
    'contact_remove',
    'contact_reseller',
    'contact_sales',
    'contact_secunia',
    'contact_support',
    'Contact_Tables',
    'contact_title',
    'contact_top',
    'contact_up',
    'contact_us',
    'Contact_Us',
    'Contact_us',
    'contact_web',
    'Contact_WWW',
    'contact1',
    'contact2',
    'contactar',
    'contactbut',
    'contactbutton',
    'contactcw',
    'contacte',
    'contactenos',
    'contactform',
    'contactus-off',
    'contactus_off',
    'contactus1',
    'ContactUsForm'
    
]
def GET_PATH(*args, **kwargs):
    if args[1] is 1:
        try:
            
            read_file = [i.rstrip('\n') for i in open(args[0]).readlines()]
            [URL.append(f"{i.split('/')[0]}//{i.split('/')[2]}") for i in read_file]

        except FileNotFoundError:
            print(f"[{R}!!!{N}] Not Find The File {args[0]} ")
            exit()

    else:
        [open('target.txt', 'a').write(f'{i}\n') for i in args[0]]
        
        

def GET_URL(*args, **kwargs):
    URL_RUN = args[0]

    try:
        with timeout(3):
            try:
                GET = SIS.get(url=URL_RUN)
                if GET.status_code == 200:
                    _URL_.append(GET.URL_RUN)
                    print(f"[ {G}OK{N} ] Find url Contact {URL_RUN}")

                else:
                    print(f"[ {R}NO{N} ] {URL_RUN} is {GET.status_code}")
                    
            except requests.exceptions.ConnectionError:
                print(f"[ {R}NO{N} ] Error For Connection {URL_RUN}")
            
    except TimeoutError:
        print(f"[ {R}NO{N} ] Time Out {URL_RUN}")
    
def PROCESSING(*args, **kwargs):
    with concurrent.futures.ProcessPoolExecutor  () as EX:
        for i in _LIST_:
            for j in URL:
                try: 
                    rTARGETs = EX.submit(GET_URL, f'{j}/{i}')
                    PRO = rTARGETs.result()

                except RuntimeError:
                    print(f"[ {R}NO{N} ] Error for SyStem Time Out {j}")
                    
            

if __name__ == "__main__":
    try:
        s, dork = sys.argv
    except:
        dork = input(f"[ {R}*{N} ] Enter The Path File: ")
        if dork == '':
            dork = os.path.join(os.getcwd(), 'target.txt')

    DORK =  GET_PATH(dork, 1)

    PROCESSING(True)

    GET_PATH(_URL_, 2)
