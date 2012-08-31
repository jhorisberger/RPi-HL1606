#!/usr/bin/python

import sys
from time import sleep
from array import *
from HL1606_RPi_GPIO import HL1606


	
LED = HL1606()

	
LED.colorgraph(int(sys.argv[1]))

sleep(10)



	

	
	

