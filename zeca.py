#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
=====================
LNLS - Controls Group
=====================
information:
------------
maintainer: Rafael Ito
e-mail:     rafael.ito@lnls.br
github:     https://gitlab.cnpem.br/con/cons-zabbix
--------------------------------------------------
description:
------------
this piece of code uses the zabbix-epics-py module (see below) to send metrics to a Zabbix server
it reads a csv spreadsheet to create "ZabbixSenderCA" instances and threads associated for each entry in the table
--------------------------------------------------
credits:
--------
module:         zabbix-epics-py
description:    EPICS CA client to send metrics to Zabbix server
github:         https://github.com/sasaki77/zabbix-epics-py
'''

#=================================================
# ZECA - Zabbix EPICS Channel Access
#=================================================

from zbxepics import ZabbixSenderCA
from threading import Thread
import pandas as pd

#import logging
#logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)-15s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# read csv spreadsheet
df = pd.read_csv("spreadsheet.csv")
# create a list for each column
s_host     = df['host']
s_pv       = df['pv']
s_interval = df['interval']
s_item_key = df['item_key']
s_func     = df['func']

# Zabbix IP and port config
server_ip  = '10.0.38.59'    # Zabbix server IP
port       = 10051           # Zabbix trapper port
config     = False

# create list of "ZabbixSenderCA" objects according to csv spreadsheet
items = []
zabbix_instances = []
spreadsheet_size = len(s_host)
for i in range(spreadsheet_size):
    items.append([
        dict(
            host     = s_host[i],
            pv       = s_pv[i],
            interval = s_interval[i],
            item_key = s_item_key[i],
            func     = s_func[i]
            )
        ]
    )
#    print(items[i])
    zabbix_instances.append(ZabbixSenderCA(server_ip, port, config, items[i]))

# thread class for "ZabbixSenderCA"
class zabbix_thread(Thread):
    def __init__(self, zabbix_object):
        Thread.__init__(self)
        self.object = zabbix_object
    def run(self):
        self.object.run()
        print("thread started")

# create and start threads
thread = []
for i in range(spreadsheet_size):
    # for each "ZabbixSenderCA" instance create a thread associated
    thread.append(zabbix_thread(zabbix_instances[i]))
    # start threads
    thread[i].start()
