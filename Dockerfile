FROM balenalib/raspberry-pi

COPY ./src ./RasberryPiTasks/src

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install cron
RUN apt-get -y install nodejs
RUN apt-get -y install git

CMD ["/bin/bash"]