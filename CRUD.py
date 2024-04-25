import pyodbc

# Define variables
DBHost = 'BSS-PC110'
#DBName = 'RobotDatabase'
DBName = 'xyz'
connection_string = f'DRIVER={{SQL Server}};SERVER={DBHost};DATABASE={DBName};Trusted_Connection=yes'

# Function to connect to the database
def connect_to_database():
    return pyodbc.connect(connection_string)

# Function to create a table
def create_table(cursor):
    query = '''
        CREATE TABLE children (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            age INT
        )
    '''
    cursor.execute(query)
    cursor.commit()

# Function to insert data into the table
def insert_data(cursor, id, name, age):
    query = f"INSERT INTO children (id, name, age) VALUES ({id}, '{name}', {age})"
    cursor.execute(query)
    cursor.commit()

# Function to update data in the table
def update_data(cursor, id, name, age):
    query = f"UPDATE children SET name = '{name}', age = {age} WHERE id = {id}"
    cursor.execute(query)
    cursor.commit()

# Function to delete data from the table
def delete_data(cursor, id):
    query = f"DELETE FROM children WHERE id = {id}"
    cursor.execute(query)
    cursor.commit()

# Function to retrieve data from the table
# def retrieve_data(cursor):
#     cursor.execute("SELECT * FROM students")
#     return cursor.fetchall()

# Function to retrieve data from the table
def retrieve_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM children")
    data = cursor.fetchall()
    cursor.close()
    return data

