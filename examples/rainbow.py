#!/usr/bin/python


from HL1606_RPi_GPIO import HL1606

	
LED = HL1606()



LED.fade(0b01000001) #zero to green
	
while True:

	LED.fade(0b10010001) #Green to Yellow
	LED.fade(0b11100001) #Yellow to Red
	LED.fade(0b00100101) #Red to Magenta
	LED.fade(0b00111001) #Magenta to Blue
	LED.fade(0b01001001) #Blue to Cyan
	LED.fade(0b10011001) #Cyan to White
	LED.fade(0b10111101) #White to Green
	