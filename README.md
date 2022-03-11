# Automated-Braking-System
This project was developed to exhibit braking mechanism and its effects on car's physica pareameters like speed and depemnding on the length of obstacle from the car

## Components used
1x Arduino nano, 1x LED, 1x Potentiometer, 1x HC-SR04 Ultrasonic Sensor, Connecting Wires

## Working Principle
The system works by initially taking object distance from the Ultrasonic sensor. The speed parameter is taken from the potentiometer.All these values are taken as input by arduino and then processed as shown below.

The speed is put intpo the following equation:
<p align=center>ds = k x speed</p>

```
Where,
    ds = Safe braking distance according to the speed value
    k = constant (0.071565)
    speed = input from potentiometer at pin A0
```

 This gives the safe braking distance according to the speed of the car. It is dynamically set
 
## Project Outcomes
From this project, following concepts were sharpened
1) PYQT5 for GUI
2) C++ for Arduino
3) Establishing Serial communication between Arduino and Python
