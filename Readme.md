# Raspberry Pi Organiser
A simple script to run on startup on a raspberry pi.

## Setup
- (Re)Install node and npm
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo bash
sudo apt install nodejs
```
- Install startup script
```
git clone https://github.com/chrispsheehan/RaspberryPiTasks.git
```
- Set cron job
```
crontab -e
```
- Cron job entry
```
@reboot sleep 60 && python /home/pi/RaspberryPiTasks/OnStartup.py
```

## Update
- Update startup script
```
cd RaspberryPiTasks/
git pull
```

### References
- https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
- https://www.youtube.com/watch?v=zRXauWUumSI
