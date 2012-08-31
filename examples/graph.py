#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
from time import sleep
from array import *
from HL1606_RPi_GPIO import HL1606

LED_Count = 32

	
LED = HL1606()
test = array('i',[])

#Convert the strings to integers 
LED.bargraph(int(sys.argv[1]), int(sys.argv[2]))

