import time
from playsound3 import playsound
import re
import os.path
from filedialpy import openFile
from configparser import ConfigParser

config = ConfigParser()
try:
    config.read('config.ini')
    filePath = config.get('main', 'chatlog_path')
except:
    print("Config not found, opening file select window")
    filePath = openFile(title="Select pd2chat.log", filter="*.log")
    config.add_section('main')
    config.set('main', 'chatlog_path', filePath)
    with open('config.ini', 'w') as f:
        config.write(f)

lastOffer = ""
notificationSound = "notification.wav"

if os.path.isfile(notificationSound) == False:
    notificationSound = "notification.mp3"
    if os.path.isfile(notificationSound) == False:
        raise Exception("notification.wav or notification.mp3 were not found in the folder")

def parse(line):
    fromUser = re.search('(?<=From )(.*)(?=:)', line)
    whatItem = re.search('(?<=your )(.*)(?= listed)', line)
    price = re.search('(?<=for ).*)', line)

def printOffer(line):
    printCleanLine = re.search('(?<=From ).*', line)
    if printCleanLine == None:
        pass
    else:
        print(printCleanLine.group(0))

while True:
    f = open(filePath,'r', encoding="ISO-8859-1")
    lines = f.readlines()
    lastLine = lines[-1]
    if lastOffer == lastLine:
        pass
    elif lastLine.startswith("2,From") and "Hi" in lastLine:
        printOffer(lastLine)
        playsound(notificationSound)
        lastOffer = lastLine
    time.sleep(1)