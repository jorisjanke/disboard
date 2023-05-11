from __future__ import absolute_import
try:
    import os
    import json
    import random
    import time
    import requests
    from time import *
    from colorama import Fore, Back as bg, Style, init
    init()
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3'} -m pip install {ex.name}'\nPress enter to exit")
    exit(1)
def infomessage(msg): #[!]
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}!{Fore.LIGHTBLACK_EX}]{Fore.CYAN} {msg}")
def questionmessage(msg): #[?]
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.BLUE}?{Fore.LIGHTBLACK_EX}]{Fore.CYAN} {msg}")
def bump(token, channelid):
    try:
        headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : token
        }
        requests.post(
        f"https://discord.com/api/channels/{channelid}/messages",
        headers = headers,
        json = {"content" : "!d bump"}
        )
        print(f"{Fore.GREEN}Bumped! -- {channelid} with {token}")
    except Exception as e:
        infomessage(f"Error with the ID or the Request-Libary: \n {e}")
def checktoken(token):
    try:
        response = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
        return True if response.status_code == 200 else False
    except:
        pass
print(f"""
{Fore.YELLOW}
{Fore.CYAN}.
                  {Fore.CYAN}.       {Fore.YELLOW}|         {Fore.CYAN}.    {Fore.CYAN}.
            {Fore.CYAN}.  {Fore.YELLOW}*         -*-          *
                 {Fore.YELLOW}\        |         /   {Fore.CYAN}.
{Fore.CYAN}.    .           {Fore.YELLOW} .     {Fore.YELLOW} /^\     .              {Fore.CYAN}.    {Fore.CYAN}.
   {Fore.YELLOW}*    |\   /\    /\  / / \ \  /\    /\   /|    *
 {Fore.CYAN}.   {Fore.CYAN}.  {Fore.YELLOW}|  \ \/ /\ \ / /     \ \ / /\ \/ /  | {Fore.CYAN}.     {Fore.CYAN}.
        {Fore.YELLOW} \ | _ _\/_ _ \_\_ _ /_/_ _\/_ _ \_/
           {Fore.YELLOW}\  *  *  *   \ \/ /  *  *  *  /
           {Fore.YELLOW} ` ~ ~ ~ ~ ~  ~\/~ ~ ~ ~ ~ ~ '

░█▀▄▀█ ░█▀▀█ ░█─── ░█▀▀█ ── ░█▀▄▀█ ░█─░█ ░█─── ▀▀█▀▀ ▀█▀ ░█▀▀█ ░█─── ░█▀▀▀ ── ▀▀█▀▀ ─█▀▀█ ░█▀▀▀█ ░█─▄▀ ── ░█▀▀█ ░█─░█ ░█▀▄▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 
░█░█░█ ░█▄▄▀ ░█─── ░█▄▄█ ▀▀ ░█░█░█ ░█─░█ ░█─── ─░█── ░█─ ░█▄▄█ ░█─── ░█▀▀▀ ▀▀ ─░█── ░█▄▄█ ─▀▀▀▄▄ ░█▀▄─ ▀▀ ░█▀▀▄ ░█─░█ ░█░█░█ ░█▄▄█ ░█▀▀▀ ░█▄▄▀ 
░█──░█ ░█─░█ ░█▄▄█ ░█─── ── ░█──░█ ─▀▄▄▀ ░█▄▄█ ─░█── ▄█▄ ░█─── ░█▄▄█ ░█▄▄▄ ── ─░█── ░█─░█ ░█▄▄▄█ ░█─░█ ── ░█▄▄█ ─▀▄▄▀ ░█──░█ ░█─── ░█▄▄▄ ░█─░█


{Fore.LIGHTGREEN_EX}
Please make sure that you configure the Tool!
Please configure the File "tasks.txt" like these:
{bg.WHITE}{Fore.BLACK}

token1:channelid1
token2:channelid2
token3:channelid3

{bg.RESET}{Fore.GREEN}
""")

while True:
    try:
        tasks = open("tasks.txt", "r")
    except Exception as e:
        infomessage("Please configure / create 'tasks.txt'!")
        infomessage(f"Error: {e}")
        break
    for line in tasks:
        try:
            task = line.split(":")
            token = str(task[0].replace("\n", ""))
            channelid = str(task[1].replace("\n", ""))
            if checktoken(token):
                try:
                    sleep(random.choice(range(5)))
                    bump(token, channelid)
                except:
                    infomessage("Error! Make Sure that the Accounts are added to the right servers!")
            else:
                infomessage("Invaild Token!")
            sleep(random.choice(range(5)))
        except Exception as e:
            infomessage(f"Error! System Crashed trying to restart...")
    print("\nAll Tasks finished! Waiting 2 hours before next execution!\n")
    sleep(121*60)
    try:
        tasks.close()
        print("\n Sucesfully reload Tasks. \n")
    except Exception as e:
        infomessage("Error with File-Management!")
        try:
            exit(1)
        except:
            break
