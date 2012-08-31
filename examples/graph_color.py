#!/usr/bin/python

import sys
sys.path.append("..")	#Add parent directoy to Include Paths


from time import sleep
from array import *
from HL1606_RPi_GPIO import HL1606

	
LED = HL1606()

#Convert the strings to integers (for [3] - [5] use base 2 (bianry) for easier color definition)
LED.bargraph(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3] ,2), int(sys.argv[4] ,2), int(sys.argv[5],2)) 