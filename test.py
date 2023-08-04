from glob import iglob
from os import path

fins = ['Aabsrv-TZ', 'Binagent-TZ', 'CBC', 'ConfigService', 'Coresession', 'Dispatcher-TZ', 'Finlistval', 'FINRPT-comnclnt', 'FINRPT-finlstclnt', 'Genlimo-TZ', 'MQMRead-TZ', 'MQMRtgsOut-TZ', 'Pmssrv-TZ', 'Referral', 'Swiftsrv-TZ', 'Trswift-TZ', 'Uniser-TZ', 'Uplpsmsg-TZ']
standard_fins = ['ConfigService', 'FINRPT-finlstclnt', 'FINRPT-comnclnt', 'CBC', 'Finlistval', 'Coresession', 'Referral', 'Uniser-TZ', 'MQMSwiftIn-TZ', 'MQMSwiftOut-TZ', 'MQMRtgsIn-TZ', 'MQMRtgsOut-TZ', 'MQMRead-TZ', 'Dispatcher-TZ', 'Binagent-TZ', 'Swiftsrv-TZ', 'Pmssrv-TZ', 'Genlimo-TZ', 'Aabsrv-TZ', 'Eabgst-TZ']
fpath = 'C:/Users/A248080/PycharmProjects/somans/data/finmonitor/'
files = [path.basename(f)[:-4] for f in iglob(fpath + "*.txt")]

status = []
for fin in standard_fins:
    if fin in files:
        status.append('UP')
        print(fin)
    else:
        status.append('DOWN')
print(status)
