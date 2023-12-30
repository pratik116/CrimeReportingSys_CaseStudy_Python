class Case:
    # prevCaseId=3
    def __init__(self,caseDes,incidentIDs):
        # self._caseID=Case.prevCaseId+1
        # Case.prevCaseId+=1
        self._caseDes=caseDes
        self._incidentIDs=incidentIDs
    
    # @property
    # def getcaseID(self):
    #     return self._caseID
    
    @property
    def getcaseDes(self):
        return self._caseDes
    
    @getcaseDes.setter
    def caseDes(self,caseDes):
        self._caseDes=caseDes

    @property
    def getincidentIDs(self):
        return self._incidentIDs

    @getincidentIDs.setter
    def incidentIDs(self,incidentIDs):
        self._incidentIDs=incidentIDs

    

