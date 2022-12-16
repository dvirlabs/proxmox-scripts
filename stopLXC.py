import subprocess

listID = [123] # Insert the ID of the LXC you want to stop them
for getConID in listID:
    getDate = subprocess.getstatusoutput('date')
    stopLXC = subprocess.getstatusoutput('pct stop ' + str(getConID))
    print("Container " + str(getConID) + " was stopped")
    with open("stoppedLXCLog.txt" ,'a') as log_file:
        log_file.write(getDate[1] + " Container " + str(getConID) + " was stopped" + "\n")
