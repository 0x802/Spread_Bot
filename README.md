<h1 align="center">
  <br>
  <a href="https://github.com/HathemAhmed/Spread_Bot"><img src="https://pbs.twimg.com/profile_images/1081178168139173888/gu-s0K9T_200x200.jpg" alt="Spread Bot"></a>
  <br>
  Spread Bot
  <br>
</h1>

<h4 align="center">Spread Bot is a postman designed to send a specific message to a large number of sites</h4>


----------------------------------------------------------------------------------------------------
### _Why Spread Bot_

because it helps you to deliver a message to a thousand sites and also sorting sites that have accepted messages that did not accept and also does not leave any trace at the target sites etc...

----------------------------------------------------------------------------------------------------
###  _Features_

- easy to use
- Target multiple locations at the same time.
- Does not leave any trace in the target website.
- Scans websites before sending.
- find the mistakes and resolve it

----------------------------------------------------------------------------------------------------
###  _Install_

```bash
$ git clone https://github.com/HathemAhmed/Spread_Bot.git
$ cd Spread_Bot
$ python3 -m pip install -r requirements.txt
$ chmod +x spread_bot.py spread_dork.py
$ ./spread_bot.py -h/--help
   ____ ___  ____ ____ ____ ___   ___  ____ ___ 
   [__  |__] |__/ |___ |__| |  \  |__] |  |  |  
   ___] |    |  \ |___ |  | |__/  |__] |__|  |  
                                         

WORK: Spread Bot is a postman designed to send a specific message to a large number of sites

USAGE: spread_bot.py [options]

Options: 
   -n NAME,   --name      Name in the content of the message default [ anonymous ]
   -e EMAIL,  --email     Email content in message default [ anonymous@gmail.com ]
   -m MESSAGE,--message   Text in message content ** Mandatory **
   -p file,   --file      File contains the target site links default [ target.txt ] 


Example:
	python3 spread_bot.py -n <name> -e <email> -m <text> -f <file_targets_list>
	OR
	python3 spread_bot.py
```
----------------------------------------------------------------------------------------------------
### _Using_

**Extract sites using Dork**
```bash
$ ./spread_dork.py <dork>
```
**Example:**
```bash
$ ./spread_dork.py "inurl:contact site:co.ir" 
```

**Make the main tool work**

```bash
$ ./spread_bot.py -n <name> -e <email> -m <text>
```

**Example:**
```bash
$ ./spread_bot.py -n example -e example@example.com -m "Do You Like Spread Bot ?" -f target.txt
```

**Or** 
```bash
$ ./spread_bot.py 
```
----------------------------------------------------------------------------------------------------
### _Photos_

<img src="https://raw.githubusercontent.com/HathemAhmed/Spread_Bot/master/images/2.png" width=600px>
<img src="https://raw.githubusercontent.com/HathemAhmed/Spread_Bot/master/images/3.png" width=600px>

----------------------------------------------------------------------------------------------------

### :warning: Warning!

***I Am Not Responsible of any Illegal Use***

