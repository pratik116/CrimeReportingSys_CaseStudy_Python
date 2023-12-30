import util.DBConnUtil as conn
insert=conn.DBConnUtil()
class InsertIntoTable:
    @staticmethod
    def insertVictim(v):
        try:
            data=[(v.getFirstName,v.getLastName,v.getDateOfBirth,v.getGender,v.getcontact_information)]
            input_str='''INSERT INTO Victims (FirstName,LastName,DateOfBirth,Gender,ContactInformation)
                        VALUES (%s,%s,%s,%s,%s);
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
            data=[(s.getFirstName,s.getLastName,s.getDateOfBirth,s.getGender,s.getcontact_information)]
            input_str='''INSERT INTO Suspects (FirstName,LastName,DateOfBirth,Gender,ContactInformation)
                        VALUES (%s,%s,%s,%s,%s);
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
            data=[(i.getIncidentType,i.getIncidentDate,i.getLocation,i.getDescription,i.getStatus,i.getVictimID,i.getSuspectID)]
            input_str='''INSERT INTO Incidents (IncidentType,IncidentDate,Location,Description,Status,VictimID,SuspectID)
                        VALUES (%s,%s,%s,%s,%s,%s,%s);
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
            data=[(r.getIncidentID,r.getReportingOfficer,r.getReportDate,r.getReportDetails,r.getStatus)]
            input_str='''INSERT INTO Reports(IncidentID,ReportingOfficer,ReportDate,ReportDetails,Status)
                        VALUES (%s,%s,%s,%s,%s);
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
            data=[(c.getincidentIDs,c.getcaseDes)]
            input_str='''INSERT INTO Cases (IncidentIDs,caseDes)
                        VALUES (%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Case Genereated...")
    


