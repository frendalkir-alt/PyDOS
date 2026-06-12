# kernel/core.py

import time
from commands.builtins import execute_command, clear_screen
from kernel.colors import GREEN, BOLD, RESET # Импорт цветов для расцветки командной строки

# Эмулируем запуск
def loading():
    print("loading kernel...")
    time.sleep(1)
    print(f"{GREEN}[  OK  ]{RESET}")
    print("initializing drivers...")
    time.sleep(1.2)
    print(f"{GREEN}[  OK  ]{RESET}")
    print("starting user interface...")
    time.sleep(2)
    clear_screen()
    print(f"PyDOS v0.1")

# Основной цикл ядра
def main_loop():
    while True:
        user_input = input(f"{BOLD}>{RESET} ").strip().lower()
        if user_input == "": # На случай если user_input пустой (ничего не произойдёт)
            continue
        execute_command(user_input)