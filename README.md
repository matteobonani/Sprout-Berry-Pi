# Sprout-Berry Pi

## 1. About

A simple watering plant system



## 2. Authors

This project was created by:

* Matteo Bonani - 20011  
* Simon Plancher - 20229
* Vinicius Triches - 20428

## 3. Usage

First thing you must connect the RPI to internet.
Secondly, you must connect the bluetooth speaker to your RPI.
Ensure that the output device is set to the bluetooth device.
To check it, type on the terminal ```pavucontrol```, if is not present, download it typing ```sudo apt-get install pavucontrol```

## 4. Implementation

We used multithreading to keep track of the different tasks of our project. One thread is for measuring the humidity and eventually watering the plant, and the second thread keeps track of the buttons pressed.
We used the explorerhat library to exploit the variety of functions, given by the explorerhat. To make the requests, we made use of the requests module. To convert the messages into audio outputs, we used the google text to speech (gtts) library. We saved the results into mp3 files and ran them using the mpg321 command line music player using the os library. 

## 5. Project Requirements

The input devices are:
1.  moisture sensor: it takes the soil humidity from where the plant is planted
2.  touchpad button 1 on the explorer hat: It retrives ,using the openweathermap api, the current temperature of Bolzano.
3.  touchpad button 3 decrements the running time of the pump.
4.  touchpad button 4 increments the running time of the pump.

The output devices are:
1.  water pump: it pump the water into the soil 
2.  speaker: is used for speak out loud the current temperature of Bolzano or the running time of the pump, according to the button pressed.





