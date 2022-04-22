import os
import dataBaseLogic

cls = lambda: os.system('cls')

def mainMenu():
	cls()
	print ("Welcome in testing database.")
	print ("Choose the action:\n")
	print ("1. Add new record")
	print ("2. Add relation")
	print ("3. List all Test Cases for specific Test Plan")
	print ("4. List all Test Results for specific Test Plan")
	print ("5. List all Test Results for specific Test Cycle")
	print ("0. Leave program")
	
	selectedOption = input ("Select option: ")
	match selectedOption:
		case "1":
			print ("Option 1")
			addRecordMenu()
		case "2":
			print ("Option 2")
		case "3":
			dataBaseLogic.listDatabase("testCase")
		case "4":
			dataBaseLogic.listDatabase("testResult")
		case "5":
			dataBaseLogic.listDatabase("testResult")
		case "0":
			print ("Goodbye")
			quit()
		case _:
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
	match selectedOption:
		case "1":
			print ("Option 1")
			dataBaseLogic.insertToDatabase("testCase")
		case "2":
			print ("Option 2")
		case "3":
			print ("Option 3")
		case "4":
			print ("Option 4")
		case "5":
			print ("Option 5")
		case "9":
			print ("Moving to main menu")
			mainMenu()
		case "0":
			print ("Goodbye")
			quit()
		case _:
			print ("Selected option doesn't exist.")
	input("Press ENTER to continue...")
	addRecordMenu()
	