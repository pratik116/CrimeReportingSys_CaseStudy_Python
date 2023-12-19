import dao.CreateTable as C
import dao.ICrimeAnalysisService as I
import exception.IncidentNumberNotFoundException as IncidentNumberNotFoundException

def main():

    # Creating all the tables in database
    C.CreateTable.CreateVictim()
    C.CreateTable.CreateSuspect()
    C.CreateTable.CreateIncident()
    C.CreateTable.CreateLawEnforcementAgencies()
    C.CreateTable.CreateOfficer()
    C.CreateTable.CreateEvidence()
    C.CreateTable.CreateReports()
    C.CreateTable.CreateCase()

    #Here I entered the dummy data in the mysql

    NewCARS=I.ICrimeAnalysisService()

    while True:
        try:
            print("\n****Welcome User*****\n")
            print("Press 1 to Add New Victim")
            print("Press 2 to Add New Suspect")
            print("Press 3 to Create New Incident")
            print("Press 4 to Update Incident Status")
            print("Press 5 to Get the Incidents from Date1 to Date2")
            print("Press 6 to Search Incidents from Incident Type")
            print("Press 7 to Generate Incident Report")
            print("Press 8 to Create New Case")
            print("Press 9 to Get the Case Using Case ID")
            print("Press 10 to Update the case Discreption using Case Id")
            print("Press 11 to Get List of all Cases")
            print("Press 12 to Exit")

            check = int(input("Enter Here: "))
            if check==1:
                I.ICrimeAnalysisService.AddNewVictim()

            elif check==2:
                I.ICrimeAnalysisService.AddNewSuspect()

            elif check==3:
                I.ICrimeAnalysisService.createIncident()
            
            elif check==4:
                try:
                    IID=int(input("Enter the Incident Id: "))
                    if not NewCARS.checkValidIncidentntId(incidentID=IID):
                        raise IncidentNumberNotFoundException.IncidentNumberNotFoundException
                    else:
                        Status=input("Enter the New Status of Incident: ")
                        NewCARS.updateIncidentStatus(IID,Status)
                except IncidentNumberNotFoundException.IncidentNumberNotFoundException as e:
                    print(e)
                except Exception as e:
                    print(e)

            elif check==5:
                start_date=input("Enter the Start date: ")
                end_date=input("Enter the End date: ")
                temp=NewCARS.getIncidentsInDateRange(start_date,end_date)
                for i in temp:
                    print(temp)

            elif check==6:
                Type=(input("Please Enter Incident Type: "))
                temp=NewCARS.searchIncidents(Type)
                for i in temp:
                    print(temp)

            elif check==7:
                NewCARS.generateIncidentReport()

            elif check==8:
                NewCARS.createCase()

            elif check==9:
                ID=input("Enter the Case Id: ")
                temp=NewCARS.getCaseDetails(caseID=ID)
                for i in temp:
                    print(temp)

            elif check==10:
                caseid=int(input("Enter Case Id: "))
                newdes=input("Enter The New Discription: ")
                NewCARS.Update_case_details(newdes,caseid)
            elif check==11:
                temp=(NewCARS.getAllCases())
                for i in temp:
                    print(temp)
            elif check==12:
                print("Thank You User")
                break
            else:
                print("\nInvalid Option")
        except Exception as e:
            print(e)


if __name__=='__main__':
    main()