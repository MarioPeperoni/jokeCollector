import joke_importer

jokes = []
player_progress = []


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


def initiate():
    load_jokes()
    load_save_file()
