#!/usr/bin/python3
# spread_dork.py

import os
import sys
import time
from modules.tools import * 

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


def SAVE_URLS(URLs, FILE):
    read_file = str()

    try:
        tryread_file = [i.rstrip('\n') for i in open(FILE).readlines()]
  
    except FileNotFoundError:
        FILE = 'target.txt'
    
    with open(os.path.join(os.getcwd(), FILE), 'a') as f:
        try:
            '''
            If your need just url like this => http://<site>.com
            
            URL = f"{URLs.split('/')[0]}//{URLs.split('/')[2]}"

            '''
            
            URL = URLs
            
            if URL not in read_file:
                f.write(f'{URL}\n')
        except:
            pass
        

    
# [ URL ] GOOGLE
Url = "https://www.google.com"

# [ PAGE ] search IN GOOGLE 
Path_search = "/search?q="

# [ PROXY ] for searching 
# PROXY  = {"http":"http://200.255.122.170:8080"}

def STYLES(*args, **kwargs):
    
    print(f"{G}{index()}{N}\n\n{W}{'-'*50}{N}\n[ {B}+{N} ] Dork  : {args[0]:<10}\n[ {B}+{N} ] Result: {args[1]}\n[ {B}+{N} ] File  : {args[2]}\n[{B}==>{N}] Plaes Wite....\n{W}{'-'*50}{N}")



def GET_DATA(args, **kwargs):
    global GET 
    Target, Number = args.split(';')
    
    # Session FOR SITE 
    SIS = requests.Session()

    # EDITE THE USER AGENT FOR AECCES SOURSE SITE
    SIS.headers['User-Agent'] = ''
    
    # [ SET ]  Proxy In the Process 
    # SIS.proxies = PROXY 

    # [ GET ] THE DATA SOURSE
    with timeout(10):

        try:
            time.sleep(1.25)
            
            GET = SIS.get(f"{Url}{Path_search}{Target}&start={Number}{'&filter=0' if int(Number) > 0 else '' }")
            
            if GET.status_code != 200:
                print(f"[{R}!!!{N}] You've been banned from Google")
                return 'gogend'

        except TimeoutError:
            print(f"[{R}!!!{N}] Timeout Error");exit()
        
        except requests.exceptions.ConnectionError:
            print(f"[{R}!!!{N}] Sorry No internet");exit()
            
    
    
    # return DATA WITH CONTENT LIKE [ BIN ]
    return GET.content

def PINDEX(*args, **kwargs):
    # global GET 
    for i in args:
        ''' ANY URL IN GOOGLE SEARCH /url?q= ''' 

        if '/url?q=' in i[0]:i[0] = i[0].split('/url?q=')[-1].split('&sa=')[0]
            
        # END THE [ results ] AND EXIT ! 
        if '/search%3' in i[0] and i[1] == '':
            print(f"\n{'-'*50}\n[ {B}OK{N}  ]   Save All Urls in {i[4]}{N}\n[ {R}END{N} ]   Find {len(i[3]) - 1 } results \n{W}")
            exit()

        print(f"[ {T  if i[1] != '' else R }ID{N}  ]   {i[2]}\n[ {T  if i[1] != '' else R }TIT{N} ]   {N}{i[1]}\n[ {T  if i[1] != '' else R}URL{N} ]   {N}{i[0]}\n{W}{'='*50}{N}")
        SAVE_URLS(i[0], i[4])
        



def GET_URLS(*args, **kwargs):
    NUM = ID = int()
    LIST = []
    while True:
                # Threading in the secript 
        with concurrent.futures.ProcessPoolExecutor() as excutor:
            try:
                rDATA = excutor.submit(GET_DATA, f'{args[0]};{NUM}')
                lDATA = rDATA.result()
            
            except RuntimeError:
                PINDEX(['','','', [],args[1]])
                continue
            
            except KeyboardInterrupt:
                break
    
        if lDATA == 'gogend':
            break
        
        # RUN BeautifulSoup TO FIND THE URL AND TITLE
        FORMATS = BeautifulSoup(lDATA, "html5lib")
        
        # CLASS THE div FOR URL AND TITLE
        for i in FORMATS.findAll("div", {"class":"ZINbbc xpd O9g5cc uUPGi"}):
            
            # THIS IS PROCESSING FOR OUTPUT URL 
            try:URL = i.find("a").get('href')
            except:URL = ""
            if "www.google.com" in URL:URL = ""
            if "/search?ie=UTF-8" in URL:URL = ""

            # THIS IS PROCESSING FOR OUTPUT TITLE                
            try:TITLE = i.find("div", {"class":"BNeawe vvjwJb AP7Wnd"}).text
            except:TITLE = ""

            # THIS IS PROCESSING FOR LIST  
            if TITLE is "" and URL is "":continue
            
            ID +=1
            LIST.append(URL)
            PINDEX([URL,TITLE,ID, LIST, args[1]])

        # if len(LIST) >= int(args[1]):break
            
        NUM = len(LIST)  
        

             
if __name__ == "__main__":
    try:
        s, *dork = sys.argv
    except:
        pass
    
    FILE = input(f"[ {R}*{N} ] File Output default is target.txt [ Y/N ]: ")
    if FILE.upper() == 'Y' or FILE == '':
        FILE = 'target.txt'    
    
    else:
        FILE = input(f"[ {R}*{N} ] Enter Path File Output: ")


    if dork != []:
        if len(dork) >= 1:
            DORK = str()

            for i in dork:
                DORK += f'{i} '

            STYLES(DORK.strip(), 1000, FILE)
            GET_URLS(DORK.strip(), FILE)
        
    else: 
        YES = input(f"[ {R}*{N} ] Enter The Dork : ")

        STYLES(YES.strip(), 1000, FILE)
        GET_URLS(YES.strip(), FILE)
