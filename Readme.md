# Raspberry Pi Organiser

A simple script to run on startup on a raspberry pi.

## Setup

```bash
git clone https://github.com/chrispsheehan/RaspberryPiTasks.git
sudo sh ./RaspberryPiTasks/Install.sh
crontab ./RaspberryPiTasks/cronjobs.txt
```

## Test

Reboot the Pi. You should see the below file.

```bash
./RaspberryPiTasks/src/test.txt
```

## Docker environment

```bash
docker build -t rasp-box .
docker run -it rasp-box
```

### References

- https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
- https://www.youtube.com/watch?v=zRXauWUumSI
