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
- Set cron job(s)
```
crontab /RasberryPiTasks/src/cronjobs.txt
```
- Install pip crontab
```
pip install crontab
```

## Update
- Update startup script
```
cd RaspberryPiTasks/
git pull
```

## Docker environment
- Creates a local environment to poke around in
```
docker build -t rasp-box .
docker run -it rasp-box
```

### References
- https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
- https://www.youtube.com/watch?v=zRXauWUumSI
