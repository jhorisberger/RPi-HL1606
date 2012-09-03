HL1606 Examples
================

**Note:** For these examples to work, you have to connect the pins to your Raspberry Pi as follows:  
  
+ Data (DI)       --> GPIO 10 (Pin 19)  
+ Clock (CI)      --> GPIO 11 (Pin 23)
+ Chipselect (LI) --> GPIO 8 (Pin 24)
+ Fade (SI)       --> GPIO 24 (Pin 18)  **Optional (only used for fading)**

Or change the Pin numbers in HL1606_RPi_GPIO.py on line 10 and following. Also change the number of pixels your stripe has on line 16.

**You need to supply Levelshifting for the signals !!!** The easiest way th achve this is with a quadruple dual-input and gate (74HC08 or similar) 
!(Levelshifter.jpeg)
 
Description 
------------

### graph.py / graph_color.py

Displays a Bargraph according to the values (in %) given to the function. In adition the color of the graph and the background can also be specified.  
**Note:** The Precentage is calculated using the LED_Count variable.  

Example to display 30% and 70% in standard colors:  
`sudo python3 graph.py 30 70`  
  
Example to display 30% and 70% in defined colors: (Greeen and white)
`sudo python3 graph_color.py 30 70 10000001 10101001 00000001`  

  
### colorgraph.py

Displays a Bargraph according to the value (in %) which fades from green to red (colors ajustable) for higher values.
`sudo python3 colorgraph.py 30`

### rainbow.py

Produces a Rainbow effect by gradualy fading through all the avalilable colors. Set the LED_Count variable in HL1606_RPi_GPIO.py according to the actual amount of pixels for best results. 


