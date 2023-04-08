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


def pick_task_new():
    for i in range(1, len(file_handle.task_rows)):
        random_range = str(file_handle.task_rows[i]).split(" !").pop().split("-")
        random_ors = str(file_handle.task_rows[i]).split("|")
        # If there is random range
        if len(random_range) == 2 and str(file_handle.task_rows[i]).find("!") >= 1:
            print("".join(str(file_handle.task_rows[i]).split(" !")[:1]) + ": "
                  + str(random.randint(int(random_range[0]), int(random_range[1]))))
        # If there is or argument
        else:
            print(random_ors[random.randint(0, len(random_ors) - 1)])
    print()


def format_colored_text(text, fr=None, bg=None):
    color_code = ''
    if bg:
        color_code += getattr(Back, bg.upper())
    if fr:
        color_code += getattr(Fore, fr.upper())
    return color_code + text + Style.RESET_ALL


def unlock_joke(index):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Joke #" + str(index) + " unlocked!\n" + show_joke(index))
    file_handle.player_progress[index] = "Unlocked"
    file_handle.save_save_file()
    input(format_colored_text("Click to run another task...", "BLACK", "LIGHTWHITE_EX"))


def program():
    run_loop = True
    while run_loop:
        os.system('cls' if os.name == 'nt' else 'clear')
        randomize_index()
        pick_task_new()

        print(format_colored_text("C", "BLACK", "LIGHTWHITE_EX") + " - show collection")
        print(format_colored_text("N", "BLACK", "LIGHTWHITE_EX") + " - did not complete task")
        user_input = input(format_colored_text("Enter", "BLACK", "LIGHTWHITE_EX") + " - Task complete\n")
        if user_input.upper() == "C":
            collection_screen.show_collection(0)
        if user_input.upper() == "N":
            file_handle.player_progress[current_joke_index] = "Locked"
        if user_input.upper() == "":
            unlock_joke(current_joke_index)


if __name__ == "__main__":
    file_handle.initiate()
    program()
