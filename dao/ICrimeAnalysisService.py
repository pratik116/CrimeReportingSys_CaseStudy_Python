import util.DBConnUtil as DB
import exception.IncidentNumberNotFoundException as IncidentNumberNotFoundException
import dao.InsertIntoTable as I
import entity.Victim as V
import entity.Suspect as S
import entity.Incident as In
import entity.Reports as R
import entity.case as C

class ICrimeAnalysisService(DB.DBConnUtil):

    def checkValidIncidentntId(self,incidentID):
        try:
            self.open()
            self.stmt.execute(f"select * from Incidents where IncidentId={incidentID}")
            temp=self.stmt.fetchall()
            if not temp:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            self.close()

    @staticmethod
    def AddNewVictim():
        FirstName=input("Enter Victim's First Name: ") 
        LastName=input("Enter Victim's Last Name: ") 
        DateOfBirth=input("Enter Victim's Date Of Birth(YYYY-MM-DD): ")
        Gender=input("Enter Victim's Gender(M/F): ")
        contact_information=input("Enter Victim's Contact Information: ")
        newvictim=V.Victim(FirstName,LastName,DateOfBirth,Gender,contact_information)
        I.InsertIntoTable.insertVictim(newvictim)
    @staticmethod
    def AddNewSuspect():
        FirstName=input("Enter Suspect's First Name: ") 
        LastName=input("Enter Suspect's Last Name: ") 
        DateOfBirth=input("Enter Suspect's Date Of Birth(YYYY-MM-DD): ")
        Gender=input("Enter Suspect's Gender(M/F): ")
        contact_information=input("Enter Suspect's Contact Information: ")
        newsuspect=S.Suspect(FirstName,LastName,DateOfBirth,Gender,contact_information)
        I.InsertIntoTable.insertSuspect(newsuspect)
    @staticmethod
    def createIncident():
        # IncidentType,IncidentDate,Location,Description,Status,VictimID,SuspectID
        IncidentType=input("Enter Incident Type: ")
        IncidentDate=input("Enter Incident Date: ")
        Location=input("Enter the Incident Location: ")
        Description=input("Enter the Discription about Incident: ")
        Status=input("What is the Status of Incident: ")
        VictimID=int(input("Enter Victim ID: "))
        SuspectID=int(input("Enter Suspect ID: "))
        newincident=In.Incident(IncidentType,IncidentDate,Location,Description,Status,VictimID,SuspectID)
        I.InsertIntoTable.insertIncident(newincident)

    def updateIncidentStatus(self,incidentID,newstatus):
        try:
                update_str=f"Update Incidents set Status='{newstatus}' where IncidentID={incidentID}"
                self.open()
                self.stmt.execute(update_str) 
                self.conn.commit()
        except IncidentNumberNotFoundException.IncidentNumberNotFoundException as I:
            print(I)
        except Exception as e:
            print(e)
        else:
            self.close()
            print("Incident Status Updated..")
    
    def getIncidentsInDateRange(self,startdate,enddate):
        try:
            select_str=f"select * from Incidents where IncidentDate between '{startdate}' and '{enddate}'"
            self.open()
            self.stmt.execute(select_str)
            temp=self.stmt.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
        else:
            self.close()
            return temp
    
    def searchIncidents(self,IncidentType):
        try:
            select_str=f"select * from Incidents where IncidentType='{IncidentType}'"
            self.open()
            self.stmt.execute(select_str)
            temp=self.stmt.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
        else:
            self.close()
            return temp
        
    def generateIncidentReport(self):
        try:
            IncidentID=int(input("Enter Incident ID: "))
            ReportingOfficer=int(input("Enter Reporting Officer ID: "))
            ReportDate=input("Enter Report Data(YYYY-MM-DD): ")
            ReportDetails=input("Enter Report Details: ")
            Status=input("Enter Report Status: ")
            newreport=R.Report(IncidentID,ReportingOfficer,ReportDate,ReportDetails,Status)
            I.InsertIntoTable.insertReport(newreport)
        except Exception as e:
            print(e)
       
            
    def createCase(self):
        try:
            # caseID=int(input("Enter Case ID: "))
            caseDes=input("Enter Case Details: ")
            incidentIDs=input("Enter the ID's of involved incidents in Case: ")
            newcase=C.Case(caseDes,incidentIDs)
            I.InsertIntoTable.insertCase(newcase)
        except Exception as e:
            print(e)
        
        
    def getCaseDetails(self,caseID):
        try:
            select_str=f"select * from Cases where caseID={caseID}"
            self.open()
            self.stmt.execute(select_str)
            temp=self.stmt.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
        else:
            self.close()
            return temp
        
    def Update_case_details(self,newDescription,caseID):
        try:
            update_str=f"Update Cases set caseDes='{newDescription}' where caseID={caseID}"
            self.open()
            self.stmt.execute(update_str) 
            self.conn.commit()
        
        except Exception as e:
            print(e)
        else:
            self.close()
            print("Incident Status Updated..")

        
    def getAllCases(self):
        try:
            select_str=f"select * from Cases"
            self.open()
            self.stmt.execute(select_str)
            temp=self.stmt.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
        else:
            self.close()
            return temp
    

