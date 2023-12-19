import util.DBConnUtil as conn
insert=conn.DBConnUtil()
class InsertIntoTable:
    @staticmethod
    def insertVictim(v):
        try:
            data=[(v.getVictimID,v.getFirstName,v.getLastName,v.getDateOfBirth,v.getGender,v.getcontact_information)]
            input_str='''INSERT INTO Victims (VictimID,FirstName,LastName,DateOfBirth,Gender,ContactInformation)
                        VALUES (%s,%s,%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Victim Details Stored in database...")
    
    @staticmethod
    def insertSuspect(s):
        try:
            data=[(s.getSuspectID,s.getFirstName,s.getLastName,s.getDateOfBirth,s.getGender,s.getcontact_information)]
            input_str='''INSERT INTO Suspects (SuspectID,FirstName,LastName,DateOfBirth,Gender,ContactInformation)
                        VALUES (%s,%s,%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Suspect's Details Stored in database...")

    @staticmethod
    def insertIncident(i):
        try:
            data=[(i.getIncidentID,i.getIncidentType,i.getIncidentDate,i.getLocation,i.getDescription,i.getStatus,i.getVictimID,i.getSuspectID)]
            input_str='''INSERT INTO Incidents (IncidentID,IncidentType,IncidentDate,Location,Description,Status,VictimID,SuspectID)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Incident Created...")

    @staticmethod
    def insertReport(r):
        try:
            data=[(r.getReportID,r.getIncidentID,r.getReportingOfficer,r.getReportDate,r.getReportDetails,r.getStatus)]
            input_str='''INSERT INTO Reports(ReportID,IncidentID,ReportingOfficer,ReportDate,ReportDetails,Status)
                        VALUES (%s,%s,%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Report Genereated...")
    
    @staticmethod
    def insertCase(c):
        try:
            data=[(c.getcaseID,c.getincidentIDs,c.getcaseDes)]
            input_str='''INSERT INTO Cases (caseID,IncidentIDs,caseDes)
                        VALUES (%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Case Genereated...")
    


