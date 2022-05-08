import pyperclip
import pyttsx3 
import time




def SayThis(word):
    engine = pyttsx3.init()
    engine.say(word)

    engine.runAndWait()

 


class Bot:
    def __init__(self, speech_speed = 1, volume =1):
        self.volume = volume
        self.cache = "initialized clipboard bot"
        self.sleep_time = 2
        self.speech_speed = speech_speed
        self.running = True
        SayThis('clipboard speech bot initiated , copy something')
    def Run(self):
        while self.running:
            clipboard = pyperclip.paste()
            if clipboard != self.cache:
                # new text copied
                # sya it
                self.cache = clipboard
                print(f'saying {clipboard}')
                SayThis(self.cache)

            time.sleep(self.sleep_time)


if __name__ == '__main__':
    Bot().Run()



