import jokeCollectorMain
import joke_importer

jokes = []
player_progress = []
task_mode = ""
task_rows = []


def create_save_file():
    with open('progress.joke', 'w') as file:
        for i in range(0, len(jokes)):
            file.write("Locked\n")


def load_save_file():
    try:
        with open('progress.joke', 'r') as file:
            lines = file.readlines()
            for line in lines:
                player_progress.append(line.strip())
            print("Save file loaded.")
    except FileNotFoundError:
        print("Save file not found. Creating new one...")
        create_save_file()
        load_save_file()


def save_save_file():
    with open('progress.joke', 'w') as file:
        for player_state in player_progress:
            file.write(player_state + "\n")


def load_jokes():
    try:
        index = 0
        with open('jokes.joke', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line == "|\n":
                    index += 1
                    jokes.append("")
                else:
                    if index >= len(jokes):
                        jokes.append("")
                    jokes[index] += line
            print("Jokes database loaded.")
    except FileNotFoundError:
        print("Jokes database not found. Fetching jokes... (This could take some time)")
        joke_importer.import_jokes(0, 800)
        load_jokes()


def load_tasks():
    try:
        with open('tasks.joke', 'r') as file:
            lines = file.readlines()
            lines[0] = task_mode
            for line in lines:
                task_rows.append(line.strip())

    except FileNotFoundError:
        create_template_tasks()
        input(jokeCollectorMain.format_colored_text("The task file could not be located in the directory. "
                                                    "A template file will be generated. "
                                                    "Please press any key to proceed with loading the task file.",
                                                    "BLACK", "LIGHTWHITE_EX"))
        load_tasks()


def create_template_tasks():
    with open('tasks.joke', 'w') as file:
        file.write("@random\n")
        file.write("This task generates number from 0 to 1000: !0-1000\n")
        file.write("To randomize numbers write ex mark and then separate numbers with '-'\n")
        file.write("To create random selection separate words with '|'\n")
        file.write("This|is|example|of|random|selection\n")


def initiate():
    load_jokes()
    load_save_file()
    load_tasks()
