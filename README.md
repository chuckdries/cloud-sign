![gif of cloud shaped lamp blinking](https://github.com/chuckdries/cloud-sign/raw/main/C0235.gif)

> apologies for the gif, it looks smooth in person but it's surprisingly difficult to cleanly capture video of PWM controlled lights

Designed to power a lamp from a raspberry pi. Turns GPIO17 on if internet works, pulses if internet doesn't

install: symlink or copy cloudsign.service to `/lib/systemd/system`

start: `sudo systemctl start cloudsign`  
stop: `sudo systemctl stop cloudsign`  
etc for enable/disable/restart  

logs: `journalctl -u cloudsign`  
edit startup: `sudo vim /lib/systemd/system/cloudsign.service`