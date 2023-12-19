class Report:
    prevReportID=5
    def __init__(self,IncidentID,ReportingOfficer,ReportDate,ReportDetails,Status='Draft'):
        self._ReportID=Report.prevReportID+1
        Report.prevReportID+=1
        self._IncidentID=IncidentID
        self._ReportingOfficer=ReportingOfficer
        self._ReportDate=ReportDate
        self._ReportDetails=ReportDetails
        self._Status=Status

    @property
    def getReportID(self):
        return self._ReportID

    @property
    def getIncidentID(self):
        return self._IncidentID

    @getIncidentID.setter
    def IncidentID(self,IncidentID):
        self._IncidentID=IncidentID

    @property
    def getReportingOfficer(self):
        return self._ReportingOfficer

    @getReportingOfficer.setter
    def ReportingOfficer(self,ReportingOfficer):
        self._ReportingOfficer=ReportingOfficer

    @property
    def getReportDate(self):
        return self._ReportDate

    @getReportDate.setter
    def ReportDate(self,ReportDate):
        self._ReportDate=ReportDate

    @property
    def getReportDetails(self):
        return self._ReportDetails

    @getReportDetails.setter
    def ReportDetails(self,ReportDetails):
        self._ReportDetails=ReportDetails

    @property
    def getStatus(self):
        return self._Status

    @getStatus.setter
    def Status(self,Status):
        self._Status=Status



