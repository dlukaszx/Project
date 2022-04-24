import os
import dataBaseLogic
import reporting

cls = lambda: os.system('cls')

def mainMenu():
	cls()
	print ("Welcome in testing database.")
	print ("Choose the action:\n")
	print ("1. Add new record")
	print ("2. Corelate existing Test Case Definition with existing Test Plan")
	print ("3. List all Test Cases for specific Test Plan")
	print ("4. List all Test Results for specific Test Plan")
	print ("5. List all Test Results for specific Test Cycle")
	print ("6. Export validation report for selected Test Cycle")
	print ("0. Leave program")
	
	selectedOption = input ("Select option: ")
	if selectedOption == "1":
		addRecordMenu()
	elif selectedOption == "2":
		dataBaseLogic.addRelationBetweenTpAndTcd()
	elif selectedOption == "3":
		dataBaseLogic.listDatabase("testCase")
	elif selectedOption == "4":
		dataBaseLogic.listDatabase("testResult")
	elif selectedOption == "5":
		dataBaseLogic.listDatabase("testResult")
	elif selectedOption == "6":
		reporting.generateValidationReport()
	elif selectedOption == "0":
		print ("Press any key to exit")
		input()
		exit()
	else:
		print ("Selected option doesn't exist.")
	input("Press ENTER to continue...")
	mainMenu()
	
def addRecordMenu():
	cls()
	print ("Choose the action:\n")
	print ("1. Add new TestPlan")
	print ("2. Add new TestCaseDefinition")
	print ("3. Add new TestCase")
	print ("4. Add new TestResult")
	print ("5. Add new TestCycle")
	print ("9. Back to main menu")
	print ("0. Leave program")
	
	selectedOption = input ("Select option: ")
	if selectedOption == "1":
		dataBaseLogic.insertToDatabase("testPlan")
	elif selectedOption == "2":
		dataBaseLogic.insertToDatabase("testCaseDefinition")
	elif selectedOption == "3":
		dataBaseLogic.insertToDatabase("testCase")
	elif selectedOption == "4":
		dataBaseLogic.insertToDatabase("testResult")
	elif selectedOption == "5":
		dataBaseLogic.insertToDatabase("testCycle")
	elif selectedOption == "9":
		print ("Moving to main menu")
		mainMenu()
	elif selectedOption == "0":
		print ("Press any key to exit")
		input()
		exit()
	else:
		print ("Selected option doesn't exist.")
	input("Press ENTER to continue...")
	addRecordMenu()
	