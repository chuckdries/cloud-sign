Designed to power a lamp from a raspberry pi. Turns GPIO17 on if internet works, pulses if internet doesn't

install: symlink or copy cloudsign.service to `/lib/systemd/system`

start: `sudo systemctl start cloudsign`  
stop: `sudo systemctl stop cloudsign`  
etc for enable/disable/restart  

logs: `journalctl -u cloudsign`  
edit startup: `sudo vim /lib/systemd/system/cloudsign.service`