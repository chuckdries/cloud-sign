#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
import requests
import blinkt


blinkt.set_clear_on_exit()


# led = LED(17)

while True:
	print("hello")
	try:
		r = requests.get("https://chuckdries.com")
	except requests.exceptions.ConnectionError as e:
		blinkt.set_all(255, 0, 0)
		# led.on()
		print(e)
	except requests.exceptions.Timeout as e:
		# led.off()
		blinkt.set_all(255, 0, 0)
		print(e)
	else:
		# led.off()
		blinkt.set_all(0, 255, 0)
		print("request succeeded")
	blinkt.show()
	sleep(2)
	blinkt.clear()
	blinkt.show()
	sleep(10)
# led.on()
# sleep(1)
# led.off()
# sleep(1)
