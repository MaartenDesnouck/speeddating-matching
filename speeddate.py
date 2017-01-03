#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Speeddate klasse
class SpeedDate():
    participants = ""
    choices = ""
    afsluiter = ""

    # Constructor
    def __init__(self, afsluiter, participants):
        print("Er zijn "+str(len(participants))+" deelnemers.")
        self.afsluiter = afsluiter
        maxId = 0
        for participant in participants:
            if participant.id>maxId:
                maxId = participant.id

        self.participants = [None for x in range(maxId+1)]

        for participant in participants:
            if self.participants[participant.id] != None:
                print("Er zijn twee deelnemers met dezelfde id: "+str(participant.id))
                exit(1)
            self.participants[participant.id] = participant

        self.choices = [[False for x in range(maxId+1)] for x in range(maxId+1)]
        print("Grootste id is "+str(maxId)+".")
        print("Alle deelnemers zijn correct ingeladen.")

    # Id van de participant en een reeks met zijn keuzes
    def choose(self, participantId, choiceIds):
        for choiceId in choiceIds:
            if (choiceId != ""):
                if self.participants[int(choiceId)] == None:
                    print("Iemand heeft een keuze gemaakt met een onbestaande id: "+str(participantId)+" koos "+str(choiceId))
                    exit(1)
                elif self.participants[int(participantId)] == None:
                    print("Een onbestaande id heeft een keuze gemaakt: "+str(participantId))
                    exit(1)
                else:
                    self.choices[int(participantId)][int(choiceId)] = True

    # Creert de sms berichten op basis van de huidige deelnemers en keuzes
    def getMessages(self, addPhonenumbers):
        messages = []
        for participant in self.participants:
            matchIDs = []
            for otherParticipant in self.participants:
                if participant != None and otherParticipant != None:
                    if self.choices[participant.id][otherParticipant.id] and self.choices[otherParticipant.id][participant.id]:
                        matchIDs.append(otherParticipant.id)

            if participant != None and otherParticipant != None:
                if addPhonenumbers:
                    if len(matchIDs)==0:
                        msg = "Dag "+participant.first_name+", je hebt helaas geen matches. Misschien heb je meer succes op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                    elif len(matchIDs)==1:
                        msg = "Dag "+participant.first_name+", je hebt 1 match."
                        msg = msg+" Breng "+self.participants[matchIDs[0]].fullName()+" ("+self.participants[matchIDs[0]].phoneNumber+") maar eens een bezoekje op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                    elif len(matchIDs)==2:
                        msg = "Dag "+participant.first_name+", je hebt 2 matches."
                        msg = msg+" Breng "+self.participants[matchIDs[0]].fullName()+" ("+self.participants[matchIDs[0]].phoneNumber+")"
                        msg = msg+" en "+self.participants[matchIDs[1]].fullName()+" ("+self.participants[matchIDs[1]].phoneNumber+") maar eens een bezoekje op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                    elif len(matchIDs)>2:
                        msg = "Dag "+participant.first_name+", je hebt "+str(len(matchIDs))+" matches. Breng"
                        for i in range(0,len(matchIDs)-1):
                            msg = msg +" "+self.participants[matchIDs[i]].fullName()+" ("+self.participants[matchIDs[i]].phoneNumber+")"
                            if(i<len(matchIDs)-2):
                                msg = msg + ","
                        msg = msg +" en "+self.participants[matchIDs[len(matchIDs)-1]].fullName()+" ("+self.participants[matchIDs[len(matchIDs)-1]].phoneNumber+") maar eens een bezoekje op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                else:
                    if len(matchIDs)==0:
                        msg = "Dag "+participant.first_name+", je hebt helaas geen matches. Misschien heb je meer succes op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                    elif len(matchIDs)==1:
                        msg = "Dag "+participant.first_name+", je hebt 1 match."
                        msg = msg+" Breng "+self.participants[matchIDs[0]].fullName()+" maar eens een bezoekje op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                    elif len(matchIDs)==2:
                        msg = "Dag "+participant.first_name+", je hebt 2 matches."
                        msg = msg+" Breng "+self.participants[matchIDs[0]].fullName()
                        msg = msg+" en "+self.participants[matchIDs[1]].fullName()+" maar eens een bezoekje op de afterparty in Delta!"
                        msg = msg + self.afsluiter
                    elif len(matchIDs)>2:
                        msg = "Dag "+participant.first_name+", je hebt "+str(len(matchIDs))+" matches. Breng"
                        for i in range(0,len(matchIDs)-1):
                            msg = msg +" "+self.participants[matchIDs[i]].fullName()
                            if(i<len(matchIDs)-2):
                                msg = msg + ","
                        msg = msg +" en "+self.participants[matchIDs[len(matchIDs)-1]].fullName()+" maar eens een bezoekje op de afterparty in Delta!"
                        msg = msg + self.afsluiter

                print("Created message: "+participant.phoneNumber+" : "+msg)
                messages.append((participant.phoneNumber,msg))
        return messages
