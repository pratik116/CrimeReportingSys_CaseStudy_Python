class Officer:
    prevOfficerId=5
    def __init__(self,FirstName,LastName,BadgeNumber,Rank,contact_information,AgencyID):
        self._OfficerID=Officer.prevOfficerId+1
        Officer.prevOfficerId+=1
        self._FirstName=FirstName
        self._LastName=LastName
        self._BadgeNumber=BadgeNumber
        self._Rank=Rank
        self._contact_information=contact_information
        self._AgencyID=AgencyID

    @property
    def getOfficerID(self):
        return self._OfficerID

    @property
    def getFirstName(self):
        return self._FirstName

    @getFirstName.setter
    def FirstName(self,FirstName):
        self._FirstName=FirstName

    @property
    def getLastName(self):
        return self._LastName

    @getLastName.setter
    def LastName(self,LastName):
        self._LastName=LastName

    @property
    def getBadgeNumber(self):
        return self._BadgeNumber

    @getBadgeNumber.setter
    def BadgeNumber(self,BadgeNumber):
        self._BadgeNumber=BadgeNumber

    @property
    def getRank(self):
        return self._Rank

    @getRank.setter
    def Rank(self,Rank):
        self._Rank=Rank

    @property
    def getcontact_information(self):
        return self._contact_information

    @getcontact_information.setter
    def contact_information(self, value):
        self._contact_information = value

    @property
    def getAgencyID(self):
        return self._AgencyID

    @getAgencyID.setter
    def AgencyID(self,AgencyID):
        self._AgencyID=AgencyID