import subprocess
from elasticsearch import Elasticsearch
from sendToElastic import sendLogs
import sys    
import os    

file_name =  os.path.basename(sys.argv[0])
es = Elasticsearch(['http://dvir:dvir4210200H@192.168.1.250:31247'])

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
        








# Change the list to input and give to the user decide what container he want to stop
# Set the inputs in a list
# If the user set "done" in the input continue the script and stop this containers
# write to the log file also the hostname of the container (check this in startLXC.py)
