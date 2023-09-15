#!/bin/bash

source ~/.bash_profile

rm -f /fincor/capp/TZUAT/finmonitor/ConfigService.txt
if [ -f /fincor/capp/TZUAT/ConfigService/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/ConfigService/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/ConfigService.txt
    scp /fincor/capp/TZUAT/finmonitor/ConfigService.txt  ea248080@10.231.116.89:data/finservices/node2
fi 

rm -f /fincor/capp/TZUAT/finmonitor/FINRPT-finlstclnt.txt
 if [ -f /fincor/capp/TZUAT/finlstclnt/FINRPT/services/finrptsrvr/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/finlstclnt/FINRPT/services/finrptsrvr/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/FINRPT-finlstclnt.txt
    scp /fincor/capp/TZUAT/finmonitor/FINRPT-finlstclnt.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/FINRPT-comnclnt.txt
if [ -f /fincor/capp/TZUAT/comnclnt/FINRPT/services/finrptsrvr/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/comnclnt/FINRPT/services/finrptsrvr/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/FINRPT-comnclnt.txt
    scp /fincor/capp/TZUAT/finmonitor/FINRPT-comnclnt.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/CBC.txt
if [ -f /fincor/capp/TZUAT/CBC/services/cbc/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/CBC/services/cbc/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/CBC.txt
    scp /fincor/capp/TZUAT/finmonitor/CBC.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Finlistval.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/finlistval/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/finlistval/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Finlistval.txt
    scp /fincor/capp/TZUAT/finmonitor/Finlistval.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Coresession.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/coresession/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/coresession/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Coresession.txt
    scp /fincor/capp/TZUAT/finmonitor/Coresession.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Referral.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/referral/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/referral/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Referral.txt
    scp /fincor/capp/TZUAT/finmonitor/Referral.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Uniser-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/uniser_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/uniser_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Uniser-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Uniser-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/MQMRtgsIn-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/mqmrtgsin_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/mqmrtgsin_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/MQMRtgsIn-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/MQMRtgsIn-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/MQMRtgsOut-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/mqmrtgsout_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/mqmrtgsout_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/MQMRtgsOut-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/MQMRtgsOut-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/MQMRead-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/mqmread_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/mqmread_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/MQMRead-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/MQMRead-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Dispatcher-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/dispatcher1_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/dispatcher1_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Dispatcher-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Dispatcher-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Binagent-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/binagent_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/binagent_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Binagent-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Binagent-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Swiftsrv-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/swiftsrv_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/swiftsrv_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Swiftsrv-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Swiftsrv-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Pmssrv-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/pmssrv_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/pmssrv_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Pmssrv-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Pmssrv-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Genlimo-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/genlimo_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/genlimo_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Genlimo-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Genlimo-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Aabsrv-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/aabsrv_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/aabsrv_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Aabsrv-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Aabsrv-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Eabgst-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/eabgst_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/eabgst_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Eabgst-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Eabgst-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Trswift-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/trswift_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/trswift_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Trswift-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Trswift-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi

rm -f /fincor/capp/TZUAT/finmonitor/Uplpsmsg-TZ.txt
if [ -f /fincor/capp/TZUAT/Finacle/FC/app/services/uplpsmsg_TZ/bin/*.pid ]; then
    cd /fincor/capp/TZUAT/Finacle/FC/app/services/uplpsmsg_TZ/bin
    ps -ef | grep `cat *pid` | grep -v grep  > /fincor/capp/TZUAT/finmonitor/Uplpsmsg-TZ.txt
    scp /fincor/capp/TZUAT/finmonitor/Uplpsmsg-TZ.txt  ea248080@10.231.116.89:data/finservices/node2
fi
