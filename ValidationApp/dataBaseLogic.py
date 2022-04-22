from os import listdir
from os.path import exists, isfile, join
import pandas as pd

databaseLocation = "Database/"
testCaseDatabasePath = "Database/testCases.csv"
testPlanDatabasePath = "Database/testPlans.csv"
testCaseDefinitionDatabasePath = "Database/testCasesDefinitions.csv"
testResultDatabasePath = "Database/testResults.csv"
testCycleDatabasePath = "Database/testCycles.csv"

def insertToDatabase(databaseName):
	workingDatabase = selectDatabase(databaseName)
	if exists(workingDatabase):
		databaseWriteMode = 'a'
		writeHeaderIntoBase = False
	else:
		databaseWriteMode = 'w'
		writeHeaderIntoBase = True
	newId = findUniqueId()
	test_case = {
					'Id' : [newId],
					'Name' : ['TestCase'],
					'Title' : ['TitleOfTC']
				}
				
	dataFrame = pd.DataFrame(test_case)
	dataFrame.to_csv(workingDatabase, mode=databaseWriteMode, header=writeHeaderIntoBase, index=False, encoding='utf-8')
	
def listDatabase(databaseName):
	workingDatabase = selectDatabase(databaseName)
	if exists(workingDatabase):
		testCaseDatabase = pd.read_csv(workingDatabase)
		print (testCaseDatabase.head())
	else:
		print ("ERROR - selected database doesn't exist")
		return 0

def selectDatabase(databaseName):
	match databaseName:
		case "testCase":
			return testCaseDatabasePath
		case "testPlan":
			return testPlanDatabasePath
		case "testCaseDefinition":
			return testCaseDefinitionDatabasePath
		case "testResult":
			return testResultDatabasePath
		case "testCycle":
			return testCycleDatabasePath

def findUniqueId():
	listOfExistingDatabases = [file for file in listdir(databaseLocation) if isfile(join(databaseLocation, file))]
	allIds = []
	for database in listOfExistingDatabases:
		openedDatabase = pd.read_csv(databaseLocation + database, skiprows=0)
		allIds.extend(openedDatabase["Id"])
	return max(allIds)+1