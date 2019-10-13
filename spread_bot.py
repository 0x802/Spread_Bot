#!/usr/bin/python3
# spread_bot.py

import os
import sys
import time
import random
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


'''

    [ Errors ]

'''

# Connact 
CONNECTIONERROR = 'No Connact For The Website'

# Time Out
TIMEOUTERROR    = 'Time Out'

# Problem in the web site
PROBLEMWEBSITE  = 'Problem In The Website'

# No Forms in the web site
NOFORM          = 'Not Found Form In The Website'

# No Found File
NOTFOUNDFILE    = 'Sorry File Not Found'


'''

    [ Basic Values ]

'''

# GET NO 
NOGET = f'[ {B}GET{N} ] [ {R}NO{N} ]'

# GET OK
OKGET = f'[ {B}GET{N} ] [ {G}OK{N} ]'

# SET NO
NOSET = f'[ {T}SET{N} ] [ {R}NO{N} ]'

# SET OK 
OKSET = f'[ {T}SET{N} ] [ {G}OK{N} ]'

# SYSTEM NO
NOSYS = f'[ {W}SYS{N} ] [ {R}NO{N} ]'

# FORM 
FORM  = f'[ {T}SET{N} ] [ {G}FORM{N} ]'

# END
END   = f'[ {W}END{N} ] [ {R}EXIT{N} ]' 

# Session <...>
SIS = requests.Session()
SIS.headers['User-Agent'] = '' # Aliens lol 

def CHACK_SYS_INPIUT():

    # Elements
    NAME = EMAIL  = MESSAGE = PATH_URL_LIST = str()
    
    if len(sys.argv) > 1:

        # Name  Message
        if '-n' in sys.argv or '--name' in sys.argv:
           
            try:
                NAME =  sys.argv[ sys.argv.index('-n') + 1 ]
           
            except ValueError:
                
                try:
                    NAME =  sys.argv[ sys.argv.index('--name') + 1 ]
                
                except IndexError:
                    pass
                    
            except IndexError:
                pass
       
        # Email Message
        if '-e' in sys.argv or '--email' in sys.argv:
          
            try:
                EMAIL =  sys.argv[ sys.argv.index('-e') + 1 ]
            
            except ValueError:
               
                try:
                    EMAIL =  sys.argv[ sys.argv.index('--email') + 1 ]
                    
                except IndexError:
                    pass
                
            except IndexError:
                pass

        # Text Message
        if '-m' in sys.argv or '--message' in sys.argv:
          
            try:
                MESSAGE =  sys.argv[ sys.argv.index(  '-m') + 1 ]

            except ValueError:
               
                try:
                    MESSAGE =  sys.argv[ sys.argv.index('--message') + 1 ]
                    
                except IndexError:
                    pass

            except IndexError:
                pass
        
        # file the url list
        if '-f' in sys.argv or '--file' in sys.argv:
          
            try:
                PATH_URL_LIST = sys.argv[ sys.argv.index('-f') + 1 ]

            except ValueError:

                try:
                    PATH_URL_LIST =  sys.argv[ sys.argv.index('--file') + 1 ]
                    
                except IndexError:
                    pass

            except IndexError:
                pass
        
        if '-h' in sys.argv or '--help' in sys.argv:
            help()
            exit()
        
    return [NAME, EMAIL, MESSAGE, PATH_URL_LIST]



def INDEX_THE_SCRIPT(*args, **kwargs):
    i_name , i_email, i_message, i_path = args
    
    print(f"{G}{index()}{N}{W}{'-'*50}\n|{N}\t\t{T}Details Of Your Message{W}\n|\n|{N} [ {G}+{N} ]{' Name':<10}: {i_name}\n{W}|{N} [ {G}+{N} ]{' Email':<10}: {i_email}\n{W}|{N} [ {G}+{N} ]{' Message':<10}: {i_message}\n{W}|{N} [ {G}+{N} ]{' Url List':<10}: {i_path}\n{W}|\n{'-'*50}\n{N}")

    time.sleep(1.25)


def GET_LIST_WEBSLITES(*args, **kwargs):
    
    return [i.rstrip('\n') for i in open(args[0]).readlines()]

 
def GET_CHACK_URL_CONTENT(*args, **kwargs):
    URL  = args[0]
   
    try:
        
        with timeout(10):
        
            try:
        
                CON = SIS.get(url=URL)
                
                if CON.status_code == 200:
   
                    error = 0
                    print(f"{OKGET} Status {URL[0:40]+'...' if len(URL) >= 40 else URL} is {G}{CON.status_code}{N}")

                else:
   
                    error = 1
                    print(f"{NOGET} Status {URL[0:40]+'...' if len(URL) >= 40 else URL} is {R}{CON.status_code}{N}")

            except requests.exceptions.ConnectionError:
   
                error = 2
                print(f"{NOGET} {CONNECTIONERROR} {URL[0:40]+'...' if len(URL) >= 40 else URL}")

            except requests.exceptions.MissingSchema:
   
                error = 2
                print(f"{NOGET} {PROBLEMWEBSITE} {URL[0:40]+'...' if len(URL) >= 40 else URL}")

    except TimeoutError:
   
        error = 3
        print(f"{NOGET} {TIMEOUTERROR} {URL[0:40]+'...' if len(URL) >= 40 else URL}")


       
    if error == 0:
        return CON

    elif error == 1:
        return 'code#|'

    elif error==2:
        return 'connect#|'

    elif error == 3:
        return 'time#|'



    
def GET_SEND_MESSAGE(*args, **kwargs):
    s_name, s_email,s_hidden,s_message, s_list,name_name, name_email,name_hidden,name_message = args[0].split('#|')

    try:
      
        with timeout(10):
      
            try:
      
                MES = SIS.post(url=s_list,
                               data={
                                        name_name:s_name,
                                        name_email:s_email,
                                        name_message:s_message,
                                        name_hidden if name_hidden != '' else '':s_hidden if s_hidden != '' else ''
                                    }
                               )
                
                if MES.status_code == 200:
                    return 'ok'

                else:
                    return f'code#|{MES.status_code}'

            except requests.exceptions.ConnectionError:
                return 'connect#|'

    except TimeoutError:
        return 'time#|'


def PROCESSING(*args, **kwargs):
    p_name, p_email, p_message, p_list  = args
   
    with concurrent.futures.ProcessPoolExecutor  () as EX:
        
        for i in p_list:

            try: 
                rTARGETs = EX.submit(GET_CHACK_URL_CONTENT, i)
                PRO = rTARGETs.result()

            except RuntimeError:
                print(f"{NOSYS} {TIMEOUTERROR} {i[0:40]+'...' if len(i)>=40 else i} ")
                continue
            
            except requests.exceptions.TooManyRedirects:
                print(f"{NOSYS} {TIMEOUTERROR} Exceeded 40 redirects {i[0:40]+'...' if len(i)>=40 else i} ")
                continue
                

            if "connect#|" in PRO:
                continue
           
            elif "time#|" in PRO:
                continue
            
            elif 'code#|' in PRO:
                continue

            else:
              
                GET = PRO
                FORMATS = BeautifulSoup(GET.text, "html5lib")

                name = email = hidden = hidden_v = message  = str()
                name_b = email_b = hidden_b = False

                for i in FORMATS.findAll("input"):
                    '''
                    
                    <input type="text" name="[a-z][A-z]">
                    
                    '''
                    if i.get("name") == "name" or i.get("name") == "name".title()  or i.get("name") == "firstname" and name_b == False:
                        name= i.get("name")
                        name_b = True
                        
                    else:
                        if i.get("type") == "text" and name_b == False:
                            name = i.get("name")
                    

                    '''
                    
                    <input type="email" name="[a-z][A-z]">
                    
                    '''
                    if i.get("name") == "email" or i.get("name") == "email".title() and email_b == False:
                        email = "email"
                        email_b = True

                    else:
                        if i.get("type") == "email" and  email_b == False:
                            email = i.get("name")


                    '''
                    
                    <input type="hidden" name="[A-Z][a-z][0-9]" value="[A-Z][a-z][0-9]">
                    
                    '''
                    if i.get("type") == "hidden" and hidden_b == False:
                        hidden   = i.get('name')
                        hidden_v = i.get("value")
                        hidden_b = True
                    
                for i in FORMATS.findAll("textarea"):
                    message = i.get("name")

                if name == '' or email == '' or message == '':
                    print(f"{NOSET} {NOFORM} {PRO.url[0:40]+'...' if len(PRO.url) >= 40 else PRO.url}")
                    continue
                
                else:
                    
                    try:
                    
                        rTARGET = EX.submit(GET_SEND_MESSAGE, f"{p_name}#|{p_email}#|{p_message}#|{hidden if hidden != '' else ''}#|{PRO.url}#|{name}#|{email}#|{hidden_v}#|{message}")
                        PRO2 = rTARGET.result()

                        print(f"{FORM} {'Name':<10} : {name}\n{FORM} {'Email':<10} : {email}\n{FORM} {'Message':<10} : {message}\n{FORM} {'Hidden':<10} : {hidden_v[0:40]+'...' if len(hidden_v) >= 40 else hidden_v}")

                        if  'connect#|' in PRO2:
                            print(f"{NOSET} {CONNECTIONERROR} {args[0]}/{i}")
                            continue
                            
                        elif 'time#|' in PRO2:
                            print(f"{NOSET} {TIMEOUTERROR} {PRO.url[0:40]+'...' if len(PRO.url) >= 40 else PRO.url}")
                            continue
                       
                        elif 'code#|' in PRO2:
                            print(f"{NOSET} Status {PRO.url[0:40]+'...' if len(PRO.url) >= 40 else PRO.url} is {PRO2.split('#|')[1]}")
                            continue    
                        
                        elif PRO2 == 'ok':
                            print(f"{OKSET} Send message for {PRO.url[0:40]+'...' if len(PRO.url) >= 40 else PRO.url}")
                   
                    except RuntimeError:
                        print(f"{NOSYS} {TIMEOUTERROR} {i}")
                        
                    except TypeError:
                        print(f"{NOSYS} {TIMEOUTERROR} {i}")
                        
                        
        print(END)

if __name__ == "__main__":
    # Run CHACK SYS INPIUT
    NAME, EMAIL, MESSAGE, PATH_URL_LIST = CHACK_SYS_INPIUT()
    
    # NAME
    if NAME is '':
        NAME = input(f"[ {B}*{N} ] Enter Name in the content of the message: ")

        if NAME is '':
            NAME = 'anonymous'
        
    else:
        pass
    
    # Email
    if EMAIL is '':
        EMAIL = input(f"[ {B}*{N} ] Enter Email in the content of the message: ")

        if EMAIL is '':
            EMAIL = "anonymous@gmail.com"
    else:
        pass
    
    # Message
    if MESSAGE is '':
        MESSAGE = input(f"[ {B}*{N} ] Enter Text in the content of the message: ")

        if MESSAGE is '':
            print(f"[ {R}!{N} ] Pleas Write Message !")
            exit()

    else:
        pass
    
    # Path Url List
    if PATH_URL_LIST is '':
        PATH_URL_LIST = input(f"[ {B}*{N} ] Enter Name File Url List: ")

        if PATH_URL_LIST is  '':
            PATH_URL_LIST = os.path.join(os.getcwd(), "target.txt")
        
        else:
            PATH_URL_LIST = os.path.join(os.getcwd(), PATH_URL_LIST)

    else:
        pass
    
    # sys input values in this fun
    INDEX_THE_SCRIPT(NAME, EMAIL, MESSAGE, PATH_URL_LIST)
    
    # Find file urls targets 
    try:
        FILE = GET_LIST_WEBSLITES(PATH_URL_LIST)
    
    except FileNotFoundError:
        print(f"\n[{R}!!!{N}] {NOTFOUNDFILE} \n\nTry:\n\tpython3 {sys.argv[0]} -h/--help")
        exit()
    
    # Start The Script 
    PROCESSING(NAME, EMAIL, MESSAGE, FILE)
