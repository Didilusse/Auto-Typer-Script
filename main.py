import pyautogui as pg
import time
import random

# Get user inputs
message = input("Enter the message you want to send: ")
duration = int(input("Enter the duration for the program to run (in seconds): "))
message_count = int(input("How many times should the message be sent: "))

# Give the user time to switch to the window where the message will be sent
print("You have 5 seconds to switch to the target window...")
time.sleep(5)

t_end = time.time() + duration
count = 0

try:
    while time.time() < t_end and count < message_count:
        pg.write(message)
        time.sleep(random.uniform(0.1, 0.5))  # Random delay between 0.1 and 0.5 seconds
        pg.press('Enter')
        print(f'Sent: {message}')
        count += 1
        time.sleep(random.uniform(0.1, 0.3))  # Another random delay
except KeyboardInterrupt:
    print("Process interrupted by user.")

print(f"Program finished. Sent {count} messages.")