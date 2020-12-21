FROM balenalib/raspberry-pi

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install git
RUN apt-get update

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN git clone https://github.com/chrispsheehan/RaspberryPiTasks.git

CMD ["/bin/bash"]