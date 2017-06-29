#!/usr/bin/python

# DS18B20 classes for use with Raspberry Pi GPIO 



import os
import glob
import time



#################################################
#	class thermometer_generic() will allow user	#
#	to set up new or unknown DS18B20 sensors	#
#	quickly										#
#################################################

class thermometer_generic(object):


	def __init__():
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')

		base_dir = '/sys/bus/w1/devices/'
		device_folder = glob.glob(base_dir + '28*')[0]
		device_file = device_folder + '/w1_slave'



	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:]!='YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos !=-1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000.0
			return temp






#################################################
#	class thermometer#() will allow use of		#
#	known DS18B20 sensors						#
#################################################

class thermometer1(object):


	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28-0000068adbbb')[0]
	device_file = device_folder + '/w1_slave'



	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:]!='YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos !=-1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000.0
			temp = round(temp,1)
			return temp





class thermometer2(object):


	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28-0000068a506f')[0]
	device_file = device_folder + '/w1_slave'



	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:]!='YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos !=-1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000.0
			temp = temp+0.85	#correction for inaccuracy
			temp = round(temp,1)
			return temp			





class thermometer3(object):


	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28-0000068b0608')[0]
	device_file = device_folder + '/w1_slave'



	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:]!='YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos !=-1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000.0
			temp = round(temp,1)
			return temp





class thermometer4(object):


	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28-0000068a75e6')[0]
	device_file = device_folder + '/w1_slave'



	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:]!='YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos !=-1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000.0
			temp = round(temp,1)
			return temp





class thermometer5(object):


	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

	base_dir = '/sys/bus/w1/devices/'
	device_folder = glob.glob(base_dir + '28-0000068af0ba')[0]
	device_file = device_folder + '/w1_slave'



	def read_temp_raw(self):
		f = open(self.device_file,'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:]!='YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos !=-1:
			temp_string = lines[1][equals_pos+2:]
			temp = float(temp_string)/1000.0
			temp = temp-0.06	#correction for inaccuracy
			temp = round(temp,1)
			return temp			