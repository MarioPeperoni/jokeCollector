import random
import os
from colorama import Back, Fore, Style

import collection_screen, file_handle

current_joke_index = 0


def show_joke(index=current_joke_index):
    return file_handle.jokes[index]


def randomize_index():
    global current_joke_index
    current_joke_index = random.randint(0, len(file_handle.jokes) - 1)


def pick_task():
    if file_handle.tasks_mode == "@random":
        for i in range(1, len(file_handle.task_rows)):
            random_range = str(file_handle.task_rows[i]).split(" !").pop().split("-")
            random_ors = str(file_handle.task_rows[i]).split("|")
            # If there is random range
            if len(random_range) == 2 and str(file_handle.task_rows[i]).find("!") >= 1:
                print("".join(str(file_handle.task_rows[i]).split(" !")[:1]) + " "
                      + str(random.randint(int(random_range[0]), int(random_range[1]))))
            # If there is or argument
            else:
                print(random_ors[random.randint(0, len(random_ors) - 1)])
    elif file_handle.tasks_mode == "@order":
        try:
            print(file_handle.task_rows[file_handle.tasks_done + 1])
        except IndexError:
            print("All tasks done!")
    else:
        print("ERR: Task file is empty or wrong formatted.")
    print()


def format_colored_text(text, fr="BLACK", bg="LIGHTWHITE_EX"):
    color_code = ''
    if bg:
        color_code += getattr(Back, bg.upper())
    if fr:
        color_code += getattr(Fore, fr.upper())
    return color_code + text + Style.RESET_ALL


def unlock_joke(index):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(format_colored_text(str("Joke #" + str(index + 1) + " unlocked!"), "GREEN", ""))
    print(show_joke(index))
    file_handle.player_progress[index] = "Unlocked"
    collection_screen.current_session_unlocked_jokes.append(int(index + 1))
    file_handle.tasks_done += 1
    file_handle.tasks_done_current += 1
    file_handle.save_save_file()
    input(format_colored_text("Click to run another task..."))


def program():
    run_loop = True
    while run_loop:
        os.system('cls' if os.name == 'nt' else 'clear')
        randomize_index()
        pick_task()
        print("Tasks completed this session: " + format_colored_text(str(file_handle.tasks_done_current), "GREEN", ""))
        print("Total tasks completed: " + format_colored_text(str(file_handle.tasks_done), "GREEN", ""))
        print(format_colored_text("C") + " - show collection")
        print(format_colored_text("N") + " - did not complete task")
        user_input = input(format_colored_text("Enter") + " - Task complete\n")
        if user_input.upper() == "C":
            collection_screen.show_collection(0)
        if user_input.upper() == "N":
            file_handle.player_progress[current_joke_index] = "Locked"
        if user_input.upper() == "":
            unlock_joke(current_joke_index)


if __name__ == "__main__":
    file_handle.initiate()
    program()
