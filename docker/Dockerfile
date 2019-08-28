# use an unofficial image with EPICS base (Debian 9) as a parent image
FROM itorafael/epics-base:r3.15.6
LABEL maintainer="Rafael Ito <rafael.ito@lnls.br>"
USER root

#================================================
# docker image versioning control
#================================================
# image itorafael/zabbix-epics
# v0.1: first release
# v0.2: mount volume instead of copying files (docker swarm)
# v0.2: mount volume instead of copying files (docker swarm)
# v0.2.1: updated service name in docker-stack.yml
# v0.2.2: fixed volume path and uncommented COPY commands in Dockerfile

#================================================
# install prerequisites
#================================================
# set correct timezone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#------------------------------------------------
RUN apt-get update && apt-get install -y \
    swig \
    git \
    python3 \
    python3-pip
#------------------------------------------------
WORKDIR /opt
COPY docker/requirements.txt /opt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt
#------------------------------------------------
# clone zabbix-epics-py and install it 
WORKDIR /opt
RUN git clone https://github.com/sasaki77/zabbix-epics-py
WORKDIR zabbix-epics-py
RUN pip3 install -e .

#================================================
# Ports & Environment Variables
#================================================
#EXPOSE 10050    # Zabbix agent
#EXPOSE 10051    # Zabbix trapper
ENV EPICS_CA_ADDR_LIST="$EPICS_CA_ADDR_LIST localhost"

#================================================
# start the container
#================================================
WORKDIR /opt/zabbix-epics/
COPY spreadsheet.csv ./
COPY zeca.py ./
CMD python3 zeca.py
