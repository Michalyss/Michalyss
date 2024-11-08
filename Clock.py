
import time


def real_time_clock():
    second = 0
    minute = 0
    hour = 0

    while hour < 24:
        while minute < 60:
            while second < 60:
                print(f"\r{hour:02}:{minute:02}:{second:02}", end="")
                time.sleep(1)  # Sleep for 1 second
                second += 1
            minute += 1
            second = 0
        hour += 1
        minute = 0

    print()  # Ensure the prompt moves to the next line after completing the loop



