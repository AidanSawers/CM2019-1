#!/usr/bin/python

from microbit import *
import radio
import neopixel

r = 0
g = 0
b = 0
np = neopixel.NeoPixel(pin13, 12)
for i in range(0,12):
    np[i] = (r,g,b)
np.show()

radio.on()
radio.config(channel=33)
radio.config(power=7)

leftSpeed = pin0
leftDirection = pin8
rightSpeed = pin1
rightDirection = pin12


# Motor control to tell the motor which direction and speed to move

def move(
    _leftSpeed,
    _rightSpeed,
    _leftDirection,
    _rightDirection,
    ):

    # speed values between 1 and 1023
    # smaller values ==faster speed moving backwards
    # smaller values == lower speeds when moving forawrds
    # directions 0 == forwards , 1 == backwards

    leftSpeed.write_analog(_leftSpeed)  # Set the speed of left motor
    rightSpeed.write_analog(_rightSpeed)  # set speed of rightt motor
    if _leftDirection != 2:
        leftDirection.write_digital(_leftDirection)
        rightDirection.write_digital(_rightDirection)


def drive(speed):
    if speed > 0:
        move(speed, speed, 0, 0)  # move motors forwards
    else:
        speed = 1023 + speed
        move(speed, speed, 1, 1)


def sharpRight():
    move(100, 1023 + 200, 0, 1)


def sharpLeft():
    move(1023 + 200, 100, 1, 0)


def gentleRight():
    move(200, 0, 0, 0)


def gentleLeft():
    move(0, 200, 0, 0)


def coast():
    move(0, 0, 2, 2)


def stop():
    move(0, 0, 0, 0)
    
    


    
while True:
    incoming = radio.receive()
    if incoming is not None:
        if incoming == "F":
            drive(1023)
            display.show(Image.ARROW_N, loop=False, delay=10)
        elif incoming == "L":
            gentleLeft()
            display.show(Image.ARROW_W, loop=False, delay=10)
        elif incoming == "R":
            gentleRight()
            display.show(Image.ARROW_E, loop=False, delay=10)
        else:
            stop()
            display.show(Image.FABULOUS, loop=False, delay=10)
