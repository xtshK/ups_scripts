import pyodbc

try:
    # Define the connection string
    # Replace 'your_server_name' with your SQL Server instance name or IP address
    # If using a named instance, the server name might be 'your_server_name\\your_instance_name'
    # The 'Trusted_Connection=yes' part is for Windows Authentication
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=172.21.1.14;'
        r'DATABASE=Service_SSISDB;'
        r'Trusted_Connection=yes;'
    )

    # Establish the connection
    cnxn = pyodbc.connect(conn_str)

    if cnxn:
        print("Successfully connected to the database using Windows Authentication!")

        # Create a cursor object to execute queries
        cursor = cnxn.cursor()

        # Example: Execute a query
        cursor.execute("SELECT @@VERSION;")
        db_version = cursor.fetchone()
        print(f"Database version: {db_version[0]}")

        # Example: Fetching data (uncomment to use)
        # cursor.execute("SELECT * FROM your_table_name;")
        # for row in cursor:
        #     print(row)

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    if sqlstate == '28000':
        print("Authentication failed. Check your Windows credentials and server permissions.")
    else:
        print(f"An error occurred: {ex}")
finally:
    if 'cnxn' in locals() and cnxn:
        cnxn.close()
        print("Database connection closed.")
