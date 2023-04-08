#!/bin/bash

# Check the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    python=python3
    pip=pip3
else
    echo "Assuming non-macOS environment"
    python=python
    pip=pip
fi

# Check if Python is installed
if command -v $python &>/dev/null; then
    echo "$python is already installed"
    command $pip install colorama
    command $pip install requests
    command $pip install bs4
    # Run the Python app
    $python jokeCollectorMain.py
else
    # Prompt the user to install Python
    echo "$python is not installed. Please install $python before running this app."
fi
