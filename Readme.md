# Raspberry Pi Organiser
A simple script to run on startup on a raspberry pi.

## Setup
```
sudo sh ./Init.sh
sudo python ./RaspberryPiTasks/src/EntryPoint.py '-init'
```

## Update
```
cd RaspberryPiTasks/
git pull
```

## Docker environment
```
docker build -t rasp-box .
docker run -it rasp-box
```

### References
- https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
- https://www.youtube.com/watch?v=zRXauWUumSI
