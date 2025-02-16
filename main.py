import pymssql

# Database connection parameters
server = 'your_server.database.windows.net'
user = 'your_username'
password = 'your_password'
database = 'your_database'

# Establish a connection to the database
conn = pymssql.connect(server, username, password, database)

# Create a new cursor
cursor = conn.cursor()

# Create a new table with one column
cursor.execute("""
IF NOT EXISTS (
    SELECT * 
    FROM sys.tables 
    WHERE name = 'TestTable'
)
CREATE TABLE TestTable (
    Id INT PRIMARY KEY,
    Data VARCHAR(255)
)
""")
conn.commit()

# Insert some dummy data
cursor.execute("INSERT INTO TestTable (Id, Data) VALUES (1, 'Dummy data 1'), (2, 'Dummy data 2')")
conn.commit()

# Query the data
cursor.execute('SELECT Id, Data FROM TestTable')

# Fetch all rows from the last executed statement
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(f"Id: {row[0]}, Data: {row[1]}")

# Close the cursor and the connection
cursor.close()
conn.close()
