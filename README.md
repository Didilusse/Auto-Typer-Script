# Auto Typer Script

This Python script automatically types a message and sends it repeatedly using the `pyautogui` library. It is configured to run for 10 seconds, sending the message every 0.1 seconds.

## Features
- Automatically types and sends a message.
- Runs for a specified duration (10 seconds).
- Simulates keyboard typing and pressing Enter.

## Requirements

- Python 3.x
- `pyautogui` library

## Installation

1. Clone the repository or download the script file.
    ```bash
    git clone git@github.com:Didilusse/Auto-Typer-Script.git
    ```
2. Install the required dependencies:
    ```bash
    pip install pyautogui
    ```

## Usage

1. Run the Python script:
    ```bash
    python auto_typer.py
    ```
2. Once you start the script, it will wait for 5 seconds before executing to give you time to switch to the target application (e.g., a chat window).
3. The script will type "Get On Skyblock" and press Enter repeatedly for 10 seconds.

## How it works

- After running the script, it waits for 5 seconds (`time.sleep(5)`) so that you can focus on the application where the message will be sent.
- The message is sent repeatedly for 10 seconds, every 0.1 seconds.
- `pyautogui.write(a)` types the message.
- `pyautogui.press('Enter')` simulates pressing the Enter key to send the message.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
