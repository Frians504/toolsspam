# Developer: MR.FRIANS | Versi: TOOLS V1

reset  = '\x1b[0m'
bold   = '\x1b[1m'
dark   = '\x1b[90m'
red    = '\x1b[31m'
green  = '\x1b[32m'
yellow = '\x1b[33m'
blue   = '\x1b[34m'
purple = '\x1b[35m'
cyan   = '\x1b[36m'
white  = '\x1b[37m'
RED    = '\x1b[91m'
GREEN  = '\x1b[92m'
YELLOW = '\x1b[93m'
BLUE   = '\x1b[94m'
PURPLE = '\x1b[95m'
CYAN   = '\x1b[96m'
WHITE  = '\x1b[97m'
liner  = '\x1b[4m'

import os
import random
import requests as req
req.urllib3.disable_warnings()
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as Yutix

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    warna = random.choice([CYAN, PURPLE, GREEN, RED, YELLOW])
    print(f"""{bold}
 {warna}╔═══════════════════════════════════════╗
 {warna}║{reset}         {bold}{liner}T  O  O  L  S   V1{reset}{warna}           ║
 {warna}╠═══════════════════════════════════════╣
 {warna}║{WHITE} Developer : {liner}MR.FRIANS{reset}{warna}                ║
 {warna}║{WHITE} Versi     : {liner}5{reset}{warna}                         ║
 {warna}║{WHITE} Github    : {liner}github.com/yutixcode{reset}{warna}     ║
 {warna}║{WHITE} Telegram  : {liner}t.me/yutixverse{reset}{warna}         ║
 {warna}╚═══════════════════════════════════════╝{reset}
    """)