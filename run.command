#!/bin/bash

# Change directory to the directory where the script is located
# shellcheck disable=SC2164
cd "$(dirname "$0")/App"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    # Prompt the user to install Python
    echo "Python is not installed. Please install Python before running this app."
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. The app will be run without checking for updates."
    # Run the Python app
    command pip3 install colorama
    command pip3 install requests
    command pip3 install bs4
    python3 jokeCollectorMain.py
    exit 0
fi

# Set the repository URL and the local download directory
repo_url=https://github.com/MarioPeperoni/jokeCollector.git
download_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the latest commit hash from the repository
latest_commit=$(git ls-remote $repo_url HEAD | cut -f 1)

# Check if the latest commit hash matches the current commit hash
if [ -f "$download_dir/latest_commit.txt" ]; then
    current_commit=$(cat "$download_dir/latest_commit.txt")
    if [ "$current_commit" = "$latest_commit" ]; then
        echo "No new version is available."
        # Run the Python app
        command pip3 install colorama
        command pip3 install requests
        command pip3 install bs4
        python3 jokeCollectorMain.py
        exit 0
    fi
fi

# Prompt the user to download the new version
echo "A new version is available. Do you want to download and install it? (y/n)"
read answer

if [ "$answer" = "y" ]; then
    # Download the latest version from the repository
    echo "Downloading new version..."
    git clone $repo_url "$download_dir"/new_version
    echo "$latest_commit" > "$download_dir"/latest_commit.txt

    # Copy the new version files to the destination directory
    # shellcheck disable=SC2154
    cp -r "$download_dir"/new_version/* "$destination_dir"

    # Clean up the temporary download directory
    rm -rf "$download_dir"/new_version

    echo "New version successfully downloaded and installed."
fi

# Run the Python app
command pip3 install colorama
command pip3 install requests
command pip3 install bs4
python3 jokeCollectorMain.py

exit 0
