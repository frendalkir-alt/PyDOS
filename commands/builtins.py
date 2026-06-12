# commands/builtins.py
# Здесь находятся все команды

import sys
import os
import time
from kernel.colors import YELLOW, RED, GREEN, RESET # Импорт цветов для расцветки командной строки

# Штука что-бы запускать команды
def execute_command(cmd: str) -> None:
    if cmd == "help":
        show_help()
    elif cmd == "ver":
        show_version()
    elif cmd == "exit":
        exit_dos()
    elif cmd == "cls":
        clear_screen()
    elif cmd == "time":
        show_time()
    else:
        print(f"{RED}Bad command or file name{RESET}")

# Весь код для команд
def show_help():
    print(f"""{GREEN}help{RESET} - {YELLOW}show this{RESET}
{GREEN}ver{RESET} - {YELLOW}show version{RESET}
{GREEN}time{RESET} - {YELLOW}show current time and date{RESET}
{GREEN}cls{RESET} - {YELLOW}clear screen{RESET}
{GREEN}exit{RESET} - {YELLOW}exit dos{RESET}""")

def show_version():
    print("PyDOS v0.1")

def exit_dos():
    print(f"{YELLOW}Shutting down...{RESET}")
    time.sleep(1)
    sys.exit(0)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_time():
    current_time = time.time()
    local_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(formatted_time)