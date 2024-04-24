*** Settings ***
Library     OperatingSystem
Library     custom.py

*** Test Cases ***
Create Parents Table
    ${output}=    Create Table
    Log    ${output}












#*** Settings ***
#Documentation       This is the default settings section
#Default Tags        default
#Library             DatabaseLibrary
#Library             OperatingSystem
#Library             Collections
#
#*** Variables ***
#${DBHost}           BSS-PC110
#${DBName}           RobotDatabase
#
#*** Test Cases ***
#Connect to SQL Server Database with Windows Authentication
#    [Documentation]    Connect to SQL Server database using Windows authentication
#    ${connection_string}=    Set Variable    DRIVER={SQL Server};SERVER=${DBHost};DATABASE=${DBName};Trusted_Connection=yes;
#    Connect To Database Using Custom Params    pyodbc    ${DBName}    ${connection_string}
#
##    ${connection_string}=    Set Variable    DRIVER={SQL Server};SERVER=${DBHost};Trusted_Connection=yes;
##    Connect To Database Using Custom Params    pyodbc       ${connection_string}
#
#
#    ${res}=      Execute SQL String    CREATE TABLE parents (id INT PRIMARY KEY,name VARCHAR(50),age INT)
#    Log     ${res}
#    Disconnect From Database
#
