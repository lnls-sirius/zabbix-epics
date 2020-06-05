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
# v0.2.3: cloned wait-for-it repository
# v0.3.0: installation with pip (requirements.txt) instead of manually

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
## clone zabbix-epics-py and install it 
#WORKDIR /opt
#RUN git clone https://github.com/sasaki77/zabbix-epics-py
#WORKDIR zabbix-epics-py
#RUN pip3 install -e .
#------------------------------------------------
# clone wait-for-it repository 
WORKDIR /opt
RUN git clone https://github.com/vishnubob/wait-for-it

#================================================
# Ports & Environment Variables
#================================================
#EXPOSE 10050    # Zabbix agent
#EXPOSE 10051    # Zabbix trapper
#ENV EPICS_CA_ADDR_LIST="$EPICS_CA_ADDR_LIST localhost"
ENV EPICS_CA_ADDR_LIST="10.128.1.11:5064 10.128.1.11:5066 10.128.1.11:5068 10.128.1.11:5070 10.128.1.12:5064 10.128.1.12:5070 10.128.1.13:5064 10.128.1.13:5068 10.128.1.13:5070 10.128.1.14:5064 10.128.1.14:5068 10.128.1.14:5070 10.128.1.15:5064 10.128.1.15:5068 10.128.1.15:5070 10.128.1.18:5064 10.128.1.18:5068 10.128.1.18:5070 10.128.1.19:5064 10.128.1.19:5068 10.128.1.19:5070 10.128.1.20:5064 10.128.1.20:5066 10.128.1.20:5068 10.128.1.20:5070 10.128.1.20:5072 10.128.1.20:5074 10.128.1.20:5076 10.128.1.20:5078 10.128.1.20:5080 10.128.1.20:5082 10.128.1.20:5084 10.128.1.20:5086 10.128.1.20:5088 10.128.1.20:5090 10.128.1.20:5092 10.128.1.20:5094 10.128.1.20:5096 10.128.1.20:5098 10.128.1.20:5100 10.128.1.20:5102 10.128.1.20:5104 10.128.1.20:5106 10.128.1.20:5108 10.128.1.20:5110 10.128.1.20:5112 10.128.1.20:5114 10.128.1.20:5116 10.128.1.20:5118 10.128.1.20:5120 10.128.1.20:5122 10.128.1.20:5124 10.128.1.20:5126 10.128.1.20:5128 10.128.1.20:5130 10.128.1.20:5132 10.128.1.20:5134 10.128.1.20:5136 10.128.1.20:5138 10.128.1.20:5140 10.128.1.20:5142 10.128.1.20:5144 10.128.1.20:5146 10.128.1.20:5148 10.128.1.20:5150 10.128.1.20:5152 10.128.1.20:5154 10.128.1.20:5156 10.128.1.20:5158 10.128.1.20:5160 10.128.1.20:5162 10.128.1.50:5064 10.128.1.50:5067 10.128.1.50:5069 10.128.1.50:5071 10.128.1.51:5064 10.128.1.51:5067 10.128.1.51:5069 10.128.1.51:5071 10.128.1.54:5064 10.128.1.55:5064 10.0.4.66:60000 10.128.255.255 localhost"

#================================================
# start the container
#================================================
WORKDIR /opt/zabbix-epics/
COPY spreadsheet.csv ./
COPY zeca.py ./
CMD python3 zeca.py
