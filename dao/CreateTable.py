import util.DBConnUtil as conn
create=conn.DBConnUtil()
class CreateTable:
    @staticmethod
    def CreateVictim():
        try:
            create_str='''CREATE TABLE  if not exists Victims(
            VictimID INT PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            DateOfBirth DATE,
            Gender CHAR(1),
            ContactInformation TEXT
            );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)

    @staticmethod
    def CreateSuspect():
        try:
            create_str='''CREATE TABLE if not exists Suspects (
            SuspectID INT PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            DateOfBirth DATE,
            Gender CHAR(1),
            ContactInformation TEXT
            );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)

    @staticmethod
    def CreateIncident():
        try:
            create_str='''CREATE TABLE Incidents (
            IncidentID INT PRIMARY KEY,
            IncidentType VARCHAR(255),
            IncidentDate DATE,
            Location VARCHAR(255),
            Description TEXT,
            Status VARCHAR(50),
            VictimID INT,
            SuspectID INT,
            FOREIGN KEY (VictimID) REFERENCES Victims(VictimID),
            FOREIGN KEY (SuspectID) REFERENCES Suspects(SuspectID)
            );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)

    @staticmethod
    def CreateLawEnforcementAgencies():
        try:
            create_str='''CREATE TABLE if not exists LawEnforcementAgencies (
            AgencyID INT PRIMARY KEY,
            AgencyName VARCHAR(255),
            Jurisdiction VARCHAR(255),
            ContactInformation TEXT
            );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)  

    @staticmethod
    def CreateOfficer():
        try:
            create_str='''CREATE TABLE if not exists Officers (
            OfficerID INT PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            BadgeNumber VARCHAR(50),
            Officer_Rank VARCHAR(50),
            ContactInformation varchar(255),
            AgencyID INT,
            FOREIGN KEY (AgencyID) REFERENCES LawEnforcementAgencies(AgencyID)
        );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)  

    @staticmethod
    def CreateEvidence():
        try:
            create_str='''CREATE TABLE if not exists Evidence (
            EvidenceID INT PRIMARY KEY,
            Description TEXT,
            LocationFound VARCHAR(255),
            IncidentID INT,
            FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID)
        );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)

    @staticmethod
    def CreateReports():
        try:
            create_str='''CREATE TABLE if not exists Reports (
            ReportID INT PRIMARY KEY,
            IncidentID INT,
            ReportingOfficer INT,
            ReportDate DATE,
            ReportDetails TEXT,
            Status VARCHAR(50),
            FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID),
            FOREIGN KEY (ReportingOfficer) REFERENCES Officers(OfficerID)
        );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e) 
        
    @staticmethod
    def CreateCase():
        try:
            create_str='''CREATE TABLE if not exists Cases (
            caseID INT PRIMARY KEY,
            IncidentIDs varchar(100),
            caseDes varchar(255)
            
        );'''
            create.open()
            create.stmt.execute(create_str)
            create.close()
            print("Table Created...")
        except Exception as e:
            print(e)
