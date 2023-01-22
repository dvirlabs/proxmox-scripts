import subprocess
from elasticsearch import Elasticsearch
from sendToElastic import sendLogs
import sys    
import os    

file_name =  os.path.basename(sys.argv[0])
es = Elasticsearch(['http://<elastic-user>:<elastic-password>@<elastic-ip:port (default-9200)>'])

listID = [102,103,107,110,111,112,113,115,116,118,119]

for getConID in listID:
    getDate = subprocess.getstatusoutput('date')
    stopLXC = subprocess.getstatusoutput('pct stop ' + str(getConID))
    print("Container " + str(getConID) + " was stopped")
    textToSend = " Container " + str(getConID) + " was stopped"
    res = sendLogs(es, file_name, textToSend)
    print(res)
    with open("stoppedLXCLog.txt" ,'a') as log_file:
        log_file.write(getDate[1] + " Container " + str(getConID) + " was stopped" + "\n")
        