git clone https://github.com/chrispsheehan/RaspberryPiTasks.git
curl -sL https://nodejs.org/dist/v8.11.3/node-v8.11.3-linux-armv6l.tar.xz | bash
apt install nodejs
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
cd RaspberryPiTasks
git pull
cd ..
python ./RaspberryPiTasks/src/EntryPoint.py '-init'