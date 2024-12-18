import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "sound.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if alarm_time == current_time:
            print("WAKE UP")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the 24 hour alarm time in the following format...(HH:MM:SS)")
    set_alarm(alarm_time)
    
