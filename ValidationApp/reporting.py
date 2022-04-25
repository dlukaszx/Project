import pandas as pd
import dataBaseLogic

def generateValidationReport():
    reportName = 'ValidationReport.xlsx'
    diagramSheetName = 'Diagram'
    resultsSheetName = 'All_results'
    testCycleToBeReported = input ("Insert ID of Test Cycle to be reported: ")
    openedTestResultDatabase = pd.read_csv(dataBaseLogic.testResultDatabasePath, skiprows=0)
    openedTestCaseDatabase = pd.read_csv(dataBaseLogic.testCaseDatabasePath, skiprows=0)
    openedTestCycleDatabase = pd.read_csv(dataBaseLogic.testCycleDatabasePath, skiprows=0)
    checkIfTestCycleExists = dataBaseLogic.checkIfElementExistsInList(openedTestCycleDatabase, testCycleToBeReported)
    if  checkIfTestCycleExists == False:
        dataBaseLogic.listDatabase("testCycle")
        return 0
    filteredTestResultDatabase = openedTestResultDatabase[openedTestResultDatabase['Test_cycle'] == int(testCycleToBeReported)]
    passedTestsDatabase = filteredTestResultDatabase[filteredTestResultDatabase['Result'] == 'PASS']
    failedTestsDatabase = filteredTestResultDatabase[filteredTestResultDatabase['Result'] == 'FAIL']
    
    numberOfAllTestCases = len(openedTestCaseDatabase.index)
    numberOfTestResults = len(filteredTestResultDatabase.index)
    numberOfNotExecutedCases = numberOfAllTestCases - numberOfTestResults
    numberOfPassedTests = len(passedTestsDatabase.index)
    numberOfFailedTests = len(failedTestsDatabase.index)

    dataForChart = {'PASS': numberOfPassedTests, 'FAIL': numberOfFailedTests, 'NOT RUN': numberOfNotExecutedCases}
    dataFrameForChart = pd.DataFrame([dataForChart])
    
    writer = pd.ExcelWriter(reportName, engine='xlsxwriter')
    dataFrameForChart.to_excel(writer, sheet_name = diagramSheetName)
    filteredTestResultDatabase.to_excel(writer, sheet_name = resultsSheetName)
    workbook = writer.book
    worksheet = writer.sheets[diagramSheetName]
    chart = workbook.add_chart({'type': 'pie'})
    
    chart.add_series({
        'categories': '=Diagram!B1:D1',
        'values':     '=Diagram!B2:D2',
        'points': [
            {'fill': {'color': 'green'}},
            {'fill': {'color': 'red'}},
            {'fill': {'color': 'silver'}},
        ],
    })    
    
    worksheet.insert_chart('B4', chart)
    writer.save()