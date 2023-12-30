class Suspect:
    # PrevSuspectId=10
    def __init__(self,FirstName,LastName,DateOfBirth,Gender,contact_information):
        # self._SuspectID=Suspect.PrevSuspectId+1
        # Suspect.PrevSuspectId+=1
        self._FirstName=FirstName
        self._LastName=LastName
        self._DateOfBirth=DateOfBirth
        self._Gender=Gender
        self._contact_information=contact_information

    # @property
    # def getSuspectID(self):
    #     return self._SuspectID

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
    def getDateOfBirth(self):
        return self._DateOfBirth

    @getDateOfBirth.setter
    def DateOfBirth(self,DateOfBirth):
        self._DateOfBirth=DateOfBirth

    @property
    def getGender(self):
        return self._Gender

    @getGender.setter
    def Gender(self,Gender):
        self._Gender=Gender

    @property
    def getcontact_information(self):
        return self._contact_information

    @getcontact_information.setter
    def contact_information(self,contact_information):
        self._contact_information=contact_information