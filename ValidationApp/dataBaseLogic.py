from datetime import date
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
	if databaseName == "testCase":
		dataToInsert = createNewTestCase(newId)
	if databaseName == "testPlan":
		dataToInsert = createNewTestPlan(newId)
	if databaseName == "testCaseDefinition":
		dataToInsert = createNewTestCaseDefinition(newId)
	if databaseName == "testResult":
		dataToInsert = createNewTestResult(newId)
	if databaseName == "testCycle":
		dataToInsert = createNewTestCycle(newId)
	
	if dataToInsert == 0:
		print ("Wrong input")
	else:
		dataFrame = pd.DataFrame(dataToInsert)
		dataFrame.to_csv(workingDatabase, mode=databaseWriteMode, header=writeHeaderIntoBase, index=False, encoding='utf-8')
	
def listDatabase(databaseName):
	workingDatabasePath = selectDatabase(databaseName)
	if exists(workingDatabasePath):
		workingDatabase = pd.read_csv(workingDatabasePath)
		print (workingDatabase)
	else:
		print ("ERROR - selected database doesn't exist")
		return 0

def selectDatabase(databaseName):
	if databaseName == "testCase":
		return testCaseDatabasePath
	if databaseName == "testPlan":
		return testPlanDatabasePath
	if databaseName == "testCaseDefinition":
		return testCaseDefinitionDatabasePath
	if databaseName == "testResult":
		return testResultDatabasePath
	if databaseName == "testCycle":
		return testCycleDatabasePath

def findUniqueId():
	listOfExistingDatabases = [file for file in listdir(databaseLocation) if isfile(join(databaseLocation, file))]
	allIds = [0]
	for database in listOfExistingDatabases:
		openedDatabase = pd.read_csv(databaseLocation + database, skiprows=0)
		allIds.extend(openedDatabase["Id"])
	return max(allIds)+1
	
def testCasePattern(id, title, description, configuration, date, priority, owner, parentId):
	dataToInsert = {
					'Id' : [id],
					'Record_type' : ['TestCase'],
					'Title' : [title],
					'Description' : [description],
					'Configuration' : [configuration],
					'Date' : [date],
					'Priority' : [priority],
					'Owner' : [owner],
					'Parent_TC_Definition' : [parentId]
					}
	return dataToInsert;
	
def testPlanPattern(id, title, description, date, priority, owner):
	dataToInsert = {
					'Id' : [id],
					'Record_type' : ['TestPlan'],
					'Title' : [title],
					'Description' : [description],
					'Date' : [date],
					'Priority' : [priority],
					'Owner' : [owner],
					}
	return dataToInsert;
	
def testCaseDefinitionPattern(id, title, description, date, priority, owner, testPlanId):
	dataToInsert = {
					'Id' : [id],
					'Record_type' : ['TestCaseDefinition'],
					'Title' : [title],
					'Description' : [description],
					'Date' : [date],
					'Priority' : [priority],
					'Owner' : [owner],
					'Related_Test_Plans' : [testPlanId]
					}
	return dataToInsert;
	
def testResultPattern(id, title, result, date, owner, parentId, cycleId):
	dataToInsert = {
					'Id' : [id],
					'Record_type' : ['TestResult'],
					'Title' : [title],
					'Test_cycle' : [cycleId],
					'Result' : [result],
					'Date' : [date],
					'Owner' : [owner],
					'Parent_Test_Case' : [parentId],
					}
	return dataToInsert;
	
def testCyclePattern(id, title, version, date, owner):
	dataToInsert = {
					'Id' : [id],
					'Record_type' : ['TestCycle'],
					'Title' : [title],
					'Build_version' : [version],
					'Date' : [date],
					'Owner' : [owner]
					}
	return dataToInsert;
	
def createNewTestCase(id):
	parentTcdId = input ("Insert ID of parent Test Case Definition for new Test Case: ")
	openedTestCaseDefinitionDatabase = pd.read_csv(testCaseDefinitionDatabasePath, skiprows=0)
	testCaseDefinitionIds =[]
	testCaseDefinitionIds.extend(openedTestCaseDefinitionDatabase["Id"])
	checkIfTcdExists = checkIfElementExistsInList(testCaseDefinitionIds, parentTcdId)
	if  checkIfTcdExists == False:
		listDatabase("testCaseDefinition")
		return 0
	tcdRowIndex = openedTestCaseDefinitionDatabase[openedTestCaseDefinitionDatabase['Id']==int(parentTcdId)].index.values.astype(int)[0]
	testCaseTitle = openedTestCaseDefinitionDatabase['Title'].values[tcdRowIndex]
	testCaseDescription = openedTestCaseDefinitionDatabase['Description'].values[tcdRowIndex]
	testCaseDate = date.today()
	testCaseConfiguration = input("Specify configuration for this Test Case: ")
	testCasePriority = input("Specify priority of this Test Case: ")
	testCaseOwner = input("Specify owner of this Test Case: ")
	data = testCasePattern(id, testCaseTitle, testCaseDescription, testCaseConfiguration, testCaseDate, testCasePriority, testCaseOwner, parentTcdId)
	return data

def createNewTestPlan(id):
	testPlanDate = date.today()
	testPlanTitle = input("Specify title for this Test Plan: ")
	testPlanDescription = input("Specify description for this Test Plan: ")
	testPlanPriority = input("Specify priority of this Test Plan: ")
	testPlanOwner = input("Specify owner of this Test Plan: ")
	data = testPlanPattern(id, testPlanTitle, testPlanDescription, testPlanDate, testPlanPriority, testPlanOwner)
	return data
	
def createNewTestCaseDefinition(id):
	testPlanId = input ("What Test Plan is this definition for? ")
	openedTestPlanDatabase = pd.read_csv(testPlanDatabasePath, skiprows=0)
	testPlanIds =[]
	testPlanIds.extend(openedTestPlanDatabase["Id"])
	checkIfTestPlanExists = checkIfElementExistsInList(testPlanIds, testPlanId)
	if  checkIfTestPlanExists == False:
		listDatabase("testPlan")
		return 0
	testPlanId += "+"
	testCaseDefinitionDate = date.today()
	testCaseDefinitionTitle = input("Specify title for this Test Case Definition: ")
	testCaseDefinitionDescription = input("Specify description for this Test Case Definition: ")
	testCaseDefinitionPriority = input("Specify priority of this Test Case Definition: ")
	testCaseDefinitionOwner = input("Specify owner of this Test Case Definition: ")
	data = testCaseDefinitionPattern(id, testCaseDefinitionTitle, testCaseDefinitionDescription, testCaseDefinitionDate, testCaseDefinitionPriority, testCaseDefinitionOwner, testPlanId)
	return data
	
def createNewTestResult(id):
	parentTestCaseId = input ("Insert ID of Test Case to add new result: ")
	openedTestCaseDatabase = pd.read_csv(testCaseDatabasePath, skiprows=0)
	testCaseIds =[]
	testCaseIds.extend(openedTestCaseDatabase["Id"])
	checkIfTestCaseExists = checkIfElementExistsInList(testCaseIds, parentTestCaseId)
	if  checkIfTestCaseExists == False:
		listDatabase("testCase")
		return 0
	testCycleId = input ("Insert ID of Test Cycle for this result: ")
	openedTestCycleDatabase = pd.read_csv(testCycleDatabasePath, skiprows=0)
	testCycleIds =[]
	testCycleIds.extend(openedTestCycleDatabase["Id"])
	checkIfTestCycleExists = checkIfElementExistsInList(testCycleIds, testCycleId)
	if  checkIfTestCycleExists == False:
		listDatabase("testCycle")
		return 0
	testCaseRowIndex = openedTestCaseDatabase[openedTestCaseDatabase['Id']==int(parentTestCaseId)].index.values.astype(int)[0]
	testResultTitle = openedTestCaseDatabase['Title'].values[testCaseRowIndex]
	testResultConfiguration = openedTestCaseDatabase['Configuration'].values[testCaseRowIndex]
	testResult = input("What is the result of this test: ")
	testResultDate = date.today()
	testResultOwner = input("Who is submitting result? ")
	data = testResultPattern(id, testResultTitle, testResult, testResultDate, testResultOwner, parentTestCaseId, testCycleId)
	return data
	
def createNewTestCycle(id):
	testCycleDate = date.today()
	testCycleTitle = input("Specify title for this Test Cycle: ")
	testCycleVersion = input("Specify build version: ")
	testCycleOwner = input("Specify owner of this Test Cycle: ")
	data = testCyclePattern(id, testCycleTitle, testCycleVersion, testCycleDate, testCycleOwner)
	return data

def addRelationBetweenTpAndTcd():
	testCaseDefinitionId = input ("Insert ID of Test Case Definition to add relation: ")
	openedTestCaseDefinitionDatabase = pd.read_csv(testCaseDefinitionDatabasePath, skiprows=0)
	testCaseDefinitionIds =[]
	testCaseDefinitionIds.extend(openedTestCaseDefinitionDatabase["Id"])
	checkIfTcdExists = checkIfElementExistsInList(testCaseDefinitionIds, testCaseDefinitionId)
	if  checkIfTcdExists == False:
		listDatabase("testCaseDefinition")
		return 0
	testPlanId = input ("Insert ID of Test Plan to add relation ")
	openedTestPlanDatabase = pd.read_csv(testPlanDatabasePath, skiprows=0)
	testPlanIds =[]
	testPlanIds.extend(openedTestPlanDatabase["Id"])
	checkIfTestPlanExists = checkIfElementExistsInList(testPlanIds, testPlanId)
	if  checkIfTestPlanExists == False:
		listDatabase("testPlan")
		return 0
	testCaseDefinitionRowIndex = openedTestCaseDefinitionDatabase[openedTestCaseDefinitionDatabase['Id']==int(testCaseDefinitionId)].index.values.astype(int)[0]
	testPlansRelatedWithSelectedTcd = openedTestCaseDefinitionDatabase['Related_Test_Plans'].values[testCaseDefinitionRowIndex]
	listOfRelatedTestPans = testPlansRelatedWithSelectedTcd.split("+")
	for testPlan in listOfRelatedTestPans:
		if testPlan == testPlanId:
			print("Specified Test Case Definition is already corelated with this Test Plan")
			return 0
	valueToInsert = testPlansRelatedWithSelectedTcd + testPlanId + "+"
	openedTestCaseDefinitionDatabase.at[testCaseDefinitionRowIndex, 'Related_Test_Plans'] = valueToInsert
	openedTestCaseDefinitionDatabase.to_csv(testCaseDefinitionDatabasePath, index = False)

def checkIfElementExistsInList(listName, element):
	for singleElement in range(len(listName)):
		if str(listName[singleElement]) == element:
			return True
	print ("There is no record with specified ID.\n\n")
	print ("List of available records:\n")
	return False