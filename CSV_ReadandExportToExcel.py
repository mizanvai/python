

import pandas as pd
import re


# Load CSV file
df = pd.read_csv('C:\MyOne\secu.csv')

pattern = r'[\w\.-]+@[\w\.-]+'  # Regex for email addresses

# Extract the specific part of the text from the column

df["New Logon"] = df["details"].apply(lambda x: x.split()[42] if pd.notna(x) else "")
df["Network Information"] = df["details"].apply(lambda x: x.split()[83] if pd.notna(x) else "

print(df[["details", "New Logon","Network Information"]])

output_file = 'IPFile.xlsx'

df.to_excel(output_file, columns=['details', 'New Logon','Network Information'], index=False)
