FROM balenalib/raspberry-pi

COPY / /RaspberryPiTasks

RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install python
RUN apt-get -y install git
RUN apt-get update

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

CMD ["/bin/bash"]