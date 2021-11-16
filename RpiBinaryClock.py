#!/usr/bin/env python

import RPi.GPIO as GPIO  
import time

#set GPIO pin configuration
GPIO.setmode(GPIO.BCM) 

#List all pins in use for project
clock_pins=[13,12,6,5,17,21,20,16,25,24,23]



def hours():
	"""method calculates which pins to set high for Hours display"""
	
	pins_hours = []

	
	t = time.strftime("%H")
	t = float(t)
	t = int(float(t))

	

	for x in xrange(0,5):
		if t >= 16:
			pins_hours.append(13) #pin13 set to 16 hour
			t = t-16
		elif t >= 8:
			pins_hours.append(12) #pin12 set to 8 hour			
			t = t-8
		elif t >= 4:
			pins_hours.append(6)	#pin6 set to 4 hour
			t = t-4
		elif t >= 2:
			pins_hours.append(5)	#pin5 set to 2 hour
			t = t-2
		elif t == 1:
			pins_hours.append(17)	#pin17 set to 1 hour
			t = t-1
		else:

			#print(pins_hours)		

			return pins_hours




def minutes():
	"""method calculates which pins to set high for Minutes display"""

	pins_minutes = []

	
	t = time.strftime("%M")
	t = float(t)
	t = int(float(t))

	

	for x in xrange(0,6):
		if t >= 32:
			pins_minutes.append(21) #pin21 set to 32 min
			t = t-32
		elif t >= 16:
			pins_minutes.append(20) #pin20 set to 16 min
			t = t-16
		elif t >= 8:
			pins_minutes.append(16)	#pin16 set to 8 min		
			t = t-8
		elif t >= 4:
			pins_minutes.append(25) #pin25 set to 4 min
			t = t-4
		elif t >= 2:
			pins_minutes.append(24) #pin24 set to 2 min
			t = t-2
		elif t == 1:
			pins_minutes.append(23) #pin23 set to 1 min
			t = t-1
		else:

			#print(pins_minutes)		

			return pins_minutes





def clean_pins():
	"""Method used to ensure desired pins are set as outputs and are set to Low (off)"""
	
	# ensures pins are off following from previous run
	for i in clock_pins:
		GPIO.setup(i, GPIO.OUT, initial=0) # sets i to output and 0V, off





def output_clock():
	"""method gets data from def hours() and def minutes() to populate list of pins to be displayed """
	

	hr = hours()
	mn = minutes()
	

	if hr is None:
		pins_all = [mn]
		print ("Hours malfunction")
		print (time.strftime("%H : %M")) # Print time in terminal - only needed for testing


	elif mn is None:	
		pins_all = [hr]
		print ("Minutes malfunction")
		print (time.strftime("%H : %M")) # Print time in terminal - only needed for testing


	else:
		pins_all = [hr + mn]	



	clean_pins() # ensure pins are off before attempting to switch high


	# turns pin	on for this run
	for i in pins_all:
		GPIO.output(i, 1)    # sets port on

	# clears pins_all list	
	del pins_all[:]







#######################################
# Run the clock program
# Attempt update every 1 seconds
#######################################


clean_pins()	# ensure pins are off at start


print "\nWelcome to Rpi Binary Clock \nTo Exit program press CTRL and C \n"

try:
	while True:
		#print (time.strftime("%H : %M")) # Print time in terminal - only needed for testing
		output_clock()
		time.sleep(1)
		

  
except KeyboardInterrupt:     
    # exits when you press CTRL+C  
    print "\n User Exited Program"		


except:
	print "\nBig error \nNo clue mate"


finally:
	GPIO.cleanup() # clean up the ports on exit, no matter why it exits 