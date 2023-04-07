import os

import main
import file_handle


def show_collection(cursor):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" + str(cursor + 1))
    if file_handle.player_progress[cursor] == "Unlocked":
        print(main.show_joke(cursor))
    else:
        print("??????? ???? ?????? ?? ???????? ??? ???????\n"
              "??????? ??? ??????? ???? ?????? ???? ??????\n"
              "??????????? ?????? ?????? ???????? ????????\n"
              "?? ???????? ??? ???????? ??? ???????? ?????\n")
    print("Unlocked " + str(file_handle.player_progress.count("Unlocked")) + " of " + str(len(file_handle.jokes)))
    print(main.format_colored_text("L", "BLACK", "LIGHTWHITE_EX") + " - for list view")
    print(main.format_colored_text("A-D", "BLACK", "LIGHTWHITE_EX") + " - for navigation")
    user_input = input("<< " + main.format_colored_text(str(cursor + 1), "BLACK", "LIGHTWHITE_EX") + " >>")
    if user_input.lower() == 'd':
        if (cursor + 1) >= 408:
            cursor = -1
        show_collection(cursor + 1)
    if user_input.lower() == 'a':
        if (cursor - 1) < 0:
            cursor = 408
        show_collection(cursor - 1)
    if user_input.lower() == 'l':
        collection_list_view(0)
    if user_input.lower() == 'b':
        return None
    if user_input.isdigit():
        show_collection(int(user_input) - 1)


def collection_list_view(page):
    os.system('cls' if os.name == 'nt' else 'clear')
    # This variable keeps track of how many jokes have been displayed on the current page.
    page_entry = 0
    # This loop goes through each joke in the file.
    for index, state in enumerate(file_handle.player_progress):
        # If the current joke is unlocked, we display it.
        if file_handle.player_progress[(20 * page) + index] == "Unlocked":
            # We get the text of the joke.
            joke = file_handle.jokes[(20 * page) + index]
            # If the joke is longer than 40 characters, we split it into lines and display only the first line.
            if len(joke) > 40:
                joke_lines = file_handle.jokes[(20 * page) + index].split('\n')
                # If the first line is empty, we display the second line.
                if not joke_lines[0].strip():  # check if the first line is empty
                    joke = str(joke_lines[1].strip()).split(' ')
                    # We display the first 20 words of the joke, followed by "..." to indicate that the joke continues.
                    print("#" + str((20 * page) + index + 1) + " " + " ".join(joke[:20]) + "...")
                else:
                    # If the first line is not empty, we display it.
                    joke = str(joke_lines[0].strip()).split(' ')
                    # We display the first 20 words of the joke, followed by "..." to indicate that the joke continues.
                    print("#" + str((20 * page) + index + 1) + " " + " ".join(joke[:20]) + "...")
            # If the joke is shorter than 40 characters, we display it in full.
            else:
                print("#" + str((20 * page) + index + 1) + " " + joke.strip())
        # If the current joke is locked, we display a message indicating that it's locked.
        if state == "Locked":
            print("#" + str((20 * page) + index + 1) + " ???? ??? ????? ???? ???????? ??? ???? ?????")
        # We increment page_entry to keep track of how many jokes we've displayed on the current page.
        page_entry += 1
        # If we've displayed 20 jokes, we break out of the loop and stop displaying more jokes on this page.
        if page_entry >= 20:
            break
    print("Unlocked " + str(file_handle.player_progress.count("Unlocked")) + " of " + str(len(file_handle.jokes)))
    user_input = input("⌃⌃ " + main.format_colored_text("PAGE: " + str(page + 1), "BLACK", "LIGHTWHITE_EX") + " ⌄⌄")
    if user_input.lower() == "w" and page > 1:
        collection_list_view(page - 1)
    if user_input.lower() == "s" and page < (len(file_handle.jokes)/20) - 2:
        collection_list_view(page + 1)
