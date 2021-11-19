from os import system
import socket
from time import sleep
import json
import httpx as requests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ping(website=None):
    try:
        requests.get("https://"+website)
        return True
    except:
        try:
            requests.get("http://"+website)
            return True
        except:
            try:
                requests.get(website)
                return True
            except:
                return False

sites = ['https://a-site.glitch.me/', 'https://meme-api.herokuapp.com/', 'https://Repl-pinger-1--proxneon.repl.co', 'PDDB--proxneon.repl.co']

while True:
    status = '\n'
    for site in sites:
        output = ping(site)
        if output == True:
            status = status + f'{site} is up\n'
        else:
            status = status + f'{site} is down\n'
    print(f'{status}\n')
    sleep(60)