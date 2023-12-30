class Evidence:
    prevEvidenceId=5
    def __init__(self,Description,location_found,IncidentID):
        # self._EvidenceID=Evidence.prevEvidenceId+1
        # Evidence.prevEvidenceId+=1
        self._Description=Description
        self._location_found=location_found
        self._IncidentID=IncidentID

    @property
    def getEvidenceID(self):
        return self._evidence_id

    @property
    def getDescription(self):
        return self._Description

    @getDescription.setter
    def Description(self,Description):
        self._Description=Description

    @property
    def getlocation_found(self):
        return self._location_found

    @getlocation_found.setter
    def location_found(self,location_found):
        self._location_found=location_found

    # @property
    # def getIncidentID(self):
    #     return self._incident_id

    # @getIncidentID.setter
    # def IncidentID(self,IncidentID):
    #     self._IncidentID=IncidentID

