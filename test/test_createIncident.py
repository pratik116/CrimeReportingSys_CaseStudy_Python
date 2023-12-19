import unittest
import util.DBConnUtil as DB
import dao.ICrimeAnalysisService as I
import entity.Incident as IN
temp=DB.DBConnUtil()
class TestCreateIncident(unittest.TestCase):
    def testCreateIncidentmethod(self):
        temp.open()
        I.ICrimeAnalysisService.createIncident()
        prev=IN.Incident.prevIncidentId
        temp.stmt.execute(f"SELECT * FROM Incidents WHERE IncidentID={prev}")
        result =temp.stmt.fetchone()
        self.assertEqual(result[0],prev)
        
    def testupdateIncidentStatus(self):
        obj=I.ICrimeAnalysisService()
        temp.open()
        IID=int(input("Enter the Incident Id: "))
        Status=input("Enter the New Status of Incident: ")
        obj.updateIncidentStatus(IID,Status)
        temp.stmt.execute(f"SELECT * FROM Incidents WHERE IncidentID={IID}")
        result =temp.stmt.fetchone()
        self.assertEqual(result[5],Status)
    
    def tearDown(self):
        temp.close()

if __name__ == '__main__':
    unittest.main()
