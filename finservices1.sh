#!/bin/bash

source ~/.bash_profile

rm -f /fincor/capp/TZPRD/finmonitor/ConfigService.txt
if [ -f /fincor/capp/TZPRD/ConfigService/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/ConfigService/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/ConfigService.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/ConfigService.txt  ea248080@10.231.116.89:data/finservices/node1
fi 

rm -f /fincor/capp/TZPRD/finmonitor/FINRPT-finlstclnt.txt
 if [ -f /fincor/capp/TZPRD/finlstclnt/FINRPT/services/finrptsrvr/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/finlstclnt/FINRPT/services/finrptsrvr/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/FINRPT-finlstclnt.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/FINRPT-finlstclnt.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/FINRPT-comnclnt.txt
if [ -f /fincor/capp/TZPRD/comnclnt/FINRPT/services/finrptsrvr/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/comnclnt/FINRPT/services/finrptsrvr/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/FINRPT-comnclnt.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/FINRPT-comnclnt.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/CBC.txt
if [ -f /fincor/capp/TZPRD/CBC/services/cbc/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/CBC/services/cbc/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/CBC.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/CBC.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Finlistval.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/finlistval/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/finlistval/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Finlistval.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Finlistval.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Coresession.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/coresession/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/coresession/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Coresession.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Coresession.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Referral.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/referral/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/referral/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Referral.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Referral.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Uniser-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/uniser_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/uniser_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Uniser-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Uniser-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/MQMRtgsIn-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/mqmrtgsin_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/mqmrtgsin_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/MQMRtgsIn-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/MQMRtgsIn-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/MQMRtgsOut-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/mqmrtgsout_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/mqmrtgsout_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/MQMRtgsOut-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/MQMRtgsOut-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/MQMRead-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/mqmread_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/mqmread_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/MQMRead-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/MQMRead-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Dispatcher-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/dispatcher1_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/dispatcher1_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Dispatcher-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Dispatcher-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Binagent-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/binagent_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/binagent_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Binagent-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Binagent-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Swiftsrv-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/swiftsrv_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/swiftsrv_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Swiftsrv-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Swiftsrv-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Pmssrv-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/pmssrv_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/pmssrv_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Pmssrv-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Pmssrv-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Genlimo-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/genlimo_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/genlimo_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Genlimo-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Genlimo-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Aabsrv-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/aabsrv_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/aabsrv_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Aabsrv-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Aabsrv-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Eabgst-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/eabgst_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/eabgst_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Eabgst-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Eabgst-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Trswift-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/trswift_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/trswift_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Trswift-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Trswift-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi

rm -f /fincor/capp/TZPRD/finmonitor/Uplpsmsg-TZ.txt
if [ -f /fincor/capp/TZPRD/Finacle/FC/app/services/uplpsmsg_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZPRD/Finacle/FC/app/services/uplpsmsg_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZPRD/finmonitor/Uplpsmsg-TZ.txt
    scp -o MACs=hmac-sha2-512 /fincor/capp/TZPRD/finmonitor/Uplpsmsg-TZ.txt  ea248080@10.231.116.89:data/finservices/node1
fi
