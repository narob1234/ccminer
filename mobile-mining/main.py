import os
import json
import time
import pip
from config import banner

try:
    with open("set-miner/mining-control.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            allow = loads['allow']
            bind = loads['bind']
            key = loads['key']
        
    os.system(f"cd set-miner && wget -N --timeout 20 --connect-timeout=30 -t 2 --no-check-certificate https://raw.githubusercontent.com/narob1234/ccminer/main/mobile-mining/set-miner/mining-control.json")
    time.sleep(2)
    from progress.bar import ShadyBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ShadyBar

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests
    
    
zergpool = ["stratum+tcp://verushash.mine.zergpool.com:3300","stratum+tcp://verushash.na.mine.zergpool.com:3300","stratum+tcp://verushash.eu.mine.zergpool.com:3300","stratum+tcp://verushash.asia.mine.zergpool.com:3300"]
    
    
def runOffline():
    banner()
    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
        if pool == "" or wallet == "":
            print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")

        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            name = loads['name']
            cpu = loads['cpu']
        if name == "":
           name = "noname"
        if cpu == "":
           cpu = "1"
        with open("set-miner/mining-control.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            allow = loads['allow']
            bind = loads['bind']
            key = loads['key']
    
        if key == "x":
           print("\033[1;34;40m")   
           print("WALLET =",wallet)
           print("NAME   =",name)
           print("POOL   =",pool)
           print("CPU    =",cpu) 
           print("PASS   =",password)
           print("\033[00m\n")
           os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u RQLmyfkCoDhRf19xCb8nXHstyx4qZXBYW4.{name} -p {password} -t {cpu}")
        elif key == "1":    
         print("\033[1;34;40m")   
         print("WALLET =",wallet)
         print("NAME   =",name)
         print("POOL   =",pool)
         print("CPU    =",cpu)
        if pool in zergpool:

           print("PASS   =",password +",id="+name)
           print("\033[00m\n")

         #  time.sleep(2)
           os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password},ID={name} -t {cpu}")
       
        else:
        	
         print("PASS   =",password)
         print("\033[00m\n")

        # time.sleep(2)
         os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
            
    except:
        push = {'pool': '','wallet': '','pass': ''}
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'name': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'allow': '','bind': '','key': ''}
        with open("set-miner/mining-control", "w") as set:
            json.dump(push, set, indent=4)
        
        
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ShadyBar("\033[32m Start Mining\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
            
        runOffline()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")
