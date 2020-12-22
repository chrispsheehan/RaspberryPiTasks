# Raspberry Pi Organiser
A simple script to run on startup on a raspberry pi.

## Setup
```
git clone https://github.com/chrispsheehan/RaspberryPiTasks.git
sudo sh ./RaspberryPiTasks/OnReboot.sh
```

## Test
Reboot the Pi. You should see the below file.
```
./RaspberryPiTasks/src/test.txt
```

## Docker environment
```
docker build -t rasp-box .
docker run -it rasp-box
```

### References
- https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
- https://www.youtube.com/watch?v=zRXauWUumSI
