from colorama import Fore, init


init(autoreset=True)
class Log:
    def __init__(self, msg):
        print(Fore.YELLOW + msg)
