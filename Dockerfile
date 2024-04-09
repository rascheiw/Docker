FROM ubuntu:18.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD content.py /my_server/content.py
WORKDIR /my_server/
EXPOSE 6000
CMD python3 content.py 
