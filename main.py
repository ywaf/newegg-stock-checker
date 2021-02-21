# Made By Leho | github.com/lehoooo
import json
import time
import requests
import datetime
from bs4 import *

webhook = "PUT WEBHOOK URL HERE" # put webhook url here

intervals = int(10) # how long it will wait after checking

print('''
 ________   _______   ___       __   _______   ________  ________          ________  _________  ________  ________  ___  __           
|\   ___  \|\  ___ \ |\  \     |\  \|\  ___ \ |\   ____\|\   ____\        |\   ____\|\___   ___\\   __  \|\   ____\|\  \|\  \         
\ \  \\ \  \ \   __/|\ \  \    \ \  \ \   __/|\ \  \___|\ \  \___|        \ \  \___|\|___ \  \_\ \  \|\  \ \  \___|\ \  \/  /|_       
 \ \  \\ \  \ \  \_|/_\ \  \  __\ \  \ \  \_|/_\ \  \  __\ \  \  ___       \ \_____  \   \ \  \ \ \  \\\  \ \  \    \ \   ___  \      
  \ \  \\ \  \ \  \_|\ \ \  \|\__\_\  \ \  \_|\ \ \  \|\  \ \  \|\  \       \|____|\  \   \ \  \ \ \  \\\  \ \  \____\ \  \\ \  \     
   \ \__\\ \__\ \_______\ \____________\ \_______\ \_______\ \_______\        ____\_\  \   \ \__\ \ \_______\ \_______\ \__\\ \__\    
    \|__| \|__|\|_______|\|____________|\|_______|\|_______|\|_______|       |\_________\   \|__|  \|_______|\|_______|\|__| \|__|    
                                                                             \|_________|                                             
                                                                                                                                      
                                                                                                                                      
 ________  ___  ___  _______   ________  ___  __    _______   ________                                                                
|\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \ |\  ___ \ |\   __  \                                                               
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \                                                              
 \ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \ \  \_|/_\ \   _  _\                                                             
  \ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \|                                                            
   \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\                                                            
    \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|                                                           
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
''')

print("Made By Leho | github.com/lehoooo\n\n\n\n")

itemurl = input("Enter The Newegg URL: ")

while True:
    urlreq = requests.get(itemurl)

    soup = BeautifulSoup(urlreq.text, 'html.parser')

    title = soup.find('title').get_text()
    print("Monitoring Item - " + title)

    x = datetime.datetime.now()
    timenow = x.strftime("%x %X")

    instock = {
        "embeds": [{
            "author": {
                "name": "Newegg Stock Checker | Made By Lehoooo",
                "url": "https://github.com/lehoooo",
            },
            "footer": {
                "text": "Time: " + timenow,
            },
            "title": "In Stock!",
            "description": title + " Is In stock right now!",
            "color": "65331",
        },
            {
                "title": "Link",
                "url": itemurl,
                "color": "65331",

            }

        ]
    }

    outofstock = {
        "embeds": [{
            "author": {
                "name": "Newegg Stock Checker | Made By Lehoooo",
                "url": "https://github.com/lehoooo",
            },
            "footer": {
                "text": "Time: " + timenow,
            },
            "title": "Out Of Stock",
            "description": title + " Is out of stock right now!",
            "color": "16711680",
        },
            {
                "title": "Link",
                "url": itemurl,
                "color": "16711680",

            }

        ]
    }

    if "OUT OF STOCK.</strong>" in urlreq.text:
        print("Currently out of stock")
        print("Checked At: " + timenow)
        r = requests.post(webhook, data=json.dumps(outofstock), headers={'Content-Type': 'application/json'})
    elif "In stock.</strong>" in urlreq.text:
        print("Currently in stock!")
        print("Checked At: " + timenow)
        r = requests.post(webhook, data=json.dumps(instock), headers={'Content-Type': 'application/json'})

    elif "Are you a human?" in urlreq.text:
        print("We Are being rate limited.")

    print("waiting " + str(intervals) + " mins until runnning again")
    time.sleep(intervals * 60)
