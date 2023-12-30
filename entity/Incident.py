class Incident:
    prevIncidentId=5
    def __init__(self,IncidentType,IncidentDate,Location,Description,Status,VictimID,SuspectID):
        # self._IncidentID=Incident.prevIncidentId+1
        # Incident.prevIncidentId+=1
        self._IncidentType=IncidentType
        self._IncidentDate=IncidentDate
        self._Location=Location
        self._Description=Description
        self._Status=Status
        self._VictimID=VictimID
        self._SuspectID=SuspectID

    # @property
    # def getIncidentID(self):
    #     return self._IncidentID

    @property
    def getIncidentType(self):
        return self._IncidentType

    @getIncidentType.setter
    def IncidentType(self,IncidentType):
        self._IncidentType=IncidentType

    @property
    def getIncidentDate(self):
        return self._IncidentDate

    @getIncidentDate.setter
    def IncidentDate(self,IncidentDate):
        self._IncidentDate=IncidentDate

    @property
    def getLocation(self):
        return self._Location

    @getLocation.setter
    def Location(self,Location):
        self._Location=Location

    @property
    def getDescription(self):
        return self._Description

    @getDescription.setter
    def Description(self,Description):
        self._Description=Description

    @property
    def getStatus(self):
        return self._Status

    @getStatus.setter
    def Status(self,Status):
        self._Status=Status

    @property
    def getVictimID(self):
        return self._VictimID

    @getVictimID.setter
    def VictimID(self,VictimID):
        self._VictimID=VictimID

    @property
    def getSuspectID(self):
        return self._SuspectID

    @getSuspectID.setter
    def SuspectID(self,SuspectID):
        self._SuspectID=SuspectID