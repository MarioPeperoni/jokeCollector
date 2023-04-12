@echo off

rem Change directory to the directory where the script is located
cd %~dp0\App

rem Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    rem Prompt the user to install Python
    echo Python is not installed. Please install Python before running this app.
    exit /b 1
)

rem Check if git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Git is not installed. The app will be run without checking for updates.
    rem Run the Python app
    call pip install colorama
    call pip install requests
    call pip install bs4
    python jokeCollectorMain.py
    exit /b 0
)

rem Set the repository URL and the local download directory
set "repo_url=https://github.com/MarioPeperoni/jokeCollector"
for %%I in ("%~dp0..\") do set "download_dir=%%~fI"

rem Get the latest commit hash from the repository
for /f "tokens=1" %%c in ('git ls-remote %repo_url% HEAD ^| cut -f 1') do set "latest_commit=%%c"

rem Check if the latest commit hash matches the current commit hash
if exist "%download_dir%\latest_commit.txt" (
    set /p current_commit=<"%download_dir%\latest_commit.txt"
    if "%current_commit%" EQU "%latest_commit%" (
        echo No new version is available.
        rem Run the Python app
        call pip install colorama
        call pip install requests
        call pip install bs4
        python jokeCollectorMain.py
        exit /b 0
    )
)

rem Prompt the user to download the new version
set /p "answer=Do you want to download and install the new version? (y/n) "
if /i "%answer%" EQU "y" (
    rem Download the latest version from the repository
    echo Downloading new version...
    git clone %repo_url% "%download_dir%\new_version"
    echo %latest_commit% > "%download_dir%\latest_commit.txt"

    rem Copy the new version files to the destination directory
    xcopy /s /e "%download_dir%\new_version\*" "%download_dir%\"

    rem Clean up the temporary download directory
    rmdir /s /q "%download_dir%\new_version"

    echo New version successfully downloaded and installed.
)

rem Run the Python app
call pip install colorama
call pip install requests
call pip install bs4
python jokeCollectorMain.py

exit /b 0
