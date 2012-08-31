RPi-HL1606
==========

A controlling script for HL1606 type LED stripes with the Raspberry Pi 

**Relies on the RPi-GPIO library!**


There are multiple functions in this class:

send_bit:
---------
Send one byte of data to the strip. (Moves the existing pixels "down")  
Acepts one byte of Data according to the Data Format table below.


send:
----
Send multiple bytes of data to the strip.   
Acepts only array of integers!

clear:
-------
Clears the whole strip according to the given amount of LED's  
Accepts one Integer containing the amount of pixels to be cleared.

fade:
-----
Slowly fades the whole stripe to a new color.
Accepts one byte of Data containing the color fade according to the Data Format table below.  
**Note:** For this to work, the SI line must be connected!



Data Format: 
============
Each LED is controlled by one byte of data, defined as follows:  

* D0,D1 LED 1 control (Green)
* D2,D3 LED 2 control (Blue)
* D4,D5 LED 3 control (Red)
* D6 	Fade rate bit, 0 = slow (127 steps), 1 = fast (63 steps)
* D7 	Buffer latch bit, 1 = latch, 0 = don't latch (Default 1!)  
--> When set to 0 the value in the shift register will not be transferred to the outputs on rise of the CS signal
					
**Note:** The colors may be in different orders depending on your manufacturer

Each color uses two bits to specify its setting:
				
D0    |    D1    |    Description  
------|----------|---------------------  
0     |    0     |    LED off  
0     |    1     |    LED off, fade up on fade clock  
1     |    0     |    LED on, no fade  
1     |    1     |    LED on, fade down on fade clock  


				
The fading has to be done manually using the SI pin on the strip or with the fade function.
