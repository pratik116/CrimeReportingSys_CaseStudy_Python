class LawEnforcementAgency:
    def __init__(self,AgencyID,AgencyName,Jurisdiction,contact_information):
        self._AgencyID=AgencyID
        self._AgencyName=AgencyName
        self._Jurisdiction=Jurisdiction
        self._contact_information=contact_information

    @property
    def getAgencyID(self):
        return self._AgencyID

    @property
    def getAgencyName(self):
        return self._agency_name

    @getAgencyName.setter
    def AgencyName(self,AgencyName):
        self._AgencyName=AgencyName

    @property
    def getJurisdiction(self):
        return self._Jurisdiction

    @getJurisdiction.setter
    def Jurisdiction(self,Jurisdiction):
        self._Jurisdiction=Jurisdiction

    @property
    def getcontact_information(self):
        return self._contact_information

    @getcontact_information.setter
    def contact_information(self, value):
        self._contact_information = value


