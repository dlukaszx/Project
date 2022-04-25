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
    
def testCasePattern(id, title, description, configuration, priority, owner, parentId):
    dataToInsert = {
                    'Id' : [id],
                    'Record_type' : ['TestCase'],
                    'Title' : [title],
                    'Description' : [description],
                    'Configuration' : [configuration],
                    'Date' : [date.today()],
                    'Priority' : [priority],
                    'Owner' : [owner],
                    'Parent_TC_Definition' : [parentId]
                    }
    return dataToInsert
    
def testPlanPattern(id, title, priority, owner):
    dataToInsert = {
                    'Id' : [id],
                    'Record_type' : ['TestPlan'],
                    'Title' : [title],
                    'Date' : [date.today()],
                    'Priority' : [priority],
                    'Owner' : [owner],
                    }
    return dataToInsert
    
def testCaseDefinitionPattern(id, title, description, priority, owner, testPlanId):
    dataToInsert = {
                    'Id' : [id],
                    'Record_type' : ['TestCaseDefinition'],
                    'Title' : [title],
                    'Description' : [description],
                    'Date' : [date.today()],
                    'Priority' : [priority],
                    'Owner' : [owner],
                    'Related_Test_Plans' : [testPlanId]
                    }
    return dataToInsert
    
def testResultPattern(id, title, result, owner, parentId, cycleId):
    dataToInsert = {
                    'Id' : [id],
                    'Record_type' : ['TestResult'],
                    'Title' : [title],
                    'Test_cycle' : [cycleId],
                    'Result' : [result],
                    'Date' : [date.today()],
                    'Owner' : [owner],
                    'Parent_Test_Case' : [parentId],
                    }
    return dataToInsert
    
def testCyclePattern(id, title, version, owner):
    dataToInsert = {
                    'Id' : [id],
                    'Record_type' : ['TestCycle'],
                    'Title' : [title],
                    'Build_version' : [version],
                    'Date' : [date.today()],
                    'Owner' : [owner]
                    }
    return dataToInsert
    
def createNewTestCase(id):
    askForDatabseList("testCaseDefinition")
    parentTcdId = input ("Insert ID of parent Test Case Definition for new Test Case: ")
    openedTestCaseDefinitionDatabase = pd.read_csv(testCaseDefinitionDatabasePath, skiprows=0)
    checkIfTcdExists = checkIfElementExistsInList(openedTestCaseDefinitionDatabase, parentTcdId)
    if  checkIfTcdExists == False:
        return 0
    tcdRowIndex = openedTestCaseDefinitionDatabase[openedTestCaseDefinitionDatabase['Id']==int(parentTcdId)].index.values.astype(int)[0]
    testCaseTitle = openedTestCaseDefinitionDatabase['Title'].values[tcdRowIndex]
    testCaseDescription = openedTestCaseDefinitionDatabase['Description'].values[tcdRowIndex]
    testCaseConfiguration = input("Specify configuration for this Test Case: ")
    testCasePriority = input("Specify priority of this Test Case: ")
    testCaseOwner = input("Specify owner of this Test Case: ")
    data = testCasePattern(id, testCaseTitle, testCaseDescription, testCaseConfiguration, testCasePriority, testCaseOwner, parentTcdId)
    return data

def createNewTestPlan(id):
    testPlanTitle = input("Specify title for this Test Plan: ")
    testPlanPriority = input("Specify priority of this Test Plan: ")
    testPlanOwner = input("Specify owner of this Test Plan: ")
    data = testPlanPattern(id, testPlanTitle, testPlanPriority, testPlanOwner)
    return data
    
def createNewTestCaseDefinition(id):
    askForDatabseList("testPlan")
    testPlanId = input ("What Test Plan is this definition for? ")
    openedTestPlanDatabase = pd.read_csv(testPlanDatabasePath, skiprows=0)
    checkIfTestPlanExists = checkIfElementExistsInList(openedTestPlanDatabase, testPlanId)
    if  checkIfTestPlanExists == False:
        return 0
    testPlanId += "+"
    testCaseDefinitionTitle = input("Specify title for this Test Case Definition: ")
    testCaseDefinitionDescription = input("Specify description for this Test Case Definition: ")
    testCaseDefinitionPriority = input("Specify priority of this Test Case Definition: ")
    testCaseDefinitionOwner = input("Specify owner of this Test Case Definition: ")
    data = testCaseDefinitionPattern(id, testCaseDefinitionTitle, testCaseDefinitionDescription, testCaseDefinitionPriority, testCaseDefinitionOwner, testPlanId)
    return data
    
def createNewTestResult(id):
    askForDatabseList("testCase")
    parentTestCaseId = input ("Insert ID of Test Case to add new result: ")
    openedTestCaseDatabase = pd.read_csv(testCaseDatabasePath, skiprows=0)
    checkIfTestCaseExists = checkIfElementExistsInList(openedTestCaseDatabase, parentTestCaseId)
    if  checkIfTestCaseExists == False:
        return 0
    askForDatabseList("testCycle")
    testCycleId = input ("Insert ID of Test Cycle for this result: ")
    openedTestCycleDatabase = pd.read_csv(testCycleDatabasePath, skiprows=0)
    checkIfTestCycleExists = checkIfElementExistsInList(openedTestCycleDatabase, testCycleId)
    if  checkIfTestCycleExists == False:
        return 0
    testCaseRowIndex = openedTestCaseDatabase[openedTestCaseDatabase['Id']==int(parentTestCaseId)].index.values.astype(int)[0]
    testResultTitle = openedTestCaseDatabase['Title'].values[testCaseRowIndex]
    testResultConfiguration = openedTestCaseDatabase['Configuration'].values[testCaseRowIndex]
    testResult = input("What is the result of this test (PASS/FAIL): ")
    if testResult == 'fail' or testResult == 'FAIL' or testResult == 'f' or testResult == 'F':
        testResult = 'FAIL'
    elif testResult == 'pass' or testResult == 'PASS' or testResult == 'p' or testResult == 'P':
        testResult = 'PASS'
    else:
        print (testResult + " is not valid result. Available results are PASS or FAIL")
        return 0
    testResultOwner = input("Who is submitting result? ")
    data = testResultPattern(id, testResultTitle, testResult, testResultOwner, parentTestCaseId, testCycleId)
    return data
    
def createNewTestCycle(id):
    testCycleTitle = input("Specify title for this Test Cycle: ")
    testCycleVersion = input("Specify build version: ")
    testCycleOwner = input("Specify owner of this Test Cycle: ")
    data = testCyclePattern(id, testCycleTitle, testCycleVersion, testCycleOwner)
    return data

def addRelationBetweenTpAndTcd():
    askForDatabseList("testCaseDefinition")
    testCaseDefinitionId = input ("Insert ID of Test Case Definition to add relation: ")
    openedTestCaseDefinitionDatabase = pd.read_csv(testCaseDefinitionDatabasePath, skiprows=0)
    checkIfTcdExists = checkIfElementExistsInList(openedTestCaseDefinitionDatabase, testCaseDefinitionId)
    if  checkIfTcdExists == False:
        return 0
    askForDatabseList("testPlan")
    testPlanId = input ("Insert ID of Test Plan to add relation ")
    openedTestPlanDatabase = pd.read_csv(testPlanDatabasePath, skiprows=0)
    checkIfTestPlanExists = checkIfElementExistsInList(openedTestPlanDatabase, testPlanId)
    if  checkIfTestPlanExists == False:
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

def checkIfElementExistsInList(dataBase, element):
    listName = []
    listName.extend(dataBase["Id"])
    for singleElement in range(len(listName)):
        if str(listName[singleElement]) == element:
            return True
    print ("There is no record with specified ID.\n\n")
    return False
    
def askForDatabseList(databaseName):
    while True:
        checkUserAnswer = input ("Do You want to list all records from " + databaseName + " database to check possible relation? (Y/N)")
        if checkUserAnswer == 'Y' or checkUserAnswer == 'y':
            listDatabase(databaseName)
            break
        elif checkUserAnswer == 'N' or checkUserAnswer == 'n':
            break
        else:
            print ("Please provide proper answer (Y/N)")

def listFilteredRecords(recordType, filteredBy):
    databasePath = selectDatabase(filteredBy)
    askForDatabseList(filteredBy)
    checkIfRecordExists = False
    relatedTo = '0'
    while checkIfRecordExists == False:
        relatedTo = input("Select %s to list all related %ss or type 0 to return to menu: " % (filteredBy, recordType))
        if relatedTo == '0':
            return False
        else:
            openedDatabase = pd.read_csv(databasePath, skiprows=0)
            checkIfRecordExists = checkIfElementExistsInList(openedDatabase, relatedTo)
            allRelatives = findRelation(recordType, filteredBy, relatedTo)
    return False

def relatives(databasePath, specialRow, relatedToId):
    relativesList = []
    openedDatabase = pd.read_csv(databasePath, skiprows=0)
    if specialRow == "TcTr":
        lookForRows = openedDatabase.loc[openedDatabase['Test_cycle'] == relatedToId]
        lookForRows = lookForRows['Test_cycle'].tolist()
    else:
        lookForRows = openedDatabase.apply(lambda row: row.str.contains(relatedToId).any(), axis=1)
        lookForRows = lookForRows.tolist()
    if lookForRows != '':
        for i in range(len(lookForRows)):
            if lookForRows[i] is not False:
                relatedToRow = openedDatabase.iloc[i]
                relativesList.append(relatedToRow.iloc[0])
    else:
        print("No relations found.")
        return False
    return relativesList

def findRelation(searchForType, relatedToType, relatedToId):
    lookForID = False
    relationIn = relatedToType
    allRelatives = []
    relatedRecords = []
    specialRow = ''
    while lookForID == False:
        if relatedToType == "testPlan":
            relationIn = "testCaseDefinition"
        elif relatedToType == "testResult":
            relationIn = "testCase"
        elif relatedToType == "testCycle":
            relationIn = "testResult"
            specialRow = "TcTr"
        else:
            lookForID = True
        #databasePath = selectDatabase(relationIn)
        allRelatives = relatives(selectDatabase(relationIn), specialRow, relatedToId)
        print("First-degree relation values for debugging: ", allRelatives)
        lookForID = True
    return relatedRecords

'''
Under development
        if searchForType != relationIn:
            if searchForType == "testResult" and relationIn == "testCaseDefinition" and relatedToType == "testPlan":
                relationIn = "testCase"
            elif searchForType == "testCase" and relationIn == "testCaseDefinition" and relatedToType == "testPlan":
                relationIn = "testCase"
                for i in range(len(allRelatives)):
                    layerRelatives = relatives(selectDatabase(relationIn), specialRow, allRelatives[i])
                    print(layerRelatives)
                    relatedRecords = relatedRecords.append(layerRelatives)
                lookForID = True
    databasePath = selectDatabase(relationIn)
    print(searchForType, relatedToType)
    openedDatabase = pd.read_csv(databasePath, skiprows=0)
    #relatedToRow = openedDatabase.loc[openedDatabase['Id'] == int(relatedToId)]  # dataframe
    #allRelatives = relatedToRow.iloc[:, -1].tolist()
    #print(allRelatives)
    if allRelatives == []:
        print("There are no related records")
    else:
        allRelatives = (str(allRelatives[0])).split('+')
    print(type(allRelatives))
    print(allRelatives)
'''
