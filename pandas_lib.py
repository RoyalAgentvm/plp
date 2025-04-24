import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'grade': [85, 42, 95]
}

df = pd.DataFrame(data)

print(df)

# Access column
#print("Names:", df['Name'])

#ADD A COLUMN
df['Passed'] = df['grade'] > 50

# Filter rows
# print("Scores above 90:")
# print(df[df['Score'] > 90])
passed=df[df['Passed'] == True]
print(passed)


import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Year': [2021, 2022, 2023],
    'Users': [1500, 3000, 5000]
}

df = pd.DataFrame(data)

# Plot using pandas + matplotlib
plt.plot(df['Year'], df['Users'], marker='o')
plt.title("User Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()