import random
import os
from colorama import Back, Fore, Style

import file_handle

current_joke_index = 0


def show_joke(index=current_joke_index):
    return file_handle.jokes[index]


def randomize_index():
    global current_joke_index
    current_joke_index = random.randint(0, 408)


def pick_matura_task():
    year = str(random.randrange(2018, 2022))
    extra = "D" if random.randint(0, 1) == 1 else ""
    task = str(random.randint(1, 15))
    return "Matura " + year + extra + " Task " + task


def show_collection(cursor):
    os.system('clear')
    print("#" + str(cursor))
    if file_handle.player_progress[cursor] == "Unlocked":
        print(show_joke(cursor))
    else:
        print("??????? ???? ?????? ?? ???????? ??? ???????\n"
              "??????? ??? ??????? ???? ?????? ???? ??????\n"
              "??????????? ?????? ?????? ???????? ????????\n"
              "?? ???????? ??? ???????? ??? ???????? ?????\n")
    print("Unlocked " + str(file_handle.player_progress.count("Unlocked")) + " of 407")
    user_input = input("<< " + Back.LIGHTWHITE_EX + Fore.BLACK + str(cursor) + Style.RESET_ALL + " >>")
    if user_input.lower() == 'd':
        if (cursor + 1) >= 408:
            cursor = 0
        show_collection(cursor + 1)
    if user_input.lower() == 'a':
        if (cursor - 1) <= 0:
            cursor = 408
        show_collection(cursor - 1)
    if user_input.lower() == 'b':
        return None
    if user_input.isdigit():
        show_collection(int(user_input))


def program():
    run_loop = True
    while run_loop:
        os.system('clear')
        randomize_index()
        print("#" + str(current_joke_index) + "\n" + show_joke(current_joke_index))
        print(pick_matura_task())

        print(Back.LIGHTWHITE_EX + Fore.BLACK + "C" + Style.RESET_ALL + " - show collection")
        print(Back.LIGHTWHITE_EX + Fore.BLACK + "N" + Style.RESET_ALL + " - do not unlock")
        user_input = input(Back.LIGHTWHITE_EX + Fore.BLACK + "Enter" + Style.RESET_ALL + " - unlock and go next")
        if user_input.upper() == "C":
            show_collection(1)
        if user_input.upper() == "N":
            file_handle.player_progress[current_joke_index] = "Locked"
        else:
            file_handle.player_progress[current_joke_index] = "Unlocked"
            file_handle.save_save_file()


if __name__ == "__main__":
    file_handle.initiate()
    program()
