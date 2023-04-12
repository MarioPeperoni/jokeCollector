import os

import jokeCollectorMain
import file_handle

current_session_unlocked_jokes = []


def show_collection(cursor):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Check if joke has been unlocked this session
    if (cursor + 1) in current_session_unlocked_jokes:
        print(jokeCollectorMain.format_colored_text(str("#" + str(cursor + 1)), "GREEN", ""))
    else:
        print("#" + str(cursor + 1))
    if file_handle.player_progress[cursor] == "Unlocked":
        print(jokeCollectorMain.show_joke(cursor))
    else:
        print("??????? ???? ?????? ?? ???????? ??? ???????\n"
              "??????? ??? ??????? ???? ?????? ???? ??????\n"
              "??????????? ?????? ?????? ???????? ????????\n"
              "?? ???????? ??? ???????? ??? ???????? ?????\n")

    print("Unlocked " + str(file_handle.player_progress.count("Unlocked")) + " of " + str(len(file_handle.jokes)))
    print(jokeCollectorMain.format_colored_text("L") + " - for list view")
    print(jokeCollectorMain.format_colored_text("A-D") + " - for navigation")

    user_input = input("<< " + jokeCollectorMain.format_colored_text(str(cursor + 1)) + " >>")
    if user_input.upper() == 'D':
        if (cursor + 1) >= 408:
            cursor = -1
        show_collection(cursor + 1)
    if user_input.upper() == 'A':
        if (cursor - 1) < 0:
            cursor = 408
        show_collection(cursor - 1)
    if user_input.upper() == 'L':
        collection_list_view(0)
    if user_input.upper() == 'B':
        return None
    if user_input.isdigit():
        show_collection(int(user_input) - 1)


def collection_list_view(page):
    os.system('cls' if os.name == 'nt' else 'clear')

    page_entry = 0  # Current entry on page

    for index, state in enumerate(file_handle.player_progress):

        # If the current joke is unlocked, we display it.
        if file_handle.player_progress[(20 * page) + index] == "Unlocked":
            joke = file_handle.jokes[(20 * page) + index]
            # If the joke is longer than 40 characters, we split it into lines and display only the first line.
            if len(joke) > 40:
                joke_lines = file_handle.jokes[(20 * page) + index].split('\n')
                first_line = joke_lines[0].strip()

                if not first_line:
                    joke = " ".join(joke_lines[1].strip().split(' ')[:20])
                else:
                    joke = " ".join(first_line.split(' ')[:20])
                if ((20 * page) + index) in current_session_unlocked_jokes:
                    print(jokeCollectorMain.format_colored_text(
                        f"#{(20 * page) + index + 1} {joke}...", "GREEN", ""))
                else:
                    print(f"#{(20 * page) + index + 1} {joke}...")

            # If the joke is shorter than 40 characters, we display it in full.
            else:
                print("#" + str((20 * page) + index + 1) + " " + joke.strip())

        if state == "Locked":
            print("#" + str((20 * page) + index + 1) + " ???? ??? ????? ???? ???????? ??? ???? ?????")
        # We increment page_entry to keep track of how many jokes we've displayed on the current page.
        page_entry += 1
        # If we've displayed 20 jokes, we break out of the loop and stop displaying more jokes on this page.
        if page_entry >= 20:
            break

    print("Unlocked " + str(file_handle.player_progress.count("Unlocked")) + " of " + str(len(file_handle.jokes)))

    user_input = input(
        "⌃⌃ " + jokeCollectorMain.format_colored_text("PAGE: " + str(page + 1), "BLACK", "LIGHTWHITE_EX") + " ⌄⌄")
    if user_input.upper() == "W" and page > 1:
        collection_list_view(page - 1)
    if user_input.upper() == "S" and page < (len(file_handle.jokes) / 20) - 2:
        collection_list_view(page + 1)
    if user_input.isdigit():
        show_collection(int(user_input) - 1)
