import threading
import explorerhat
from time import sleep
import requests
from gtts import gTTS
import os

lat_unibz = 46.4982953
lon_unibz = 11.3547582
pump_time = 3
lock = threading.Lock()

api_key = "b6686cd5b2cdca1b35573a1fe1cc6104"
url = "https://api.openweathermap.org/data/2.5/onecall"
ow_dict = { 'lat': lat_unibz, 'lon': lon_unibz, 'appid': api_key, 'units': 'metric' }




def check_humidity():
    moisture_sensor = explorerhat.analog.one
    while True:
        hum = moisture_sensor.read()
        sleep(1)
        if hum > 1:
            run_pump()
            print("Pump has run")
            sleep(300) #wait for 5 minutes if the pump ran


def run_pump():
    relay = explorerhat.output.one
    relay.toggle()
    sleep(pump_time)
    relay.toggle()

def pressButton():
    
    button1 = explorerhat.touch.one
    button3 = explorerhat.touch.three
    button4 = explorerhat.touch.four

    while True:
        if button1.is_pressed():
            print("Button 1 is pressed")
            #shows outside temperature from weather api of bolzano
            response = requests.get(url,params=ow_dict)
            data = response.json()
            current_temp = data['current']['temp']
            # specify the message
            message = "The temperature outside in Bolzano is : " + str(current_temp) + "degrees"
            # create the gTTS object and save the speech to an mp3 file
            tts = gTTS(text=message, lang = 'en')
            tts.save("message.mp3")
            #play the mp3 file
            os.system("mpg321 message.mp3") 
        if button3.is_pressed():
            print("Button 3 is pressed")
            # specify the message
            decrement_pump_time()
            message = "The pump will be active for : " + str(pump_time) + "second"
            # create the gTTS object and save the speech to an mp3 file
            tts = gTTS(text=message, lang = 'en')
            tts.save("pump_time.mp3") 
            os.system("mpg321 pump_time.mp3")   
        if button4.is_pressed():
            print("Button 4 is pressed")
            increment_pump_time()
            # specify the message
            message = "The pump will be active for : " + str(pump_time) + "second"
            # create the gTTS object and save the speech to an mp3 file
            tts = gTTS(text=message, lang = 'en')
            tts.save("pump_time.mp3")
            os.system("mpg321 pump_time.mp3")      
        sleep(1)

def increment_pump_time():
    global pump_time
    with lock:
        pump_time += 1

def decrement_pump_time():
    global pump_time
    with lock:
        if pump_time > 1:
            pump_time -= 1       

# Create the first thread
first_thread = threading.Thread(target=check_humidity)

# Create the second thread
second_thread = threading.Thread(target=pressButton)

# Start the first thread
first_thread.start()

# Start the second thread
second_thread.start()

# Join the threads so the program will wait for them to finish
first_thread.join()
second_thread.join()

