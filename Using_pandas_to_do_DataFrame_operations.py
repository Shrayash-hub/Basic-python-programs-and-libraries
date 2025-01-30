import pandas as pd

#creating a simple dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25,30,35]}
df = pd.DataFrame(data)

#Display the Dataframe
print(df)

# Example of accessing a column
print("\n")
print(df['Name'])

#Example of accessing a row
print("\n")
print(df.loc[0])

#Example of simple data manipulation: adding a new column
df['City'] = ['New York', 'San Francisco', 'Los Angeles']
print("\n")
print(df)

#Example of filtering data
young_people = df[df['Age'] < 30]
print("\n")
print(young_people)

#Example of simple data manipulation
df['salary'] = [50000,60000,70000]
print("\n")
print(df)
