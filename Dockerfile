FROM balenalib/raspberry-pi

COPY ./src ./RasberryPiTasks/src

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install cron
RUN apt-get -y install nodejs
RUN apt-get -y install git
RUN apt-get update

RUN crontab /RasberryPiTasks/src/cronjobs.txt
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install crontab

CMD ["/bin/bash"]