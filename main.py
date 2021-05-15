#!/usr/bin/env python3

from gpiozero import LED, PWMLED
from time import sleep
import requests
from datetime import datetime
# import blinkt


# blinkt.set_clear_on_exit()


# led = LED(17)
led = PWMLED(17)

url = "https://chuckdries.com"
sleepTime = 60

while True:
	print(datetime.now())
	try:
		r = requests.get(url)
	except requests.exceptions.ConnectionError as e:
		sleepTime = 20
		# blinkt.set_all(255, 0, 0)
		# led.blink()
		led.pulse(2, 2)
		print(e)
	except requests.exceptions.Timeout as e:
		sleepTime = 20
		# blinkt.set_all(255, 0, 0)
		# led.blink()
		led.pulse(2, 2)
		print(e)
	else:
		sleepTime = 60
		# blinkt.set_all(0, 255, 0)
		# led.value = 1
		led.on()
		print("request succeeded")
	# blinkt.show()
	# sleep(2)
	# blinkt.clear()
	# blinkt.show()
	sleep(sleepTime)
# led.on()
# sleep(1)
# led.off()
# sleep(1)
