# database_operations.py

import pyodbc

def create_table():
    # Define variables
    DBHost = 'BSS-PC110'
    DBName = 'RobotDatabase'

    # Construct connection string
    connection_string = f'DRIVER={{SQL Server}};SERVER={DBHost};DATABASE={DBName};Trusted_Connection=yes'

    # Connect to the database
    connection = pyodbc.connect(connection_string)

    # Create cursor
    cursor = connection.cursor()

    # Execute query to create table
    query = '''
        CREATE TABLE children (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            age INT
        )
    '''
    cursor.execute(query)

    # Commit transaction
    connection.commit()

    # Close cursor and connection
    cursor.close()
    connection.close()














# from robot.libraries.BuiltIn import BuiltIn
# from robot.api.deco import keyword
# import pyodbc
#
# # Define variables
# DBHost = 'BSS-PC110'
# DBName = 'RobotDatabase'
#
# # Construct connection string
# connection_string = f'DRIVER={{SQL Server}};SERVER={DBHost};DATABASE={DBName};Trusted_Connection=yes'
#
# # Connect to the database
# connection = pyodbc.connect(connection_string)
#
# # Create cursor
# cursor = connection.cursor()
#
# # Execute query to create table
# query = '''
#     CREATE TABLE students (
#         id INT PRIMARY KEY,
#         name VARCHAR(50),
#         age INT
#     )
# '''
# cursor.execute(query)
#
# # Commit transaction
# connection.commit()
#
# # Close cursor and connection
# cursor.close()
# connection.close()
