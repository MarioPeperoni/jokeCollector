@echo off

rem Change directory to the directory where the script is located
cd /d %~dp0

rem Check the operating system
if "%OS%"=="Windows_NT" (
    echo Detected Windows
    set "python=python"
    set "pip=pip"
) else (
    echo Assuming non-Windows environment
    set "python=python"
    set "pip=pip"
)

rem Check if Python is installed
where %python% >nul 2>nul
if %errorlevel% equ 0 (
    echo %python% is already installed
    %pip% install colorama
    %pip% install requests
    %pip% install bs4
    rem Run the Python app
    %python% jokeCollectorMain.py
) else (
    rem Prompt the user to install Python
    echo %python% is not installed. Please install %python% before running this app.
)
