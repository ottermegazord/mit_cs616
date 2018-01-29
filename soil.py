import pycs616
import mux
import RPi.GPIO as GPIO
import time
import signal

class TimeoutException(Exception):
	pass

def timeout_handler(signum, frame):
	raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)

chan_list = [31, 33, 35, 37]
channels = [0,1,2,3]

for i in range (0, len(channels)):
	signal.alarm(5)
	try:
		mux.mux_channel(channels[i], chan_list)
		print(channels[i])
		time.sleep(1)
		print(pycs616.get_freq())
	except TimeoutException:
		print('NaN')
		continue
	else:
		signal.alarm(0)
