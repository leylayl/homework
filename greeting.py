Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys

def greeting():

    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    reset = "\033[0m"

    print(f"{red}Hello,{reset} {green}world!{reset}")
    print(f"How are you?{reset}")

