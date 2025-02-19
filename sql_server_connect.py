import pyodbc
from tabulate import tabulate
# Connection details
server = 'SUD-MSS-A-12908'  # e.g., 'localhost' or 'your_server_name'
database = 'TBU_OldDb'
username = 'dataUser'  # Leave empty if using Windows Authentication
password = 'UNmiss@2025'  # Leave empty if using Windows Authentication
# Connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish connection
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"Error connecting to SQL Server: {e}")
    exit()
# Create a cursor object
cursor = conn.cursor()

# Query to fetch data from a table
table_name = 'eBillingZainMobileDataJan25'
query = f'SELECT * FROM {table_name}'

cursor.execute(query)
rows = cursor.fetchall()

print(tabulate(cursor.rowIdColumns()))
#print(tabulate(rows, rows, tablefmt="simple"))
#print(tabulate(rows, rows, tablefmt="grid"))













