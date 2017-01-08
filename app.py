#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""speeddating.py: Processes all speeddating choices and sends an SMS informing each participant of their matches."""

import csv
import sys

from participant import Participant
from smsgateway import SmsgatewayDevice, SmsgatewayAccount
from speeddate import SpeedDate

__author__ = "Maarten Desnouck"
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Maarten Desnouck"
__email__ = "maarten.desnouck@gmail.com"
__status__ = "Development"
__date__ = "18 Jan, 2016"

# Settings
MAX_MATCHES = 5
USERNAME = ""
PASSWORD = ""
DEVICEID = ""
addPhonenumbers = False

# Load participants
participants = []
with open('participants.csv', 'rb') as participantsFile:
    reader = csv.reader(participantsFile)
    participants = list(reader)

for participant in participants:
    participantList = []
    # first_name,last_name,sex,likes,org,year,E-mail,+TelNr,id
    participantList.append(Participant(int(participant[8]), participant[
        0], participant[1], participant[7]))

# Create a speeddate
closingMessage = " Met vriendelijke groeten van het Speeddating-team."
VTK_SpeedDate = SpeedDate(closingMessage, participantList)

# Read choices
with open('choices.csv', 'rb') as choicesFile:
    reader = csv.reader(choicesFile)
    choices = list(reader)

for choice in choices:
    choiceList = []
    for i in range(1, MAX_MATCHES + 1):
        choiceList.append(choice[i])
    VTK_SpeedDate.choose(choice[0], choiceList)
print("Choices have been correctly loaded.\n")

# Get messages to send
messages = VTK_SpeedDate.getMessages(addPhonenumbers)

# Create SMSgateway.me account and phone
account = SmsgatewayAccount(USERNAME, PASSWORD)
GSM = SmsgatewayDevice(account, DEVICEID)

# Ask if we can send the messages
send = str(raw_input('\nSend all created SMS messages? (Y|N) '))
if send.lower() == 'y':
    for message in messages:
        GSM.send(message[0].decode('utf-8'), message[1].decode('utf-8'))

    print("\nThe SMS messages in buffer have been sent to SMSgateway.me. Make sure the app on your phone is doing the rest.")
else:
    print("\nThe SMS messages in buffer have been CANCELLED!")
