import random
import os
from colorama import Back, Fore, Style

import collection_screen
import file_handle

current_joke_index = 0


def show_joke(index=current_joke_index):
    return file_handle.jokes[index]


def randomize_index():
    global current_joke_index
    current_joke_index = random.randint(0, 408)


def pick_task():
    year = str(random.randrange(2018, 2022))
    extra = "D" if random.randint(0, 1) == 1 else ""
    task = str(random.randint(1, 15))
    return "Matura " + year + extra + " Task " + task


def format_colored_text(text, fr=None, bg=None):
    color_code = ''
    if bg:
        color_code += getattr(Back, bg.upper())
    if fr:
        color_code += getattr(Fore, fr.upper())
    return color_code + text + Style.RESET_ALL


def program():
    run_loop = True
    while run_loop:
        os.system('cls' if os.name == 'nt' else 'clear')
        randomize_index()
        print("#" + str(current_joke_index) + "\n" + show_joke(current_joke_index))
        print(pick_task())

        print(Back.LIGHTWHITE_EX + Fore.BLACK + "C" + Style.RESET_ALL + " - show collection")
        print(Back.LIGHTWHITE_EX + Fore.BLACK + "N" + Style.RESET_ALL + " - do not unlock")
        user_input = input(Back.LIGHTWHITE_EX + Fore.BLACK + "Enter" + Style.RESET_ALL + " - unlock and go next")
        if user_input.upper() == "C":
            collection_screen.show_collection(0)
        if user_input.upper() == "N":
            file_handle.player_progress[current_joke_index] = "Locked"
        else:
            file_handle.player_progress[current_joke_index] = "Unlocked"
            file_handle.save_save_file()


if __name__ == "__main__":
    file_handle.initiate()
    program()
