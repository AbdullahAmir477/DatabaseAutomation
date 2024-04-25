*** Settings ***
Library     CRUD.py    # Replace 'path.to.your.python.module' with the actual path to your Python module
#Library     DatabaseLibrary
#Library     SeleniumLibrary
#Library     OperatingSystem

*** Test Cases ***
Perform CRUD Operations on Database
    # Connect to the database
    ${connection}=    Connect To Database

    # Create table
    #Create Table    ${connection}

#    # Insert data
#    Insert Data    ${connection}    1    "Alice"    25
#    Insert Data    ${connection}    2    "John"    20
#    Insert Data    ${connection}    3    "Jamal"    30
#
#    # Update data
#    Update Data    ${connection}    1    "Alice Smith"    26
#
#    # Delete data
    Delete Data    ${connection}    2
    Delete Data    ${connection}    1
#
    # Retrieve data
    ${data}=        Retrieve Data    ${connection}
    Log Many    ${data}

    # Close connection
    #Close Connection    ${connection}
    #Disconnect From All Databases

