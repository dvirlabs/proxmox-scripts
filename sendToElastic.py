from datetime import datetime

def sendLogs(es, author, text):
    doc = {
        'author': author,
        'text': text,
        'timestamp': datetime.now(),
    }
    return es.index(index="proxmox-python", document=doc)