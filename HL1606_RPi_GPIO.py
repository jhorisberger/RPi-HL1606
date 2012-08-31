#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from array import *

# Variables
#----------

Data = 10		#Pins connected to the Strip
Clock = 11
CS = 8
Dim = 24

speed = 0.006	#Dimming speed (time delay between fades)
LED_Count = 32   #Number of LED's on the Strip
			

class HL1606:
	def __init__(self):
	
	#Initialize Pins	
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(Data, GPIO.OUT)
		GPIO.setup(Clock, GPIO.OUT)
		GPIO.setup(CS, GPIO.OUT)
		GPIO.setup(Dim, GPIO.OUT)
		GPIO.output(CS, True)
	
	# Clear Screen
		self.clear(LED_Count)

	
	# Send one byte of data to the strip. (moves the existing pixels "down")
	def send_bit(self, data):
		bits=bin(data)[2:].zfill(8)
	
		GPIO.output(CS, False)
	
		for i in range(8):
			if bits[7-i] == "1":
				GPIO.output(Data, True)
			else:
				GPIO.output(Data, False)
				
			GPIO.output(Clock, True)
			GPIO.output(Clock, False)

		GPIO.output(CS, True)	
	
	# Send multiple bytes of data to the strip. Acepts only array of integers!
	def send(self, data):

		GPIO.output(CS, False)
	
		for byte in data:
	
			bits = bin(byte)[2:].zfill(8)			#convert byte to array of bits
		
		
			for i in range(8):						#transmit each bit MSB first!
				if bits[7-i] == "1":
					GPIO.output(Data, True)
				else:
					GPIO.output(Data, False)
				
				GPIO.output(Clock, True)
				GPIO.output(Clock, False)
		
		GPIO.output(CS, True)

	
	# Clears the whole strip according to the given amount of LED's
	def clear(self, bits):
		bytes = array('i',[])
		for i in range(bits):
			bytes.append(0x00000001)
		
		self.send(bytes)
		
	#Fade to a new color
	def fade(self, color):

		for j in range(LED_Count): 
		
			bytes = array('i',[])
		
			for i in range(LED_Count):				#move out old data
				bytes.append(0b00000000)
		
			bytes.append(color)						#Set new color fade
		
			for i in range(j):						#move in right amount of times
				bytes.append(0b00000000)
		
			self.send(bytes)
			
			for i in range(int(128/LED_Count)):		# Fade some befor going to the next LED
				GPIO.output(Dim, True)
				sleep(0.001)
				GPIO.output(Dim, False)
				sleep(speed)
	
	# Displays a bargraph acording to the given value(s) in % Colors can also be defined
	def bargraph(self, value1, value2=0, color1=0b10001001, color2=0b00100001, background=0b0000001):
	
		value1 = int((value1/100)*LED_Count)		#Adjust the values according to the No. of LED's on the strip
		value2 = int((value2/100)*LED_Count)
		
		bytes = array('i',[])
		
		for i in range(LED_Count):	
			if (value1 >= value2) :
				if (LED_Count-i) <= value2:
					bytes.append(color2)
				elif (LED_Count-i) > value2 and (LED_Count-i) <= value1:
					bytes.append(color1)
				else:
					bytes.append(background)
					
			if value2 > value1:
				if (LED_Count-i) <= value1:
					bytes.append(color1)
				elif (LED_Count-i) > value1 and (LED_Count-i) <= value2:
					bytes.append(color2)
				else:
					bytes.append(background)
					
		self.send(bytes)		
		
	def colorgraph(self, value, color=0b01110001, offset=8, offsetcolor=0b10000001):

		value = int((value/100)*LED_Count)		#Adjust the value according to the No. of LED's on the strip
		for j in range(LED_Count): 
		
			bytes = array('i',[])
		
			for i in range(LED_Count):				#move out old data
				bytes.append(0b00000000)
				
			
			if j <= value :				#Set color or blank
				if j < offset:
					bytes.append(offsetcolor)		
				else:
					bytes.append(color)
					
			else: 
				bytes.append(0b00000001)	
		
		
			for i in range(j):						#move in right amount of times
				bytes.append(0b00000000)
		
			self.send(bytes)
			
			for i in range(int(128/(LED_Count-offset))):		# Fade some befor going to the next LED
				GPIO.output(Dim, True)
				sleep(0.0005)
				GPIO.output(Dim, False)
				sleep(0.0005)
				


if __name__ == '__main__':
	
	LED = HL1606()
	test = array('i',[])
			
	for i in range(10):	
		test.append(0b10101001)
		
	LED.send(test)
		
	

	
	

